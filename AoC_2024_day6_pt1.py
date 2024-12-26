from aocd import get_data

def find_start_position(grid):
    """找到警卫的起始位置和方向"""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '^':
                return i, j, 0  # 0: 上, 1: 右, 2: 下, 3: 左

def get_next_position(x, y, direction):
    """根据方向获取下一个位置"""
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 上右下左
    dx, dy = moves[direction]
    return x + dx, y + dy

def is_valid_position(x, y, grid):
    """检查位置是否在地图范围内"""
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def simulate_guard_movement(grid):
    # 找到起始位置和方向
    x, y, direction = find_start_position(grid)
    visited = set([(x, y)])  # 记录访问过的位置
    
    while True:
        # 获取前方位置
        next_x, next_y = get_next_position(x, y, direction)
        
        # 检查是否离开地图
        if not is_valid_position(next_x, next_y, grid):
            break
            
        # 检查前方是否有障碍物
        if grid[next_x][next_y] == '#':
            # 向右转90度
            direction = (direction + 1) % 4
        else:
            # 向前移动
            x, y = next_x, next_y
            visited.add((x, y))
    
    return len(visited)

if __name__ == "__main__":
    data = get_data(year=2024, day=6)
    grid = [list(row) for row in data.split('\n')]
    result = simulate_guard_movement(grid)
    print(f"The guard visited {result} distinct positions")