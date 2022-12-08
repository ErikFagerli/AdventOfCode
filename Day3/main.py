import string

letter_lower = list(string.ascii_lowercase)
letter_upper = list(string.ascii_uppercase)

score_lower = [i for i in range(1,27)]
score_upper = [i for i in range(27,53)]

with open("backpack.txt", "r") as f:
    text = f.read()
    lst = text.split("\n")

score = 0
""" Task 1
for i in range(len(lst)):
    backpack = lst[i]
    firstpart, secondpart = backpack[:len(backpack)//2], backpack[len(backpack)//2:]
    for letter in firstpart:
        if letter in secondpart:
            if letter.islower():
                indx_letter = letter_lower.index(letter)
                score = score + score_lower[indx_letter]
                break
            else:
                indx_letter = letter_upper.index(letter)
                score = score + score_upper[indx_letter]
                break
"""

for i in range(2,len(lst),3):
    backpack_1 = lst[i]
    backpack_2 = lst[i-1]
    backpack_3 = lst[i-2]

    for letter in backpack_1:
        if letter in backpack_2 and letter in backpack_3:
            if letter.islower():
                indx_letter = letter_lower.index(letter)
                score = score + score_lower[indx_letter]
                break
            else:
                indx_letter = letter_upper.index(letter)
                score = score + score_upper[indx_letter]
                break




print(score)