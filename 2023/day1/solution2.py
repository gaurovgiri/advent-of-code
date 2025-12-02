import re

create_number = lambda first, second : first*10 + second

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


pattern = re.compile(r'(?=(' + '|'.join(digits.keys()) + '|[0-9]))')


words = []
with open("input.txt",'r') as cal_doc:
    for word in cal_doc.readlines():
        words.append(word.strip())

# words = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
sum = 0

for word in words:
    matches = pattern.findall(word)
    match_1 = matches[0]
    match_2 = matches[-1]

    if match_1 in digits:
        first_num = digits[match_1]
    else:
        first_num = ord(match_1) - ord('0')

    if match_2 in digits:
        second_num = digits[match_2]
    else:
        second_num = ord(match_2) - ord('0')
    
    number = create_number(first_num, second_num)

    sum += number

print(sum)