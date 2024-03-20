from typing import Dict, List, Tuple, Optional, TypeVar, Generic
from dataclasses import dataclass, field
from transitions import State, Machine

type TypeSkill = Skill
type TypeInvestigator = Investigator


@dataclass
class Skill[TypeSkill]:
    name: str
    level: int = 1
    levels = Dict[int, str]


@dataclass
class Investigator[TypeInvestigator]:
    name: str = "Player"
    insanity: int = 0
    max_insanity: int = 15
    health: int = 5
    max_health: int = 0
    stress: int = 5
    max_stress: int = 5
    skills = List[Skill]
    actions: int = 3
    actions_left: int = 3
    actions_free: List[str] = field(default_factory=list)
    is_safe: bool = True
    is_alive: bool = True
    is_standing: bool = True
    room: int = 0
    fsm: Machine = field(init=False)

    def __post_init__(self):
        self.set_fsm()

    def set_fsm(self):
        machine_states = [
            State(name="playing", on_enter="play_actions"),
            State(name="mythos", on_enter="draw_mythos_card"),
            State(name="investigate", on_enter="investigate_or_fight"),
            State(name="resolv", on_enter="resolv_end_of_turn"),
        ]

        self.fsm = Machine(self, states=machine_states, initial="playing")


@dataclass
class SkillStealth(Skill):
    name: str = "Stealth"
    levels = {
        1: "When you move, you may sneak past 1 enemy, so he doesnt follow you.",
        2: "When you move, you may sneak past 2 enemies, so he doesnt follow you.",
        3: "When you move, you may sneak past 3 enemies, so he doesnt follow you.",
        4: "When you move, you may sneak past 4 enemies, so he doesnt follow you.",
    }


@dataclass
class SkillSwiftness(Skill):
    name: str = "Swiftness"
    levels = {
        1: "You may move 1 additional space.",
        2: "You may move 2 additional spaces.",
        3: "You may move 3 additional spaces.",
        4: "You may move 4 additional spaces.",
    }


@dataclass
class SkillThouthness(Skill):
    name: str = "Toughness"
    levels = {
        1: "You may ignore 1 damage.",
        2: "You may ignore 2 damage.",
        3: "You may ignore 3 damage.",
        4: "You may ignore 4 damage.",
    }


@dataclass
class InvestigatorBeth(Investigator):
    name: str = "Beth"
    skills = [SkillStealth(), SkillSwiftness(), SkillThouthness()]


all_investigators = {"beth": InvestigatorBeth()}
