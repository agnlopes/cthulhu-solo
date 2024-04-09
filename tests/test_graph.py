from cthulhu.utils.graph import Graph, Node, Edge

# test Node initialization
def test_node_initialization():
    node = Node("A")
    assert node.id == "A"
    assert node.value == {}

# test Edge initialization
def test_edge_initialization():
    edge = Edge(Node("A"), Node("B"))
    assert edge.source.id == "A"
    assert edge.target.id == "B"

# test Graph initialization
def test_graph_initialization():
    graph = Graph()
    assert graph.nodes == {}
    assert graph.edges == []

# test add node to graph
def test_graph_add_node():
    graph = Graph()
    node1 = Node("A")
    node2 = Node("B")
    graph.add_node(node1)
    assert graph.nodes == {"A": node1}
    graph.add_node(node2)
    assert graph.nodes == {"A": node1, "B": node2}

# test represent graph as adjancency list
def test_graph_adjacency_list():
    graph = Graph()
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    graph.add_nodes([node_a, node_b, node_c, node_d])
    graph.add_edge(Edge(node_a, node_b))
    graph.add_edge(Edge(node_b, node_c))
    graph.add_edge(Edge(node_c, node_d))
    graph.add_edge(Edge(node_d, node_a))
    assert graph.to_adjacency_list() == {"A": ["B", "D"], "B": ["A", "C"], "C": ["B", "D"], "D":["A", "C"]}

# test represent graph as adjancency matrix
def test_graph_adjacency_matrix():
    graph = Graph()
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    graph.add_nodes([node_a, node_b, node_c, node_d])
    graph.add_edge(Edge(node_a, node_b))
    graph.add_edge(Edge(node_b, node_c))
    graph.add_edge(Edge(node_c, node_d))
    graph.add_edge(Edge(node_d, node_a))
    assert graph.to_adjacency_matrix() == [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
    ]

def test_graph_nodes_in_range():
    graph = Graph()
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E")
    graph.add_nodes([node_a, node_b, node_c, node_d, node_e])
    graph.add_edge(Edge(node_a, node_b))
    graph.add_edge(Edge(node_b, node_c))
    graph.add_edge(Edge(node_c, node_d))
    graph.add_edge(Edge(node_d, node_a))
    graph.add_edge(Edge(node_c, node_e))
    assert graph.get_nodes_in_range("A", 2) == ["A", "B", "C", "D"]
    assert graph.get_nodes_in_range("B", 1) == ["A", "B", "C"]
    assert graph.get_nodes_in_range("E", 1) == ["C", "E"]

