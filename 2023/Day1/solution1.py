create_number = lambda first, second : first*10 + second

# words = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f", "treb7uchet"]
words = []
with open("inp2.txt",'r') as cal_doc:
    for word in cal_doc.readlines():
        words.append(word.strip())

sum = 0
zero_ascii = ord('0')
nine_ascii = ord('9')

for word in words:
    digits = []
    for char in word:
        if ord(char) in range(zero_ascii, nine_ascii+1):
            digits.append(ord(char) - zero_ascii)
    number = create_number(digits[0], digits[-1])
    sum += number
print(sum)