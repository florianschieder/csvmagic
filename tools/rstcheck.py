#!/usr/bin/python3

import sys
from glob import glob
from os import execv


def main():
    matches = [
        *glob("*.rst", recursive=True),
    ]

    execv(sys.executable,
          [sys.executable,
           "-m", "rstcheck._cli",
           *matches])


if __name__ == "__main__":
    main()
