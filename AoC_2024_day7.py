from aocd import get_data
from functools import lru_cache
from typing import Dict, List

def data_process() -> Dict[int, List[int]]:
    data = get_data(year=2024, day=7)
    return {
        int(line.split(":")[0].strip()): list(map(int, line.split(":")[1].strip().split()))
        for line in data.splitlines()
    }


def recursive_circuits(index: int, target: int, numbers: tuple, current_result: int) -> bool:
    # 如果当前结果等于目标，直接返回 True
    if not current_result:
        current_result=numbers[0]
    # 如果索引超出范围，返回 False
    if index == len(numbers):
        return current_result == target
    
    # 递归调用，分别考虑加法和乘法
    return (recursive_circuits(index + 1, target, numbers, current_result + numbers[index]) or
            recursive_circuits(index + 1, target, numbers, current_result * numbers[index]))

def part1(data: Dict[int, List[int]]) -> int:
    result = 0
    for k, v in data.items():
        # 从第一个元素开始，初始结果为 numbers[0]
        if recursive_circuits(1, k, tuple(v),current_result=None):
            result += k
    return result

"""part2"""
def recursive_circuits_pt2(index: int, target: int, numbers: tuple, current_result: None) -> bool:
    # 如果当前结果等于目标，直接返回 True
    if not current_result:
        current_result=numbers[0]
    # 如果索引超出范围，返回 False
    if index == len(numbers):
        return current_result == target
    
    # 递归调用，分别考虑加法和乘法
    return (recursive_circuits_pt2(index + 1, target, numbers, current_result + numbers[index]) or
            recursive_circuits_pt2(index + 1, target, numbers, current_result * numbers[index]) or
            recursive_circuits_pt2(index + 1, target, numbers, current_result *(10**len(str(numbers[index])))+ numbers[index])) 

def part2(data: Dict[int, List[int]]) -> int:
    result = 0
    for k, v in data.items():
        # 从第一个元素开始，初始结果为 numbers[0]
        if recursive_circuits_pt2(1, k, tuple(v),current_result=None):
            result += k
    return result

if __name__ == "__main__":
    data = data_process()
    result_pt1 = part1(data)
    print(f"Part 1: {result_pt1}")

    result_pt2 = part2(data)
    print(f"Part 2: {result_pt2}")