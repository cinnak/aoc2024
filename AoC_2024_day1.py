from aocd import get_data
from typing import Sequence, Iterator

def parse_numbers(inp: Sequence[str]) -> tuple[list[int], list[int]]:
    left, right = [], []
    for i, line in enumerate(inp):
        try:
            lf, rt = line.split("   ")
            left.append(int(lf))
            right.append(int(rt))
        except ValueError:
            raise ValueError(f"Invalid format at line {i}")
    return left, right

def similarity_score(inp: Sequence[str]) -> int:
    if not inp:
        raise ValueError("Input cannot be empty")
    left, right = parse_numbers(inp)
    left.sort()
    right.sort()
    return sum(abs(x - y) for x, y in zip(left, right))
from collections import Counter

def pt2(inp):
    left, right = parse_numbers(inp)
    count_right = dict(list(Counter(right).items()))
    count_left = {}
    count_left.update({x: count_right[x] for x in tuple(left) if count_right.get(x,0)})
    return sum([int(k)*v for k,v in count_left.items()])



if __name__ == "__main__":
    data = get_data(year=2024,day=1)
    inp = data.splitlines()
    result = similarity_score(inp)
    print(f"Part 1: {result}")


    result_pt2 = pt2(inp)
    print(f"Part 2: {result_pt2}")