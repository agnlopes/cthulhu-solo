from typing import List, Type
from dataclasses import dataclass, field
import random

type TypeCthulhuDie = CthulhuStandardDie | CthulhuBonusDie


@dataclass
class DieFace:
    values: List[str]


@dataclass
class BlankDieFace(DieFace):
    values: List[str] = field(default_factory=lambda: ["Blank"])


@dataclass
class SuccessDieFace(DieFace):
    values: List[str] = field(default_factory=lambda: ["Success"])


@dataclass
class TentacleDieFace(DieFace):
    values: List[str] = field(default_factory=lambda: ["Tentacle"])


@dataclass
class ElderSignDieFace(DieFace):
    values: List[str] = field(default_factory=lambda: ["ElderSign"])


@dataclass
class TentacleSucessDieFace(DieFace):
    values: List[str] = field(default_factory=lambda: ["Tentacle", "Success"])


@dataclass
class ElderSignSuccessDieFace(DieFace):
    values: List[str] = field(default_factory=lambda: ["ElderSign", "Success"])


@dataclass
class Die:
    faces: List[DieFace]

    def roll(self):
        return random.choice(self.faces)


@dataclass
class CthulhuDie[TypeCthulhuDie](Die):
    faces: List[DieFace] = field(default_factory=list)
    blank: int = 0
    success: int = 0
    tentacle: int = 0
    tentacle_success: int = 0
    eldersign: int = 0
    eldersign_success: int = 0

    def __post_init__(self):

        if self.blank:
            self.faces.extend([BlankDieFace() for _ in range(0, self.blank)])

        if self.success:
            self.faces.extend([SuccessDieFace() for _ in range(0, self.success)])

        if self.tentacle:
            self.faces.extend([TentacleDieFace() for _ in range(0, self.tentacle)])

        if self.tentacle_success:
            self.faces.extend(
                [TentacleSucessDieFace() for _ in range(0, self.tentacle_success)]
            )

        if self.eldersign:
            self.faces.extend([ElderSignDieFace() for _ in range(0, self.eldersign)])

        if self.eldersign_success:
            self.faces.extend(
                [ElderSignSuccessDieFace() for _ in range(0, self.eldersign_success)]
            )


@dataclass
class CthulhuStandardDie(CthulhuDie):
    blank: int = 1
    success: int = 2
    tentacle: int = 1
    eldersign: int = 1
    tentacle_success: int = 1


@dataclass
class CthulhuBonusDie(CthulhuDie):
    blank: int = 2
    success: int = 2
    eldersign: int = 1
    eldersign_success: int = 1
