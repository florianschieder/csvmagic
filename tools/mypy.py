#!/usr/bin/python3

import sys
from os import execv


def main():

    execv(
        sys.executable,
        [
            sys.executable,
            "-m",
            "mypy",
            "csvmagic/",
            # This is required since mypy cannot find a
            # module stub for a module which is implemented
            # as a C extension.
            "--ignore-missing-imports",
            "--strict-equality",
            "--strict-optional",
            "--disallow-untyped-defs",
            "--warn-redundant-casts",
            "--warn-unreachable",
            "--warn-no-return",
        ],
    )


if __name__ == "__main__":
    main()
