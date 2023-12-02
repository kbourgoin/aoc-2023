import re

SAMPLE_RESULT_ONE = 142
SAMPLE_RESULT_TWO = 281 + 72


def part_one(fname):
    result = 0
    for line in open(fname):
        matches = list(re.finditer(r"\d", line))
        num = int(f"{matches[0].group()}{matches[-1].group()}")
        result += num
    return result


WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def _resolve(word):
    if word in WORDS:
        return WORDS[word]
    else:
        return int(word)


def part_two(fname):
    result = 0
    for line in open(fname):
        first = re.search(r"(\d|one|two|three|four|five|six|seven|eight|nine)", line)
        first = _resolve(first.group())

        last = None
        for i in range(1, len(line) + 1):
            last = re.search(
                r"(\d|one|two|three|four|five|six|seven|eight|nine)", line[-i:]
            )
            if last:
                last = _resolve(last.group())
                break

        num = f"{first}{last}"
        print(f"{num}: {line.strip()}")
        result += int(num)
    return result


if __name__ == "__main__":
    if SAMPLE_RESULT_ONE:
        assert part_one("./sample_one.txt") == SAMPLE_RESULT_ONE
        print("Puzzle 1 Validated")
        print(f"Puzzle 1: {part_one('./input.txt')}\n")

    if SAMPLE_RESULT_TWO:
        assert part_two("./sample_two.txt") == SAMPLE_RESULT_TWO
        print("Puzzle 2 Validated")
        print(f"Puzzle 2: {part_two('./input.txt')}")
