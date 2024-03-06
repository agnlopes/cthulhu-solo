from collections import defaultdict
from dataclasses import dataclass, field
from typing import DefaultDict, Iterable, List

from cthulhu.box.enemies import Enemy
from cthulhu.box.investigators import Investigator
from cthulhu.box.tokens import Token


@dataclass
class Exit:
    direction: str
    to_room: "Room"
    is_locked: bool = False


@dataclass
class Room:
    id: int
    items: List[str] = field(default_factory=list)
    enemies: List[Enemy] = field(default_factory=list)
    investigators: List[Investigator] = field(default_factory=list)
    exits: List[Exit] = field(default_factory=list)
    tokens: List[Token] = field(default_factory=list)

    def __str__(self):
        return str(self.id)


@dataclass
class EpisodeMap:
    adj_list: DefaultDict = field(default_factory=lambda: defaultdict(list))

    def add_edge(self, src: Room, dst: Room):
        self.adj_list[src.id].append(dst)
        self.adj_list[dst.id].append(src)

    def display(self):
        for item in self.adj_list:
            print(item)


@dataclass
class Episode:
    id: str
    name: str
    map: List[Room] = field(default_factory=list)
    actions: List[Iterable] = field(default_factory=list)
    rules: List[Iterable] = field(default_factory=list)

    def map_from_json(self, map: List[dict]):
        for room in map:
            self.map.append(Room(**room))


class EpisodesRegistry:
    _instance = None
    episodes: DefaultDict

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(EpisodesRegistry, cls).__new__(cls)
            cls._instance.episodes = defaultdict()
        return cls._instance

    def register(self, episode: Episode):
        self.episodes[episode.id] = episode
