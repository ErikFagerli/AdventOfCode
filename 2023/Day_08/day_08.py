
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
num_Z = 0

# Find all keys that end with "A"
next_keys = []
for keys in nodes:
    if keys.endswith("A"):
        next_keys.append(keys)

# Access all the values of the keys that end with "A"

while num_Z != len(next_keys):
    for direction in instructions:
        # Access all the values of the keys that end with "A"
        values = [nodes[keys] for keys in next_keys]

        if direction == "L":
            next_keys = [value[0] for value in values]
            count += 1
        else:
            next_keys = [value[1] for value in values]
            count += 1
        num_Z = [key[-1] for key in next_keys].count("Z")
        if num_Z == len(next_keys):
            print("All keys end with Z")
            break    
print(count)

