
time, distance = open("text_file.txt").read().split("\n")

time = int("".join(list(map(str, time.split(":")[1].split()))))
distance = int("".join(list(map(str, distance.split(":")[1].split()))))

count = 0
for charge_time in range(time):
    remaining_time = time - charge_time
    distance_travelled = charge_time * remaining_time
    if distance_travelled > distance:
        count += 1
print(count)


