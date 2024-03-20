import argparse

from cthulhu.game import CthulhuGame, CthulhuGameController
from cthulhu.box.investigators import all_investigators
from cthulhu.seasons import all_episodes


def argparser():
    seasons = list(all_episodes.keys())
    print(seasons)
    parser = argparse.ArgumentParser(description="Mythos's Cthulhu Death May Die")

    # TODO: valid seasons and players are hardcoded, should be read from the config file, or from the game itself
    parser.add_argument(
        "-s",
        "--season",
        dest="season",
        type=str,
        default="1",
        help="Season to be played, valid values are: 1, 2, 3",
    )
    parser.add_argument(
        "-e",
        "--episode",
        dest="episode",
        type=str,
        default="1",
        help="Episode to be played, valid values are: 1, 2, 3, 4, 5, 6",
    )
    parser.add_argument(
        "-eo",
        "--elder-one",
        dest="elder_one",
        type=str,
        default="cthulhu",
        help="Elder One to be played, valid values are: cthulhu",
    )
    parser.add_argument(
        "-i",
        "--investigator",
        dest="investigators",
        type=str,
        action="append",
        default=[],
        help="investigator's name, valid values are: beth",
    )
    parser.add_argument(
        "-v",
        dest="verbosity",
        action="count",
        default=0,
        help="log verbosity level -v=info, -vv=error, -vvv=debug",
    )
    return parser.parse_args()


def main():
    args = argparser()
    game = CthulhuGame(
        selected_investigators=args.investigators,
        selected_season=args.season,
        selected_episode=args.episode,
        elder_one_selected=args.elder_one,
    )
    controller = CthulhuGameController(game, verbosity=0)
    controller.ui.run()


if __name__ == "__main__":
    main()
