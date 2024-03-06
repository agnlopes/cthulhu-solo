import argparse

from cthulhu.game import CthulhuGame


def argparser():
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
        required=True,
        help="investigator's name, valid values are: beth",
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
    game.start()


if __name__ == "__main__":
    main()
