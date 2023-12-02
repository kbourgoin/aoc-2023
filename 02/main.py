import re

SAMPLE_RESULT_ONE = 8
SAMPLE_RESULT_TWO = 2286


def _parse_line(line) -> (int, list):
    # ex: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    game_id, reveals = line.split(": ")
    game_id = int(re.search("Game (?P<id>\\d+)", game_id).group("id"))
    re.search(r"Game (\d+): ((\d+)+ (blue|green|red))", line)

    reveals = reveals.split("; ")
    parsed_reveals = []
    for r in reveals:
        finds = list(re.finditer(r"(?P<count>\d+)+ (?P<color>blue|green|red)", r))
        parsed_reveals.append({f.group("color"): int(f.group("count")) for f in finds})
    return game_id, parsed_reveals


def is_valid(reveal, num_red, num_green, num_blue):
    return (
        reveal.get("red", 0) <= num_red
        and reveal.get("green", 0) <= num_green
        and reveal.get("blue", 0) <= num_blue
    )


def part_one(fname):
    NUM_RED = 12
    NUM_GREEN = 13
    NUM_BLUE = 14

    output = 0
    for line in open(fname):
        id, reveals = _parse_line(line)
        if all(is_valid(r, NUM_RED, NUM_GREEN, NUM_BLUE) for r in reveals):
            output += id
    return output


def _get_power(reveals):
    max_red = 0
    max_green = 0
    max_blue = 0

    for reveal in reveals:
        max_red = max(max_red, reveal.get("red", 0))
        max_green = max(max_green, reveal.get("green", 0))
        max_blue = max(max_blue, reveal.get("blue", 0))

    return max_red * max_green * max_blue


def part_two(fname):
    output = 0
    for line in open(fname):
        _, reveals = _parse_line(line)
        output += _get_power(reveals)
    return output


if __name__ == "__main__":
    if SAMPLE_RESULT_ONE:
        assert part_one("./sample_one.txt") == SAMPLE_RESULT_ONE
        print("Puzzle 1 Validated")
        print(f"Puzzle 1: {part_one('./input.txt')}\n")

    if SAMPLE_RESULT_TWO:
        assert part_two("./sample_two.txt") == SAMPLE_RESULT_TWO
        print("Puzzle 2 Validated")
        print(f"Puzzle 2: {part_two('./input.txt')}")
