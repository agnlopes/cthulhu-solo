from cthulhu.box.investigators import all_investigators


class EpisodeNotFound(Exception):
    def __init__(self, episode_name):
        self.message = f"Episode: {episode_name} not found"
        super().__init__(self.message)


class ElderOneNotFound(Exception):
    def __init__(self, elder_one):
        self.message = f"Elder One: {elder_one} not found"
        super().__init__(self.message)


class InvestigatorNotFound(Exception):
    def __init__(self, investigator_name):
        if investigator_name not in all_investigators:
            self.message = f"Investigator: {investigator_name} not found"
            super().__init__(self.message)
