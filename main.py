"""Texts From Your Future Self -- make.fun bounty entry.

Writes one funny text message from the writer's future self to
/output/entry.txt (UTF-8, under 200 characters). Pure stdlib.
"""

import os

TEXT = (
    "It's you from 2040. Good news: time travel works. "
    "Bad news: I can only send one text: cancel the haircut. "
    "That's the whole message."
)


def main():
    assert 1 <= len(TEXT) <= 200, "entry text must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
