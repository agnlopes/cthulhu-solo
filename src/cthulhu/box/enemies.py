from cthulhu.box.dice import (
    CthulhuStandardDie,
    CthulhuBonusDie,
    CthulhuDie,
)
from typing import List
from dataclasses import dataclass, field

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
    position_on_track: int = 1
    is_killable: bool = False
    is_on_board: bool = False

    def move_on_track(self):
        self.position_on_track += 1

    def levelup(self):
        self.level += 1
        self.health = 12
        self.max_health = 12
        self.dice.append(CthulhuBonusDie())
        self.position_on_track: int = 1


all_elder_ones = {"cthulhu": ElderOneCthulhu()}
