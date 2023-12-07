
time, distance = open("text_file.txt").read().split("\n")

time = list(map(int, time.split(":")[1].strip().split()))
distance = list(map(int, distance.split(":")[1].strip().split()))

different_options = []
for max_time, record_distance in zip(time, distance):
    count = 0
    for charge_time in range(max_time):
        remaining_time = max_time - charge_time
        distance_travelled = charge_time * remaining_time
        if distance_travelled > record_distance:
            count += 1
    different_options.append(count)
print(different_options)

sum = 1

for num in different_options:
    sum *= num
print(sum)

