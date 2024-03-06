from collections import defaultdict

from cthulhu.box.dice import CthulhuBonusDie, CthulhuStandardDie
from cthulhu.game import CthulhuGame


# test game instantiation
def test_game_instantiation():
    game = CthulhuGame(
        selected_investigators=["beth"],
        elder_one_selected="cthulhu",
        selected_season="1",
        selected_episode="1",
    )
    assert game.episode_id == "season1_episode1"
    assert game.investigators[0].name == "Beth"
    assert game.elder_one.name == "Cthulhu"


# test game standard dice
def test_game_standard_dice():
    cthulhu_standard_die = CthulhuStandardDie()
    cthulhu_standard_die_faces = defaultdict(int)
    for face in cthulhu_standard_die.faces:
        for value in face.values:
            cthulhu_standard_die_faces[value] += 1
    assert len(cthulhu_standard_die.faces) == 6
    assert cthulhu_standard_die_faces["Blank"] == 1
    assert cthulhu_standard_die_faces["Success"] == 3
    assert cthulhu_standard_die_faces["Tentacle"] == 2
    assert cthulhu_standard_die_faces["ElderSign"] == 1


# test game bonus dice
def test_game_bonus_dice():
    cthulhu_bonus_die = CthulhuBonusDie()
    cthulhu_bonus_die_faces = defaultdict(int)
    for face in cthulhu_bonus_die.faces:
        for value in face.values:
            cthulhu_bonus_die_faces[value] += 1
    assert len(cthulhu_bonus_die.faces) == 6
    assert cthulhu_bonus_die_faces["Blank"] == 2
    assert cthulhu_bonus_die_faces["Success"] == 3
    assert cthulhu_bonus_die_faces["ElderSign"] == 2
