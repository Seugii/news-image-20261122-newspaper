#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261122.

Writes the pre-rendered front page to the output directory.
Standard library only: the grader runs Python 3.13 with no third-party modules.
"""
import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        sys.stderr.write("entry.png not found next to main.py\n")
        return 1
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
