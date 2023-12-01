# Open the file in read mode
with open('file.txt', 'r') as f:
    # Read the file as a single string
    text = f.read()

# Iterate over the string in blocks of 4 characters
# starting from the beginning of the string
for i in range(len(text) - 14):
    # Get the four-letter block at the current position
    block = text[i:i+14]

    # Check if all four letters in the block are unique
    if len(set(block)) == 14:
        # If so, print the index of the last letter in the block
        # and stop the loop
        print(i + 13 + 1)
        break