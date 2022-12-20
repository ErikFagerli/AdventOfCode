
def create_lst(textfile):
    lst = []
    with open(textfile, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = int(line)
            lst.append(line)
    return lst

encrypted = create_lst("text.txt")
#encrypted = [1, 2, -3, 3, -2, 0, 4]
encrypted = [(int(x), i) for i, x in enumerate(encrypted)]
mixed = encrypted.copy()  # copy the encrypted file to a new list for mixing

# mix the file
print(mixed)
for x in mixed:
    if x != 0 or True:
        old_idx = encrypted.index(x)
        new_idx = (old_idx + x[0]) % (len(encrypted) - 1)
        encrypted.pop(old_idx) 
        encrypted.insert(len(encrypted) if new_idx == 0 else new_idx, x)
    # print(mixed)

print(encrypted)
start_number = 0
start_index = [i for i in range(len(encrypted)) if encrypted[i][0] == 0]
counter = start_index[0]
value = 0
while counter < start_index[0] + 3000:
    counter += 1
    index = counter % len(encrypted)
    if counter == (start_index[0] + 1000) or counter == (start_index[0] + 2000) or counter == (start_index[0] + 3000):
        print(f"Counter: {counter}, Number: {encrypted[index][0]}")
        value += encrypted[index][0]
    
print(value)
