#!/usr/bin/python3

import sys
from os import execv


def main():

    execv(
        sys.executable,
        [
            sys.executable,
            "-m",
            "black",
            "csvmagic/",
            "tools/",
            "--line-length",
            "80",
            *sys.argv[1:],
        ],
    )


if __name__ == "__main__":
    main()
