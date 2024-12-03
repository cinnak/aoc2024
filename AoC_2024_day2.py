from aocd import get_data

def is_monotonic(nums: list[int]) -> bool:
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))

def check_difference(levels):
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])  # Calculate the absolute difference
        if diff < 1 or diff > 3:  # Check if the difference is outside the valid range
            return False  # If any difference is invalid, return False
    return True  # If all differences are valid, return True



if __name__ == "__main__":
    data = get_data(day=2, year=2024)
    inp = data.splitlines()
    result = 0
    for line in inp:
        if is_monotonic(line) and check_difference(line):
            result += 1
    print(result)
    
