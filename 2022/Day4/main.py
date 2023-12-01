
with open("text.txt", "r") as f:
    text_file = f.read()
    pair = text_file.split()

score = 0

for i in range(len(pair)):
    pair1 = pair[i].replace("-", " ")
    pair2 = pair1.replace(",", " ")
    pair3 = pair2.split(" ")
    range1 = list(range(int(pair3[0]), int(pair3[1])+1))
    range2 = list(range(int(pair3[2]), int(pair3[3])+1))

    # if set(range1).issubset(range2) or set(range2).issubset(range1):
    #     score += 1
    if set(range1).intersection(range2) or set(range2).intersection(range1):
        score += 1

print(score)