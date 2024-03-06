from dataclasses import dataclass

from cthulhu.box.tokens import FireToken, GateToken, PlayerStartToken
from cthulhu.box.enemies import Cultist
from cthulhu.box.episodes import Episode, Room, EpisodeMap, EpisodesRegistry


@dataclass
class Season1Episode1(Episode):
    id: str = "season1_episode1"
    name: str = "Blasphemous Alchemy"

    def __post_init__(self):
        rooms = {
            1: Room(1, tokens=[PlayerStartToken()]),
            2: Room(2, enemies=[Cultist()] * 2),
            4: Room(3, tokens=[FireToken()], enemies=[Cultist()]),
            3: Room(4),
            5: Room(5, tokens=[FireToken()], enemies=[Cultist()]),
            6: Room(6, tokens=[FireToken()]),
            7: Room(7, enemies=[Cultist()]),
            8: Room(8, tokens=[GateToken(color="blue")]),
            9: Room(9, tokens=[GateToken(color="yellow")]),
            10: Room(10, enemies=[Cultist()]),
            11: Room(11, tokens=[FireToken()]),
            12: Room(12, tokens=[FireToken()]),
            13: Room(13, tokens=[FireToken(), GateToken(color="red")]),
            14: Room(14, enemies=[Cultist()]),
            15: Room(15, tokens=[FireToken()]),
        }

        map: EpisodeMap = EpisodeMap()
        map.add_edge(rooms[1], rooms[2])
        map.add_edge(rooms[2], rooms[3])
        map.add_edge(rooms[2], rooms[6])
        map.add_edge(rooms[3], rooms[4])
        map.add_edge(rooms[3], rooms[6])
        map.add_edge(rooms[3], rooms[8])
        map.add_edge(rooms[3], rooms[9])
        map.add_edge(rooms[4], rooms[5])
        map.add_edge(rooms[5], rooms[9])
        map.add_edge(rooms[6], rooms[7])
        map.add_edge(rooms[7], rooms[8])
        map.add_edge(rooms[8], rooms[9])
        map.add_edge(rooms[9], rooms[10])
        map.add_edge(rooms[9], rooms[12])
        map.add_edge(rooms[10], rooms[11])
        map.add_edge(rooms[12], rooms[13])
        map.add_edge(rooms[12], rooms[15])
        map.add_edge(rooms[13], rooms[14])
        map.add_edge(rooms[14], rooms[15])


episodes_registry = EpisodesRegistry()
episodes_registry.register(Season1Episode1())
