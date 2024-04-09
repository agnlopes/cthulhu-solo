from typing import Optional, Dict, List
from collections import defaultdict, deque


class Node:
    def __init__(self, id: str, value: Optional[Dict] = None):
        self.id = id
        if value:
            self.value = value
        else:
            self.value = {}

    def __str__(self):
        return f"Node {self.id} with value {self.value}"

    def __repr__(self):
        return self.__str__()


class Edge:
    def __init__(self, source: Node, target: Node, weight: int = 0):
        self.source = source
        self.target = target
        self.weight = weight

    def __str__(self):
        return (
            f"Edge from {self.source.id} to {self.target.id} with weight {self.weight}"
        )

    def __repr__(self):
        return self.__str__()


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        self.nodes[node.id] = node

    def add_nodes(self, nodes: List[Node]):
        for node in nodes:
            self.add_node(node)

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def add_edges(self, edges: List[Edge]):
        for edge in edges:
            self.add_edge(edge)

    def to_adjacency_list(self) -> Dict[str, List[str]]:
        adj_list = defaultdict(list)

        for edge in self.edges:
            adj_list[edge.source.id].append(edge.target.id)
            adj_list[edge.target.id].append(edge.source.id)

        return {key: sorted(adj) for key, adj in adj_list.items()}

    def to_adjacency_matrix(self) -> List[List[int]]:
        adj_matrix = [
            [0 for _ in range(len(self.nodes))] for _ in range(len(self.nodes))
        ]

        map_node_to_idx = {node.id: idx for idx, node in enumerate(self.nodes.values())}

        for i, node in enumerate(self.nodes.values()):
            for edge in self.edges:
                if edge.source.id == node.id:
                    adj_matrix[i][map_node_to_idx[edge.target.id]] = 1
                if edge.target.id == node.id:
                    adj_matrix[i][map_node_to_idx[edge.source.id]] = 1

        return adj_matrix

    def get_nodes_in_range(self, start: str, distance: int = 1):
        adj_list = self.to_adjacency_list()
        visited = set()
        queue = deque([(start, 0)])

        while queue:
            node, dist = queue.popleft()
            visited.add(node)
            if dist < distance:
                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, dist + 1))  # type: ignore

        return sorted(list(visited))
