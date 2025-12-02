def solution(inputs: list):
    pos = 50
    count = 0
    for rot in inputs:
        if 'R' in rot:
            pos = (pos + int(rot.split('R')[-1]))%100
        elif 'L' in rot:
            pos = (pos - int(rot.split('L')[-1]))%100

        if pos == 0:
            count += 1

    print(count)


if __name__ == "__main__":
    with open('2025/day1/input.txt', 'r') as f:
        inputs = f.readlines()
    
    solution(inputs)