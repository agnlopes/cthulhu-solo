from dataclasses import dataclass, field
from typing import List
from cthulhu.box.dice import CthulhuBonusDie, CthulhuDie, CthulhuStandardDie
from cthulhu.box.decks import (
    MythosCardsDeck,
    MythosCard,
    DiscoveryCardsDeck,
    DiscoveryCard,
    DiscoveryCardItem,
)

type TypeEnemy = Enemy
type TypeCultist = Cultist
type TypeMonster = Monster
type TypeElderOne = ElderOne


@dataclass
class Enemy[TypeEnemy]:
    health: int = 0
    max_health: int = 0
    dice = List[CthulhuDie]
    is_dead: bool = False
    is_standing: bool = True


@dataclass
class ElderOne[Enemy]:
    name: str = "ElderOne"
    mythos_deck: MythosCardsDeck = field(default_factory=MythosCardsDeck)


@dataclass
class Monster[TypeMonster](Enemy):
    name: str = "Monster"


@dataclass
class Cultist[TypeCultist](Enemy):
    name: str = "Cultist"
    health: int = 2
    max_health: int = 2
    dice: List[CthulhuBonusDie] = field(default_factory=lambda: [CthulhuBonusDie()] * 2)


@dataclass
class StarSpawnMonster[TypeMonster](Monster):
    name: str = "StarSpawn"
    health: int = 7
    max_health: int = 7
    dice: List[CthulhuDie] = field(default_factory=lambda: [CthulhuStandardDie()] * 3)


@dataclass
class ElderOneCthulhu[TypeElderOne](ElderOne):
    name: str = "Cthulhu"
    level: int = 1
    health: int = 12
    max_health: int = 12
    dice: List[CthulhuDie] = field(default_factory=lambda: [CthulhuStandardDie()] * 3)
    is_killable: bool = False
    is_on_board: bool = False
    mythos_deck: MythosCardsDeck = field(init=False)
    discovery_deck: DiscoveryCardsDeck = field(init=False)

    def __post_init__(self):
        self.mythos_deck = MythosCardsDeck()
        mythos_cards = [
            MythosCard(name="xxx", description="", mythos_symbol=False),
            MythosCard(name="yyy", description="", mythos_symbol=False),
            MythosCard(name="zzz", description="", mythos_symbol=False),
        ]
        for card in mythos_cards:
            self.mythos_deck.add(card)

    def move_on_track(self):
        self.position_on_track += 1

    def levelup(self):
        self.level += 1
        self.health = 12
        self.max_health = 12
        self.dice.append(CthulhuBonusDie())
        self.position_on_track: int = 1


all_elder_ones = {"cthulhu": ElderOneCthulhu()}
