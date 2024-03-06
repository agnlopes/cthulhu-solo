from dataclasses import dataclass, field
from typing import List

from cthulhu.box.enemies import ElderOne, all_elder_ones
from cthulhu.box.episodes import Episode
from cthulhu.box.investigators import Investigator, all_investigators
from cthulhu.exceptions import InvestigatorNotFound
from cthulhu.seasons import all_episodes


@dataclass
class CthulhuGame:
    selected_investigators: List[str]
    investigators: List[Investigator] = field(default_factory=list)
    elder_one_selected: str = "cthulhu"
    elder_one: ElderOne = field(init=False)
    selected_season: str = "1"
    selected_episode: str = "1"
    episode: Episode = field(init=False)

    def __post_init__(self):
        self.setup()

    def setup(self):
        # episode
        _season, _episode = (
            f"season{self.selected_season}",
            f"episode{self.selected_episode}",
        )
        self.season = self.selected_season
        self.episode_id = all_episodes[f"{_season}_{_episode}"].id

        # investigators
        for investigator in self.selected_investigators:
            if investigator not in all_investigators:
                raise InvestigatorNotFound(investigator)
            self.investigators.append(all_investigators[investigator])

        # elder one
        if self.elder_one_selected not in all_elder_ones:
            # TODO: create an exception for this
            raise ValueError(self.elder_one_selected)
        self.elder_one = all_elder_ones[self.elder_one_selected]

    def start(self):
        for investigator in self.investigators:
            print(investigator.name)
            print(investigator.skills)
