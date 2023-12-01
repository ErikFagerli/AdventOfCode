
tasks = []
iteration = 1
signal_strength = []
search_signal = [i for i in range(20, 221, 40)]
value = 1

with open("text.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    task = line.split()
    tasks.append(task)


for command in tasks:
    if command[0] == "addx":
        for i in range(2):
            iteration += 1
            if i == 1:
                value += int(command[1])
            if iteration in search_signal:
                signal_strength.append(value * iteration)
        
    else:
        iteration += 1
        if iteration in search_signal:
                signal_strength.append(value * iteration)

print(sum(signal_strength))