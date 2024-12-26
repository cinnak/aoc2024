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

def calculate_antinodes_part1(antennas):
    """计算 Part 1 的反节点"""
    antinodes = set()
    for frequency, locations in antennas.items():
        n = len(locations)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = locations[i]
                x2, y2 = locations[j]

                x_a1 = 2 * x1 - x2
                y_a1 = 2 * y1 - y2
                x_a2 = 2 * x2 - x1
                y_a2 = 2 * y2 - y1

                antinodes.add((x_a1, y_a1))
                antinodes.add((x_a2, y_a2))

    return antinodes

def calculate_antinodes_part2(antennas, width, height):
    """计算 Part 2 的反节点"""
    antinodes = set()
    for frequency, locations in antennas.items():
        n = len(locations)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = locations[i]
                x2, y2 = locations[j]

                # 找到所有共线的点
                dx = x2 - x1
                dy = y2 - y1

                # 如果两个点重合，跳过
                if dx == 0 and dy == 0:
                    continue
                
                # 遍历直线上的所有点
                if dx == 0:  # 垂直线
                    for y in range(0,height):
                        antinodes.add((x1, y))
                elif dy == 0:  # 水平线
                    for x in range(0,width):
                        antinodes.add((x, y1))
                else:  # 斜线
                    for k in range(-max(width,height),max(width,height)):
                        x = x1 + k
                        y = y1 + (dy * k) // dx
                        if (dy * k) % dx == 0:
                            antinodes.add((x, y))
    return antinodes

def filter_antinodes(antinodes, width, height):
    """过滤超出地图边界的反节点"""
    filtered_antinodes = set()
    for x, y in antinodes:
        if 0 <= x < width and 0 <= y < height:
            filtered_antinodes.add((x, y))
    return filtered_antinodes

def count_unique_antinodes(part):
    """计算唯一反节点的数量，根据 part 选择计算方法"""
    antennas = parse_input()
    width = max(x for locs in antennas.values() for x, _ in locs) + 1
    height = max(y for locs in antennas.values() for _, y in locs) + 1

    if part == 1:
        antinodes = calculate_antinodes_part1(antennas)
    elif part == 2:
        antinodes = calculate_antinodes_part2(antennas, width, height)
    else:
        raise ValueError("Invalid part number. Must be 1 or 2.")

    filtered_antinodes = filter_antinodes(antinodes, width, height)
    return len(filtered_antinodes)




if __name__ == "__main__":
    result_part1 = count_unique_antinodes(1)
    print("Part 1:", result_part1)
    result_part2 = count_unique_antinodes(2)
    print("Part 2:", result_part2)