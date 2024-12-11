from aocd import get_data
import re

def pt1(data):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, data)
    result = 0
    for m in matches:
        mul = int(m[0])*int(m[1])
        result += mul
    return result



class MulInstructionProcessor:
    def __init__(self):
        # 初始状态，默认启用指令
        self.mul_enabled = True
        self.results = []
    
    def process_text(self,text):
        matches = re.finditer(r'(do\(\))|(don\'t\(\))|mul\((\d+),(\d+)\)',text)

        for m in matches:
            full_match = m.group(0)
            # 处理do()指令
            if full_match == 'do()':
                self.mul_enabled = True

            # 处理don't()指令
            elif full_match == 'don\'t()':
                self.mul_enabled = False

            elif full_match.startswith('mul('):
                if self.mul_enabled:
                    # 提取两个数字并计算乘积
                    num1, num2 = map(int, full_match[4:-1].split(','))
                    self.results.append(num1 * num2)
        
        return sum(self.results)
def pt2(text):
    processor = MulInstructionProcessor()
    return processor.process_text(text)

if __name__=="__main__":
    data = get_data(year=2024,day=3)
    pt1 = pt1(data)
    print(f'part 1: {pt1}')
    pt2 = pt2(data)
    print(f'part 2: {pt2}')


