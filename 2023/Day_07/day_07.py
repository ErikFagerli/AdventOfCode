
player = [line.strip().split(" ") for line in open("text_file.txt").readlines()]

value_order = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

result = []
for hand, bet in player:
    count = {}
    score = 0
    for char in hand:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for value in count.values():
        score += value ** 2
    
    result.append([hand, bet, score])

result.sort(key=lambda x: x[2])

for i in range(0,len(result) - 1):
    for j in range(len(result) - 1):
        if result[j][2] == result[j+1][2]:
            for char1, char2 in zip(result[j][0], result[j+1][0]):
                if value_order[char1] == value_order[char2]:
                    continue
                elif value_order[char1] > value_order[char2]:
                    #print(f"Swapping {result[j]} with {result[j+1]}")
                    temp = result[j]
                    result[j] = result[j+1]  
                    result[j+1] = temp
                    break
                else:
                    break

tot_score = 0

for i in range(1, len(result) + 1):
    tot_score += i * int(result[i-1][1])
print(tot_score)