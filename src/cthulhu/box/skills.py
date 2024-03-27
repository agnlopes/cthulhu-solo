from dataclasses import dataclass, field
from typing import Dict, Callable, List

type TypeSkill = Skill


@dataclass
class SkillLevel:
    description: str = field(default_factory=str)
    actions: List[Callable] = field(default_factory=list)


@dataclass
class Skill[TypeSkill]:
    name: str
    level: int = 1
    levels: Dict[int, SkillLevel] = field(default_factory=dict)


@dataclass
class GateManipulationSkill(Skill):
    # these actions should run on gate spawn
    name: str = "Gate Manipulation"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="If you are in the same space as a `Gate`, `Monsters` and `Cultists` summoned there take wounds equal to half their health (rounded up)",
            ),
            2: SkillLevel(
                description="This skill works if you are within 1 space of a `Gate`",
            ),
            3: SkillLevel(
                description="if you are within 1 space of a `Gate`, you are always considered `Safe` to `Rest`",
            ),
            4: SkillLevel(
                description="If you are within 1 space of a `Gate`, you gain 1 `BonusDie` and have 1 free `Rest` action",
            ),
        }


@dataclass
class SavageSkill(Skill):
    # these actions should run when the investigator attacks (every roll)
    name: str = "Savage"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="When attacking, you may deal 1 additional wound to your target if there are no other `Enemies` in its space",
            ),
            2: SkillLevel(
                description="You may deal 1 additional wound (2 total)",
            ),
            3: SkillLevel(
                description="If you kill the target and there are no other `Enemies` in its space, heal all your `Stress`",
            ),
            4: SkillLevel(
                description="You may deal 3 additional wounds (5 total)",
            ),
        }


@dataclass
class SwiftnessSkill(Skill):
    name: str = "Swiftness"

    def __post__init__(self):
        self.levels = {
            1: SkillLevel(
                description="When you Run you may move 1 additional space",
            ),
            2: SkillLevel(
                description="You have 1 free `Run` action each `Turn`",
            ),
            3: SkillLevel(
                description="During a `Run` you may take 1 `Investigator` with you when leaving a space",
            ),
            4: SkillLevel(description="You have 1 extra `Action` each `Turn`"),
        }


@dataclass
class UnkillableSkill(Skill):
    name: str = "Unkillable"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="1 free `Death`: If you would die from wounds, instead return to life with full health",
            ),
            2: SkillLevel(
                description="1 additional free `Death` (2 total)",
            ),
            3: SkillLevel(
                description="When you return to life, also heall all your `Stress`",
            ),
            4: SkillLevel(
                description="1 additional free `Death` (3 total)",
            ),
        }


@dataclass
class VengeanceObsessionSkill(Skill):
    name: str = "Vengeance Obsession"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="When attacked, if you are dealt wounds, deal 1 `Wound` to that `Enemy` and heal 1 `Stress`",
            ),
            2: SkillLevel(
                description="Instead, deal 1 `Wound` to each `Enemy` in the attacker's space and heal 1 `Stress`",
            ),
            3: SkillLevel(
                description="Instead, deal 1 `Wound` to each `Enemy` in the attacker's space and heal 2 `Stress`",
            ),
            4: SkillLevel(
                description="Instead, deal 2 `Wound` to each enemy in the attacker's space and heal 2 `Stress`",
            ),
        }


@dataclass
class ProtectorSkill(Skill):
    name: str = "Protector"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="If an `Investigator` in your space is attacked, you may redirect the attack to you (before the roll)",
            ),
            2: SkillLevel(
                description="You may redirect to you an attack made against an `Investigator` up to 1 space away",
            ),
            3: SkillLevel(
                description="You have 2 free `Reroll` when being attacked and redirected attack",
            ),
            4: SkillLevel(
                description="After resolving a redirected attack, heall all your `Stress`",
            ),
        }


@dataclass
class HealingPrayerSkill(Skill):
    name: str = "Healing Prayer"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="At the end of your turn, you may heal 1 `Stress` OR `Wound` on an `Investigator` in your space (it may be yourself)",
            ),
            2: SkillLevel(
                description="Instead, heal 2 in any combination of `Stress` and `Wound`",
            ),
            3: SkillLevel(description="Instead, heal 2 `Stress` AND 2 `Wound`"),
            4: SkillLevel(
                description="Instead, heal 2 `Stress` AND 2 `Wound` on each `Investigator` in your space"
            ),
        }


@dataclass
class LuckySkill(Skill):
    name: str = "Lucky"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="You have 1 free `Reroll` per `Turn`",
            ),
            2: SkillLevel(
                description="You have 1 additional `Reroll` per `Turn` (2 total)",
            ),
            3: SkillLevel(
                description="You have 1 additional `Reroll` per `Turn` (3 total)",
            ),
            4: SkillLevel(description="Instead, you have 3 free `Reroll` per `Roll`"),
        }


@dataclass
class ReadTheOmensSkill(Skill):
    name: str = "Read The Omens"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="You may put the first `Mythos` card you draw each `Turn` at the bottom of the deck and draw again. If you do, heal 2 stress",
            ),
            2: SkillLevel(
                description="Instead, draw 2 `Mythos` cards, choose 1 to play, and put the other underneath the deck. Heal 2 stress",
            ),
            3: SkillLevel(
                description="Instead, if you draw 2 cards to choose from heal ALL of your `Stress`",
            ),
            4: SkillLevel(
                description="You may take 2 `Wound` to cancel any `Mythos` card's special effect and `Enemy` summoning",
            ),
        }


@dataclass
class StealthSkill(Skill):
    name: str = "Stealth"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="When you `Run`, you may sneak once (one `Enemy doesn't follow you`)",
            ),
            2: SkillLevel(
                description="Instead, when you `Run` you may sneak 3 times",
            ),
            3: SkillLevel(
                description="Deal 1 `Wound` to each `Enemy` you sneak past",
            ),
            4: SkillLevel(
                description="Instead, you may Sneak any number of times",
            ),
        }


@dataclass
class FueledByMadnessSkill(Skill):
    name: str = "Fueled By Madness"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="Gain 1 `BonusDie` while your `Sanity` is on a `InsanityTreshold`",
            ),
            2: SkillLevel(
                description="Instead, gain 1 `BonusDie` while your `Sanity` is on a `InsanityTreshold OR 1 space back`",
            ),
            3: SkillLevel(
                description="Instead, gain 2 `BonusDie` while your `Sanity` is on a `InsanityTreshold OR 1 space back`",
            ),
            4: SkillLevel(
                description="Instead, gain 3 `BonusDie` while your `Sanity` is on a `InsanityTreshold OR 1 space back`",
            ),
        }


@dataclass
class HighStrungSkill(Skill):
    name: str = "High Strung"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="When making any `Roll` you may count 1 `Tentacle` as 1 success (it still also count as a `Tentacle`)",
            ),
            2: SkillLevel(
                description="Instead, you may count any number of `Tentacle` as successes (they still also count as `Tentacle`)",
            ),
            3: SkillLevel(
                description="Heal 1 of your `Wound` for each `Tentacle` you count as success",
            ),
            4: SkillLevel(
                description="Also, If you rolled at least 2 `Tentacle`, you may add 3 successes to the `Roll`"
            ),
        }


@dataclass
class BrawlingSkill(Skill):
    name: str = "Brawling"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="Gain 1 `BonusDie` when attacking a target in your space",
            ),
            2: SkillLevel(
                description="When you attack, you may target ANY NUMBER of figures (split the wounds as you like)",
            ),
            3: SkillLevel(
                description="You have 2 free `Reroll` when attacking a target in your space",
            ),
            4: SkillLevel(
                description="When you attack figures in your space, deal the full `Wound` to each target",
            ),
        }


@dataclass
class ThoughnessSkill(Skill):
    name: str = "Thoughness"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="You have 1 free `Reroll` when attacked or rolling for fire",
            ),
            2: SkillLevel(
                description="Instead, you may reduce `Wound` taken and loss of `Sanity` by 1 when attacked or rolling for fire",
            ),
            3: SkillLevel(
                description="Instead, you may reduce `Wound` taken and loss of `Sanity` by 1 from ANY SOURCE",
            ),
            4: SkillLevel(
                description="Instead, you may reduce `Wound` taken by 2 and loss of `Sanity` by 1 from ANY SOURCE",
            ),
        }


@dataclass
class MarksmanSkill(Skill):
    name: str = "Marksman"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="You may attack a target 1 space away",
            ),
            2: SkillLevel(
                description="Gain 2 `BonusDie` when attacking a target not in your space",
            ),
            3: SkillLevel(
                description="You may attack a target 1 additional space away (2 total)",
            ),
            4: SkillLevel(
                description="You may perform 1 free attack per `Turn` against a target not in your space",
            ),
        }


@dataclass
class ArcaneMasterySkill(Skill):
    name: str = "Arcane Mastery"

    def __post_init__(self):
        self.levels = {
            1: SkillLevel(
                description="When making any `Roll`, you may count `Arcane` as a success",
            ),
            2: SkillLevel(
                description="Instead, you may count any number of `Arcane` as successes",
            ),
            3: SkillLevel(
                description="Heal 1 `Stress` for each `Arcane` you count as a success",
            ),
            4: SkillLevel(
                description="You may count any number of `Arcane` as 2 sucesses each",
            ),
        }
