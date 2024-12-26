from collections import defaultdict
from aocd import get_data

def parse_input():
    data = get_data(year=2024, day=8)
    antennas = defaultdict(list)
    for y, row in enumerate(data.splitlines()):
        for x, c in enumerate(row):
            if c != '.':
                antennas[c].append((x, y))
    return antennas

def calculate_antinodes(antennas):
    antinodes = set()
    for frequency, locations in antennas.items():
        n = len(locations)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = locations[i]
                x2, y2 = locations[j]

                # 使用向量方法计算反节点
                x_a1 = 2 * x1 - x2
                y_a1 = 2 * y1 - y2
                x_a2 = 2 * x2 - x1
                y_a2 = 2 * y2 - y1

                antinodes.add((x_a1, y_a1))
                antinodes.add((x_a2, y_a2))

    return antinodes

def filter_antinodes(antinodes, width, height):
    filtered_antinodes = set()
    for x, y in antinodes:
        if 0 <= x < width and 0 <= y < height:
            filtered_antinodes.add((x, y))
    return filtered_antinodes

def count_unique_antinodes():
    antennas = parse_input()
    width = max(x for locs in antennas.values() for x, _ in locs) + 1
    height = max(y for locs in antennas.values() for _, y in locs) + 1

    antinodes = calculate_antinodes(antennas)
    filtered_antinodes = filter_antinodes(antinodes, width, height)

    return len(filtered_antinodes)

def test_with_example():
    example_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    antennas = defaultdict(list)
    for y, row in enumerate(example_input.splitlines()):
        for x, c in enumerate(row):
            if c != '.':
                antennas[c].append((x, y))
    width = len(example_input.splitlines()[0])
    height = len(example_input.splitlines())
    antinodes = calculate_antinodes(antennas)
    filtered_antinodes = filter_antinodes(antinodes, width, height)
    print("Example Test Result:",len(filtered_antinodes))
    assert len(filtered_antinodes) == 14, f"Expected 14, got {len(filtered_antinodes)}"
test_with_example()

if __name__ == "__main__":
    result = count_unique_antinodes()
    print(result)