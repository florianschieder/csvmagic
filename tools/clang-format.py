#!/usr/bin/python3

from glob import glob
from subprocess import PIPE, run
from sys import exit


def main():
    matches = [
        *glob("csvmagic/**/*.cpp", recursive=True),
        *glob("csvmagic/**/*.hpp", recursive=True),
        *glob("csvmagic/**/*.c", recursive=True),
        *glob("csvmagic/**/*.h", recursive=True),
    ]

    output = run(
        ["clang-format", "--Werror", "--style=google", "--dry-run", *matches],
        stderr=PIPE,
    ).stderr
    lines = output.decode().splitlines()

    if len(lines) % 3 != 0:
        print("got an unexpected output format. output follows:")
        for line in lines:
            print(line)
        exit(1)

    else:
        # clang sometimes complains about legitimate constructs.
        # We append these lines with "noqa" like in Python.
        # We want our tool to strip those errors and only exit with
        # return code 1 if something is not alright.

        for i in range(0, int(len(lines) / 3)):
            # example output:
            # lines[i * 3]       = foo.c:1:337: error: code should (...)
            # lines[(i * 3) + 1] =    foobar this is the broken line {
            # lines[(i * 3) + 2] =                                   ^

            broken_line = lines[(i * 3) + 1]

            if broken_line.endswith("  // noqa"):
                lines[(i * 3) + 0] = None
                lines[(i * 3) + 1] = None
                lines[(i * 3) + 2] = None

        filtered_lines = list(filter(lambda it: it is not None, lines))
        if filtered_lines:
            for line in filtered_lines:
                print(line)
            exit(1)


if __name__ == "__main__":
    main()
