win = 6
draw = 3
lose = 0

X = 1
Y = 2
Z = 3

lst_strategy = ["A X", "A Y", "A Z", "B X", "B Y", "B Z", "C X", "C Y", "C Z"]
lst_score =     [3,     4,      8,     1,     5,     9,     2,     6,     7]

score = 0
with open("strategy.txt", "r") as f:
    file = f.read()
    game = file.split("\n")
    print(game)
    for i in range(len(game)):
        index_lst = lst_strategy.index(game[i])
        score = score + lst_score[index_lst]

print(score)