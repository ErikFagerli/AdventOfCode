max_number_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

sum_game = 0

def convert_to_dict(lst):
    new_dict = {}
    for j in range(0, len(lst), 2):
        new_dict[lst[j+1]] = int(lst[j])
    return new_dict

with open("text_file.txt", "r") as f:
    for line in f:
        line = line.strip()
        game, set = line.split(":")
        id = int(game.split()[-1])
        set = set.split(";")

        for i in range(len(set)):
            set[i] = set[i].strip()
            set[i] = set[i].replace(",", "")
            set[i] = set[i].split(" ")

        invalid_draw = False
        for draw in set:
            #print(draw)
            dict = convert_to_dict(draw)
            print(dict)
            for color in dict.keys():
                if dict[color] > max_number_cubes[color]:
                    print("Game", id, "is invalid")
                    invalid_draw = True
                    break
            if invalid_draw:
                break
        if not invalid_draw:
            print("Game", id, "is valid")
            sum_game += id
            

print(sum_game)

# Part 2    
sum_power = 0

with open("text_file.txt", "r") as f:
    for line in f:
        line = line.strip()
        game, set = line.split(":")
        id = int(game.split()[-1])
        set = set.split(";")

        new_dict = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for i in range(len(set)):
            set[i] = set[i].strip()
            set[i] = set[i].replace(",", "")
            set[i] = set[i].split(" ")

        invalid_draw = False
        sum = 1
        for draw in set:
            #print(draw)
            dict = convert_to_dict(draw)
            for color in dict.keys():
                if dict[color] > new_dict[color]:
                    new_dict[color] = dict[color]
        print(new_dict)
        for color in new_dict.keys():
            sum *= new_dict[color]
        sum_power += sum

print(sum_power)
