from cthulhu.seasons.season1_episode1 import Season1Episode1
from cthulhu.box.episodes import EpisodesRegistry

ep_registry = EpisodesRegistry()
ep_registry.register(Season1Episode1(id="s1e1"))

all_episodes = ep_registry.episodes
