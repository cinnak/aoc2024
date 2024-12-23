from aocd import get_data
from dataclasses import dataclass
from typing import List, Tuple, Iterator
from functools import partial
from itertools import product
import time

@dataclass(frozen=True)
class Point:
    """表示矩阵中的一个点"""
    row: int
    col: int

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.row + other.row, self.col + other.col)

    def get_value(self, matrix: List[List[str]]) -> str:
        """获取点在矩阵中的值，如果点不在矩阵范围内返回空字符串"""
        if not (0 <= self.row < len(matrix) and 0 <= self.col < len(matrix[0])):
            return ''
        return matrix[self.row][self.col]

class Matrix:
    """矩阵类，包含所有矩阵操作"""
    def __init__(self, data: List[List[str]]):
        if not data or not data[0]:
            raise ValueError("矩阵不能为空")
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("矩阵必须是规则的（所有行长度相同）")
        self.data = data
        self.height = len(data)
        self.width = len(data[0])

    def is_valid_point(self, point: Point) -> bool:
        """检查点是否在矩阵范围内"""
        return 0 <= point.row < self.height and 0 <= point.col < self.width

    def get_word(self, center: Point, offsets: List[Point]) -> str:
        """获取给定中心点和偏移量列表对应的单词"""
        return ''.join(
            (center + offset).get_value(self.data)
            for offset in offsets
        )

    def iter_points(self) -> Iterator[Point]:
        """生成所有可能的点（跳过边缘）"""
        return (
            Point(row, col)
            for row, col in product(
                range(1, self.height - 1),
                range(1, self.width - 1)
            )
        )

class XMASFinder:
    """XMAS图案查找器"""
    VALID_WORDS = frozenset({"MAS", "SAM"})
    CENTER_CHAR = 'A'
    
    # 定义两条对角线的偏移量
    DIAGONALS = [
        [Point(i, i) for i in range(-1, 2)],     # 左上到右下
        [Point(i, -i) for i in range(-1, 2)]     # 右上到左下
    ]

    def __init__(self, matrix: Matrix):
        self.matrix = matrix

    def is_valid_center(self, point: Point) -> bool:
        """检查点是否是有效的中心点"""
        return (point.get_value(self.matrix.data) == self.CENTER_CHAR and
                all(self.matrix.is_valid_point(point + offset)
                    for diagonal in self.DIAGONALS
                    for offset in diagonal))

    def check_point(self, point: Point) -> bool:
        """检查一个点是否形成XMAS图案"""
        if not self.is_valid_center(point):
            return False

        return all(
            self.matrix.get_word(point, diagonal) in self.VALID_WORDS
            for diagonal in self.DIAGONALS
        )

    def count_patterns(self) -> Tuple[int, float]:
        """统计所有XMAS图案
        返回：(找到的图案数量, 执行时间)
        """
        start_time = time.time()
        count = sum(map(self.check_point, self.matrix.iter_points()))
        return count, time.time() - start_time

def run_tests() -> None:
    """运行测试用例"""
    test_cases = [
        # 测试用例1：标准X-MAS
        [
            ["M", "X", "M"],
            ["S", "A", "S"],
            ["M", "X", "M"]
        ],
    ]
    
    for i, test_matrix in enumerate(test_cases, 1):
        try:
            matrix = Matrix(test_matrix)
            finder = XMASFinder(matrix)
            count, time_taken = finder.count_patterns()
            print(f"测试用例 {i}: 找到 {count} 个图案 (耗时 {time_taken:.4f}秒)")
        except ValueError as e:
            print(f"测试用例 {i} 失败: {e}")

if __name__ == "__main__":
    # 运行测试
    print("运行测试用例...")
    run_tests()
    
    # 处理实际数据
    print("\n处理实际数据...")
    try:
        data = get_data(year=2024, day=4)
        matrix = Matrix([list(line) for line in data.splitlines()])
        finder = XMASFinder(matrix)
        count, time_taken = finder.count_patterns()
        print(f"找到 {count} 个X-MAS图案 (耗时 {time_taken:.4f}秒)")
    except ValueError as e:
        print(f"错误: {e}")
