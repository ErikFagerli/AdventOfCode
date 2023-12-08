
instructions, *rest = open("text_file.txt").read().split("\n\n")

nodes = {}

for node in rest:
    for line in node.strip().split("\n"):
        # Define the string
        key, value = line.strip().split(" = ")

        # remove parenthesis from value and split by comma
        value = value.strip("()").split(", ")

        # Add key and value to dictionary
        nodes[key] = value
count = 0
key = "AAA"

while key != "ZZZ":
    for direction in instructions:
        if direction == "L":
            next_key = nodes[key][0]
            count += 1
        else:
            next_key = nodes[key][1]
            count += 1

        if next_key == "ZZZ":
            key = next_key
            break
        key = next_key
print(count)

