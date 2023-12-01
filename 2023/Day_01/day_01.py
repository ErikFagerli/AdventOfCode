
import re

sum = 0

def convert_to_numbers(s):
   
    words_to_numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
    pattern = re.compile(r'\b(' + '|'.join(words_to_numbers.keys()) + r')\b')
    return re.sub(pattern, lambda x: words_to_numbers[x.group()], s)

# Part 1
with open("text_file.txt") as f:
    for line in f:
        lst = []
        for char in line:
            if char.isdigit():
                lst.append(char)
        first_and_last_digit = int(lst[0] + lst[-1])
        sum += first_and_last_digit
print(sum)

# Part 2


with open("example.txt") as f:
    for line in f:
        lst = []
        print(convert_to_numbers(line))