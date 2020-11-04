from argparse import ArgumentParser
from fmovies_api import Fmovies, FmoviesConfig

import os
import re


class Application():
    def __init__(self):
        self.config_data = {}

    def setup_parser():
        parser = ArgumentParser()

        parser.add_argument("-u", "--base-url",
                            help="The base url for the website.")
        parser.add_argument(
            "--search-path", help="Absolute or relative url to search page. If relative, base-url must be supplied.")
        parser.add_argument("-c", "--config-file",
                            help="Input file for the configuration.")

        self.data = FmoviesConfig.parse(parser.parse_args(), type=(
            "file" if parser.config_file else "data"))


def main():
    pass


if __name__ == "__main__":
    setup_parser()
    main()
