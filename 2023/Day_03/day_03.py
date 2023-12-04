symbols = set(r"""`~!@\#$%^&*()_-+={[}}|\:;"'<,>?/""")
print(symbols)

array = []

sum = 0

def convert_to_array(string):
    return [char for char in string]

#Part 1

with open("example.txt", "r") as f:
        for line in f:
            line = line.strip()
            line = convert_to_array(line)
            array.append(line)

        digit = ""
        idx = []
        idx_temp = []
        next_to_symbol = False
        for i in range(len(array)):
            for j in range(len(line)):
                legal_moves = [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j+1), (i+1,j+1), (i+1,j), 
                               (i+1,j-1), (i,j-1)]
                if array[i][j] is ".":
                    if next_to_symbol:
                        print(digit, idx_temp)
                        sum += int(digit)
                        idx.append(idx_temp)
                    digit = ""
                    idx_temp = []
                    next_to_symbol = False
                    continue
                elif array[i][j] in symbols:
                    if next_to_symbol:
                        print(digit, idx_temp)
                        sum += int(digit)
                        idx.append(idx_temp)
                    digit = ""
                    idx_temp = []
                    next_to_symbol = False
                    continue
                elif array[i][j].isdigit():
                    digit += array[i][j]
                    idx_temp.append((i,j))
                    legal_moves = [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j+1), (i+1,j+1), (i+1,j), 
                               (i+1,j-1), (i,j-1)]
                    for move in legal_moves:
                        if move[0] < 0 or move[1] < 0 or move[0] > len(array)-1 or move[1] > len(line)-1:
                            continue
                        elif array[move[0]][move[1]] is ".":
                            continue
                        elif array[move[0]][move[1]].isdigit():
                            continue
                        else:
                            next_to_symbol = True
print(sum)

#Part 2