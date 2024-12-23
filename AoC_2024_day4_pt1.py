from aocd import get_data
from dataclasses import dataclass
from functools import lru_cache
from typing import Iterator, List, Tuple

@dataclass(frozen=True)
class Position:
    row: int
    col: int

@dataclass(frozen=True)
class Direction:
    dx: int
    dy: int

# 定义常量
TARGET = "XMAS"
TARGET_LEN = len(TARGET)

# 8个方向定义为Direction对象
DIRECTIONS = [
    Direction(0, 1),   # 右
    Direction(1, 1),   # 右下
    Direction(1, 0),   # 下
    Direction(1, -1),  # 左下
    Direction(0, -1),  # 左
    Direction(-1, -1), # 左上
    Direction(-1, 0),  # 上
    Direction(-1, 1)   # 右上
]

def is_valid(pos: Position, direction: Direction) -> bool:
    """检查给定位置和方向是否在矩阵范围内"""
    end_row = pos.row + direction.dx * (TARGET_LEN - 1)
    end_col = pos.col + direction.dy * (TARGET_LEN - 1)
    return (0 <= pos.row < len(matrix) and 
            0 <= pos.col < len(matrix[0]) and
            0 <= end_row < len(matrix) and 
            0 <= end_col < len(matrix[0]))

@lru_cache(maxsize=None)
def get_word(pos: Position, direction: Direction) -> str:
    """获取指定位置和方向上的单词"""
    return ''.join(
        matrix[pos.row + direction.dx * i][pos.col + direction.dy * i]
        for i in range(TARGET_LEN)
    )

def find_possible_positions() -> Iterator[Tuple[Position, Direction]]:
    """生成矩阵中所有可能的位置和方向组合"""
    height, width = len(matrix), len(matrix[0])
    for row in range(height):
        for col in range(width):
            pos = Position(row, col)
            for direction in DIRECTIONS:
                if is_valid(pos, direction):
                    yield pos, direction

def find_all_xmas() -> int:
    """在矩阵中查找所有'XMAS'出现的次数"""
    return sum(
        get_word(pos, direction) == TARGET
        for pos, direction in find_possible_positions()
    )

if __name__ == "__main__":
    data = get_data(year=2024, day=4)
    matrix = [list(line) for line in data.splitlines()]
    print(find_all_xmas())
