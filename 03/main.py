from pprint import pprint
import os


SAMPLE_RESULT_ONE = 4361
SAMPLE_RESULT_TWO = 467835

__here__ = os.path.abspath(__file__).rsplit("/", 1)[0]


def _is_symbol(ch, ignore_star):
    if ignore_star:
        return not ch.isdigit() and ch != "*" and ch != "."
    else:
        return not ch.isdigit() and ch != "."


def _check_line(pos, line, ignore_star=False):
    # check pos-1, pos, and pos+1 for symbols
    start = max(0, pos - 1)
    end = min(len(line), pos + 1)
    return any(_is_symbol(ch, ignore_star) for ch in line[start : end + 1])


def _makes_valid_number(pos, lines, ignore_star=False):
    x, y = pos
    if y > 0:
        if _check_line(x, lines[y - 1], ignore_star=ignore_star):
            return True
    if y < len(lines) - 1:
        if _check_line(x, lines[y + 1], ignore_star=ignore_star):
            return True
    return _check_line(x, lines[y], ignore_star=ignore_star)


def _extract_numbers(lines):
    curr_num = ""
    curr_num_valid = False

    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch.isdigit():
                curr_num += ch
                curr_num_valid = curr_num_valid or _makes_valid_number((x, y), lines)
            else:
                if curr_num:
                    if curr_num_valid:
                        yield (int(curr_num), len(curr_num), (x - len(curr_num), y))
                    curr_num = ""
                    curr_num_valid = False
        if curr_num:
            if curr_num_valid:
                yield (int(curr_num), len(curr_num), (x - len(curr_num), y))
            curr_num = ""
            curr_num_valid = False


def _find_stars(lines):
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == "*":
                yield (x, y)


def _find_adjacent(pos, numbers):
    # find numbers that are adjacent to pos
    x, y = pos
    for num in numbers:
        num_y = num[2][1]
        points = [(num[2][0] + i, num_y) for i in range(num[1])]
        for point_x, point_y in points:
            if abs(point_x - x) <= 1 and abs(point_y - y) <= 1:
                yield num
                break


def part_one(fname):
    with open(fname) as f:
        lines = [line.strip() for line in f.readlines()]

    numbers = list(_extract_numbers(lines))
    pprint(numbers)

    return sum(n[0] for n in numbers)


def part_two(fname):
    with open(fname) as f:
        lines = [line.strip() for line in f.readlines()]

    output = 0
    numbers = list(_extract_numbers(lines))
    stars = list(_find_stars(lines))
    good_stars = []
    for star in stars:
        adjacent = list(_find_adjacent(star, numbers))
        if len(adjacent) == 2:
            output += adjacent[0][0] * adjacent[1][0]
            print(adjacent)
            good_stars.append(star)

    with open("./out.txt", "w") as f:
        for y, line in enumerate(lines):
            for x, ch in enumerate(line):
                if ch == "*":
                    if (x, y) in good_stars:
                        f.write("*")
                    else:
                        f.write("X")
                else:
                    f.write(ch)
            f.write("\n")

    return output


if __name__ == "__main__":
    if SAMPLE_RESULT_ONE:
        assert part_one(os.path.join(__here__, "sample_one.txt")) == SAMPLE_RESULT_ONE
        print("Puzzle 1 Validated")
        print(f"Puzzle 1: {part_one(os.path.join(__here__, './input.txt'))}\n")

    if SAMPLE_RESULT_TWO:
        assert part_two(os.path.join(__here__, "./sample_two.txt")) == SAMPLE_RESULT_TWO
        print("Puzzle 2 Validated")
        print(f"Puzzle 2: {part_two(os.path.join(__here__, './input.txt'))}")
        # 79687676 is not correct (but maybe not too low)
