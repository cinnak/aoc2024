from aocd import get_data
from typing import List, Set, Tuple
from dataclasses import dataclass
from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

@dataclass
class Position:
    x: int
    y: int
    
    def move(self, direction: Direction) -> 'Position':
        dx, dy = direction.value
        return Position(self.x + dx, self.y + dy)
    
    def __hash__(self):
        return hash((self.x, self.y))

class GuardSimulator:
    def __init__(self, grid: List[str]):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.start_pos = self._find_start()
        self.direction = Direction.UP  # 初始方向向上
        
    def _find_start(self) -> Position:
        """找到起始位置 (^)"""
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == '^':
                    return Position(x, y)
        raise ValueError("No starting position found")
    
    def is_valid_position(self, pos: Position) -> bool:
        """检查位置是否有效"""
        return (0 <= pos.x < self.width and 
                0 <= pos.y < self.height and 
                self.grid[pos.y][pos.x] != '#')
    
    def detect_loop(self) -> bool:
        """检测是否形成循环"""
        visited_states: Set[Tuple[Position, Direction]] = set()
        current_pos = self.start_pos
        current_dir = self.direction
        
        while True:
            state = (current_pos, current_dir)
            if state in visited_states:
                return True  # 找到循环
            visited_states.add(state)

            next_pos = current_pos.move(current_dir)

            if not self.is_valid_position(next_pos):
                return False
            
            if self.grid[next_pos.y][next_pos.x] == '#':
                current_dir = Direction((current_dir.value[0] + 1) % 4)  # 右转
            else:
                current_pos = next_pos

    def find_all_loop_positions(self) -> Set[Position]:
        """找出所有可以形成循环的位置"""
        loop_positions = set()
        
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == '.':
                    new_grid = [list(row) for row in self.grid]
                    new_grid[y][x] = '#'
                    simulator = GuardSimulator(new_grid)
                    
                    if simulator.detect_loop():
                        loop_positions.add(Position(x, y))
        
        return loop_positions

def solve(input_data: str) -> int:
    grid = input_data.strip().splitlines()
    simulator = GuardSimulator(grid)
    loop_positions = simulator.find_all_loop_positions()
    return len(loop_positions)

if __name__ == "__main__":
    data = get_data(year=2024, day=6)
    result = solve(data)
    print(f"There are {result} positions where an obstruction would create a loop")