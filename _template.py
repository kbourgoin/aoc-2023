import os

__here__ = os.path.abspath(__file__).rsplit("/", 1)[0]

SAMPLE_RESULT_ONE = None
SAMPLE_RESULT_TWO = None


def part_one(fname):
    pass


def part_two(fname):
    pass


if __name__ == "__main__":
    if SAMPLE_RESULT_ONE:
        assert part_one(os.path.join(__here__, "sample_one.txt")) == SAMPLE_RESULT_ONE
        print("Puzzle 1 Validated")
        print(f"Puzzle 1: {part_one(os.path.join(__here__, './input.txt'))}\n")

    if SAMPLE_RESULT_TWO:
        assert part_two(os.path.join(__here__, "./sample_two.txt")) == SAMPLE_RESULT_TWO
        print("Puzzle 2 Validated")
        print(f"Puzzle 2: {part_two(os.path.join(__here__, './input.txt'))}")
