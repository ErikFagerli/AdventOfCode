
import re

sum = 0

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

sum_2 = 0

with open("text_file.txt") as f:
    for line in f:
        new_lst = []
        new_line = line.strip()
        for idx in range(1,len(line)):
            if line[:idx][-1].isdigit():
                new_lst.append(line[:idx][-1])
                break
            elif "one" in line[:idx]:
                new_lst.append("1")
                break
            elif "two" in line[:idx]:
                new_lst.append("2")
                break
            elif "three" in line[:idx]:
                new_lst.append("3")
                break
            elif "four" in line[:idx]:
                new_lst.append("4")
                break
            elif "five" in line[:idx]:
                new_lst.append("5")
                break
            elif "six" in line[:idx]:
                new_lst.append("6")
                break
            elif "seven" in line[:idx]:
                new_lst.append("7")
                break
            elif "eight" in line[:idx]:
                new_lst.append("8")
                break
            elif "nine" in line[:idx]:
                new_lst.append("9")
                break
        for idx in range(len(new_line)-1,-1,-1):
            if new_line[idx].isdigit():
                new_lst.append(new_line[idx])
                break
            elif "one" in new_line[idx:]:
                new_lst.append("1")
                break
            elif "two" in new_line[idx:]:
                new_lst.append("2")
                break
            elif "three" in new_line[idx:]:
                new_lst.append("3")
                break
            elif "four" in new_line[idx:]:
                new_lst.append("4")
                break
            elif "five" in new_line[idx:]:
                new_lst.append("5")
                break
            elif "six" in new_line[idx:]:
                new_lst.append("6")
                break
            elif "seven" in new_line[idx:]:
                new_lst.append("7")
                break
            elif "eight" in new_line[idx:]:
                new_lst.append("8")
                break
            elif "nine" in new_line[idx:]:
                new_lst.append("9")
                break
        print(new_lst)
        sum_2 += int("".join(new_lst))
print(sum_2)
