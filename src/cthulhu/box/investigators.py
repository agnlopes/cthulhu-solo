from dataclasses import dataclass, field
from typing import List

from cthulhu.box.skills import (
    ArcaneMasterySkill,
    BrawlingSkill,
    FueledByMadnessSkill,
    GateManipulationSkill,
    HealingPrayerSkill,
    HighStrungSkill,
    LuckySkill,
    MarksmanSkill,
    ProtectorSkill,
    ReadTheOmensSkill,
    SavageSkill,
    Skill,
    StealthSkill,
    SwiftnessSkill,
    ThoughnessSkill,
    UnkillableSkill,
    VengeanceObsessionSkill,
)
from transitions import Machine, State

type TypeInvestigator = Investigator


@dataclass
class Investigator[TypeInvestigator]:
    name: str = "Investigator Name"
    long_name: str = "Investigator Long Name"
    quote: str = "Some snarky words"
    origin: str = ""
    description: str = ""
    insanity: int = 0
    max_insanity: int = 15
    health: int = 5
    max_health: int = 0
    stress: int = 5
    max_stress: int = 5
    skills: List[Skill] = field(default_factory=list)
    actions: int = 3
    actions_left: int = 3
    actions_free: List[str] = field(default_factory=list)
    is_safe: bool = True
    is_alive: bool = True
    is_standing: bool = True
    room_id: int = 0
    fsm: Machine = field(init=False)

    def __post_init__(self):
        self.set_fsm()

    def set_fsm(self):
        machine_states = [
            State(name="waiting", on_enter="wait_for_turn"),
            State(name="playing", on_enter="play_actions"),
            State(name="mythos", on_enter="draw_mythos_card"),
            State(name="investigate", on_enter="investigate_or_fight"),
            State(name="resolv", on_enter="resolv_end_of_turn"),
        ]
        self.fsm = Machine(self, states=machine_states, initial="waiting")


@dataclass
class BethInvestigator(Investigator):
    name: str = "Beth"
    long_name: str = "Sister Beth"
    origin: str = "Bogota, Colombia"
    description: """
    Sister Beth knows not what God's plan for ther may be, except that she'll likely meet him very soon. Afflicted at an early age with a nervous nature, young Beth made the rounds through various hospitals and sanitariums before finding peace (and fatalism) in church. Were it not for the insulation her faith provides her psyche, she would have survived her first encounter with the Old Ones and their cults. Since then, she's become an expert on the occult and their horrific practices, justified in the beliefe that the day she finally falls will be the day of her ultimate salvation."
    """
    skills: List[Skill] = field(
        default_factory=lambda: [HighStrungSkill(), BrawlingSkill(), ThoughnessSkill()]
    )


@dataclass
class FatimaInvestigator(Investigator):
    name: str = "Fatima"
    skills: List[Skill] = field(
        default_factory=lambda: [
            ReadTheOmensSkill(),
            ArcaneMasterySkill(),
            SwiftnessSkill(),
        ]
    )


@dataclass
class ElizabethInvestigator(Investigator):
    name: str = "Elizabeth"
    skills: List[Skill] = field(
        default_factory=lambda: [LuckySkill(), MarksmanSkill(), StealthSkill()]
    )


@dataclass
class AhmedInvestigator(Investigator):
    name: str = "Ahmed"
    skills: List[Skill] = field(
        default_factory=lambda: [
            HealingPrayerSkill(),
            StealthSkill(),
            ArcaneMasterySkill(),
        ]
    )


@dataclass
class MorganInvestigator(Investigator):
    name: str = "Morgan"
    skills: List[Skill] = field(
        default_factory=lambda: [ProtectorSkill(), SwiftnessSkill(), ThoughnessSkill()]
    )


@dataclass
class IanInvestigator(Investigator):
    name: str = "Ian"
    skills: List[Skill] = field(
        default_factory=lambda: [
            VengeanceObsessionSkill(),
            BrawlingSkill(),
            SwiftnessSkill(),
        ]
    )


@dataclass
class RasputinInvestigator(Investigator):
    name: str = "Rasputin"
    skills: List[Skill] = field(
        default_factory=lambda: [
            UnkillableSkill(),
            ArcaneMasterySkill(),
            BrawlingSkill(),
        ]
    )


@dataclass
class BordenInvestigator(Investigator):
    name: str = "Borden"
    skills: List[Skill] = field(
        default_factory=lambda: [SavageSkill(), SwiftnessSkill(), StealthSkill()]
    )


@dataclass
class AdamInvestigator(Investigator):
    name: str = "Adam"
    skills: List[Skill] = field(
        default_factory=lambda: [
            FueledByMadnessSkill(),
            MarksmanSkill(),
            ThoughnessSkill(),
        ]
    )


@dataclass
class TheKidInvestigator(Investigator):
    name: str = "The Kid"
    skills: List[Skill] = field(
        default_factory=lambda: [
            GateManipulationSkill(),
            MarksmanSkill(),
            ArcaneMasterySkill(),
        ]
    )


all_investigators = {
    "beth": BethInvestigator(),
    "fatima": FatimaInvestigator(),
    "elizabeth": ElizabethInvestigator(),
    "ahmed": AhmedInvestigator(),
    "morgan": MorganInvestigator(),
    "ian": IanInvestigator(),
    "rasputin": RasputinInvestigator(),
    "borden": BordenInvestigator(),
    "adam": AdamInvestigator(),
    "thekid": TheKidInvestigator(),
}
