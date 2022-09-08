#!/usr/bin/python3

import sys
from glob import glob
from os import execv


def main():
    matches = [
        *glob("csvmagic/**/*.cpp", recursive=True),
        *glob("csvmagic/**/*.hpp", recursive=True),
    ]

    execv(sys.executable,
          [sys.executable, "-m", "cpplint", *matches])


if __name__ == "__main__":
    main()
