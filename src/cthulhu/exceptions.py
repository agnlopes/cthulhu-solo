from cthulhu.box.investigators import all_investigators


class EpisodeNotFound(Exception):
    def __init__(self, episode_name):
        self.message = f"Episode: {episode_name} not found"
        super().__init__(self.message)


class EnemyNotFound(Exception):
    def __init__(self, enemy_name):
        self.message = f"Enemy: {enemy_name} not found"
        super().__init__(self.message)


class InvestigatorNotFound(Exception):
    def __init__(self, investigator_name):
        if investigator_name not in all_investigators:
            self.message = f"Investigator: {investigator_name} not found"
            super().__init__(self.message)
