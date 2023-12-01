import re


row1 = ["B", "G", "S", "C"]
row2 = ["T", "M", "W", "H", "J", "N", "V", "G"]
row3 = ["M", "Q", "S"]
row4 = ["B", "S", "L", "T", "W", "N", "M"]
row5 = ["J", "Z", "F", "T", "V", "G", "W", "P"]
row6 = ["C", "T", "B", "G", "Q", "H", "S"]
row7 = ["T", "J", "P", "B", "W"]
row8 = ["G", "D", "C", "Z", "F", "T", "Q", "M"]
row9 = ["N", "S", "H", "B", "P", "F"]

crates = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

with open("text.txt", "r") as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip() == "":
            for x in range(i+1, len(lines)):
                lst = re.findall(r"\d+", lines[x])

                amountCrates = lst[0]
                rowFrom = lst[1]
                rowTo = lst[2]

                cratesTaken = crates[int(rowFrom)-1][-int(amountCrates):]
                # cratesTaken.reverse()
                for crate in cratesTaken:
                    crates[int(rowTo)-1].append(crate)
                del crates[int(rowFrom)-1][-int(amountCrates):]
            break

    text = []
    for crate in crates:
        text.append(crate[-1])
    string_text ="".join(text)
    print(string_text)
