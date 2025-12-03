
def is_invalid(num):
    s = str(num)
    n = len(s)

    for i in range(1, n//2+1):
        if n%i == 0:
            repeat_count = n//i
            if repeat_count >= 2 and s[:i] * repeat_count == s:
                    return True
    return False

def solution(input_text):
    total = 0
    id_ranges = input_text.split(',')
    for id_range in id_ranges:
        start, end = map(int, id_range.split('-'))
        for num in range(start, end+1):
            if is_invalid(num):
                total += num
    return total


if __name__ == "__main__":
    with open("2025/day2/input.txt", 'r') as f:
        inputs = f.read()
    
    print(solution(inputs))