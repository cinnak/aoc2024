from aocd import get_data

def is_monotonic(line):
    asd = all(line[i]<=line[i+1] for i in range(len(line)-1))
    dsd = all(line[i]>=line[i+1] for i in range(len(line)-1))
    return asd or dsd

def check_diff(line):
    return all((abs(line[i]-line[i+1])>=1 and abs(line[i]-line[i+1])<=3) for i in range(len(line)-1))

def is_safe(line):
    safe = is_monotonic(line) and check_diff(line)
    return 1 if safe else 0

def pt2(not_safe_pt1):
    result = 0
    for line in not_safe_pt1:
        found_valid = False
        for i in range(len(line)):
            removed = line[:i] + line[i+1:]
            if is_safe(removed):
                found_valid = True
                break
        if found_valid:
            result += 1
    return result
    
def pt2_alt(not_safe_pt1):
    result = sum(1 for line in not_safe_pt1 if any(is_safe(line[:i] + line[i+1:]) for i in range(len(line))))
    return result

if __name__ == "__main__":
    data = get_data(year=2024,day=2)
    inp = [[int(y) for y in x.split(' ')] for x in data.splitlines()]
    # part 1
    result_pt1 = sum(is_safe(line) for line in inp)
    print(f"Part 1: {result_pt1}")

    # part 2
    not_safe_pt1 = [line for line in inp if is_safe(line)==0]
    result_pt2 = pt2(not_safe_pt1)
    print(f"Part 2: {result_pt1+result_pt2}")
    
