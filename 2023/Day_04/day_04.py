
with open("text_file.txt") as f:
    score = 0
    lst = []
    for line in f:
        n = 0
        line = line.strip()
        card_id, ticket = line.split(":")
        winning_nr, your_nr = ticket.strip().split("|")
        winning_nr = winning_nr.split()
        your_nr = your_nr.split()
        for idx, nr in enumerate(winning_nr):
            for nr2 in your_nr:
                if nr == nr2:
                    n += 1
                    break
        if n == 0:
            points = 0
        else:
            points = 2 ** (n - 1)
        lst.append([card_id.split()[-1], n, 1])
        score += points
        # print(lst)
    for idx, card in enumerate(lst):
        for i in range(1, card[1]+1):
            lst[idx + i][2] += card[2]

sum = 0
for card in lst:
    sum += card[2]
print(sum)
# print(score)
# print(lst)