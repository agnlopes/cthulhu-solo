from dataclasses import dataclass, field

from cthulhu.box.enemies import Cultist
from cthulhu.box.episodes import Episode, EpisodeMap, Room
from cthulhu.box.tokens import FireToken, GateToken, PlayerStartToken


@dataclass
class Season1Episode1(Episode):
    id: str = "s1e1"
    name: str = "Blasphemous Alchemy"
    map: EpisodeMap = field(init=False)

    def __post_init__(self):
        self.map = EpisodeMap()

        # loadp map
        rooms = {
            1: Room(1, tokens=[PlayerStartToken()]),
            2: Room(2),
            4: Room(3, tokens=[FireToken()]),
            3: Room(4),
            5: Room(5, tokens=[FireToken()]),
            6: Room(6, tokens=[FireToken()]),
            7: Room(7),
            8: Room(8, tokens=[GateToken(color="blue")]),
            9: Room(9, tokens=[GateToken(color="yellow")]),
            10: Room(10),
            11: Room(11, tokens=[FireToken()]),
            12: Room(12, tokens=[FireToken()]),
            13: Room(13, tokens=[FireToken(), GateToken(color="red")]),
            14: Room(14),
            15: Room(15, tokens=[FireToken()]),
        }

        self.map.add_edge(rooms[1], rooms[2])
        self.map.add_edge(rooms[2], rooms[3])
        self.map.add_edge(rooms[2], rooms[6])
        self.map.add_edge(rooms[3], rooms[4])
        self.map.add_edge(rooms[3], rooms[6])
        self.map.add_edge(rooms[3], rooms[8])
        self.map.add_edge(rooms[3], rooms[9])
        self.map.add_edge(rooms[4], rooms[5])
        self.map.add_edge(rooms[5], rooms[9])
        self.map.add_edge(rooms[6], rooms[7])
        self.map.add_edge(rooms[7], rooms[8])
        self.map.add_edge(rooms[8], rooms[9])
        self.map.add_edge(rooms[9], rooms[10])
        self.map.add_edge(rooms[9], rooms[12])
        self.map.add_edge(rooms[10], rooms[11])
        self.map.add_edge(rooms[12], rooms[13])
        self.map.add_edge(rooms[12], rooms[15])
        self.map.add_edge(rooms[13], rooms[14])
        self.map.add_edge(rooms[14], rooms[15])
