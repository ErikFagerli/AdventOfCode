
row = [list(map(int,row.split())) for row in open('text_file.txt').read().split('\n')]


# Find difference between value i, and value i+1 in each row
def find_diff(row, storage=None):
    if storage is None:
        storage = []
    diffs = [row[i+1] - row[i] for i in range(len(row)-1)]
    storage.append(row[-1])
    # Check if every difference is the same
    if len(set(diffs)) == 1:
        storage.append(diffs[-1])
        return storage
    else:
        return find_diff(diffs, storage)
    
# sum_values = 0
# for r in row:
#     lst = find_diff(r)
#     sum_values += sum(lst)
# print(sum_values)

# Part 2
def find_diff2(row, storage=None):
    if storage is None:
        storage = []
    diffs = [row[i+1] - row[i] for i in range(len(row)-1)]
    storage.append(row[0])
    # Check if every difference is the same
    if len(set(diffs)) == 1:
        storage.append(diffs[0])
        storage.append(0)
        return storage
    else:
        return find_diff2(diffs, storage)
sum_value2 = 0
for r in row:
    lst = find_diff2(r)
    for i in reversed(range(1, len(lst))):
        lst[i-1] = lst[i-1] - lst[i]
    sum_value2 += lst[0]

print(sum_value2)