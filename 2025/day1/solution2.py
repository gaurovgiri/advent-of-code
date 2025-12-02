def solution(inputs: list):
    curr = prev = 50
    count = 0
    for rot in inputs:
        if 'R' in rot:
            curr +=  int(rot.split('R')[-1])
            for i in range(prev, curr):
                if i % 100 == 0:
                    count += 1

        elif 'L' in rot:
            curr -= int(rot.split('L')[-1])
            for i in range(prev, curr, -1):
                if i % 100 == 0:
                    count += 1

        curr %= 100
        prev = curr
        

    print(count)


if __name__ == "__main__":
    with open('2025/day1/input.txt', 'r') as f:
        inputs = f.readlines()
    
    solution(inputs)