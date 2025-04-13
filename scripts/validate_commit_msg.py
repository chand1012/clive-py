#!/usr/bin/env python3
import re
import sys

PATTERN = r"^(feat|fix|docs|style|refactor|test|chore)(\([\w\-]+\))?: .+"


def main():
    commit_msg_file = sys.argv[1]
    with open(commit_msg_file, "r") as f:
        first_line = f.readline().strip()

    if not re.match(PATTERN, first_line):
        print(
            "❌ Invalid commit message. Use Conventional Commits (e.g., feat: add feature)"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
