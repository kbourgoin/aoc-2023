import os
import re

from collections import defaultdict

__here__ = os.path.abspath(__file__).rsplit("/", 1)[0]

SAMPLE_RESULT_ONE = 13
SAMPLE_RESULT_TWO = 30


def _parse_card(card):
    parsed = re.match(
        r"Card\s+(?P<id>\d+): (?P<winners>[^|]+) \| (?P<numbers>[^$]+)", card
    ).groupdict()
    parsed["id"] = int(parsed["id"])
    parsed["winners"] = set(int(w) for w in re.findall(r"\d+", parsed["winners"]))
    parsed["numbers"] = set(int(n) for n in re.findall(r"\d+", parsed["numbers"]))
    return parsed


def _parse_cards(fname):
    with open(fname) as f:
        for line in f.readlines():
            yield _parse_card(line.strip())


def part_one(fname):
    output = 0
    cards = list(_parse_cards(fname))
    for card in cards:
        # print(f"Winners: ({len(winners & numbers)}) {winners & numbers}")
        score = len(card["winners"] & card["numbers"])
        if score > 0:
            output += 2 ** (score - 1)

    return output


def part_two(fname):
    count = 0
    cards = list(_parse_cards(fname))

    # reverse the cards and resolve in that order, memoizing the result for each card
    results = {}  # id : cards generated
    cards = cards[::-1]

    for card in cards:
        score = len(card["winners"] & card["numbers"])
        results[card["id"]] = score
        if score == 0:
            continue  # no need to keep going

        for i in range(1, score + 1):
            results[card["id"]] += results[card["id"] + i]

    return sum(v for v in results.values()) + len(cards)


if __name__ == "__main__":
    if SAMPLE_RESULT_ONE:
        assert part_one(os.path.join(__here__, "sample_one.txt")) == SAMPLE_RESULT_ONE
        print("Puzzle 1 Validated")
        print(f"Puzzle 1: {part_one(os.path.join(__here__, './input.txt'))}\n")

    if SAMPLE_RESULT_TWO:
        assert part_two(os.path.join(__here__, "./sample_two.txt")) == SAMPLE_RESULT_TWO
        print("Puzzle 2 Validated")
        print(f"Puzzle 2: {part_two(os.path.join(__here__, './input.txt'))}")
