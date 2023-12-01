
# Create list where each item contains which two nested lists to compare
x = list(map(str.splitlines, open("text.txt").read().strip().split("\n\n")))

# Create function to check compare the two potential nested lists. Recursive function
def f(x, y):
    # Check if the first list is either an list or an int
    if type(x) == int:
        # Check if the second list is either an list or an int
        if type(y) == int:
            # return the difference, interested if it is negative, positive or 0
            return x - y
        # If x is an int, make it into a list and try again
        else:
            return f([x], y)
    # x is an list
    else:
        # Check if y is an int, if it, make it an list and try again
        if type(y) == int:
            return f(x, [y])
    # Both x and y is an list
    for a, b in zip(x, y):
        # Go through the list and check if x and y contains lists. It does so until one x or y is not a list
        v = f(a, b)
        if v:
            return v

    # If all the values in both list are equal, return the difference in length
    return len(x) - len(y)

t = 0

for i, (a, b) in enumerate(x):
    v = f(eval(a), eval(b))
    if v < 0:
        t += i + 1
print(t)

# Part 2
# Create list where each item is a list in text file
x = list(map(eval, open("text.txt").read().split()))


i2 = 1
i6 = 2

# Loop through each list
for a in x:
    # Use the function in part 1 to check if the list is less than the divider packets. 
    # If so add values to i2, and/or i6.
    if f(a, [[2]]) < 0:
        i2 += 1
        i6 += 1
    elif f(a, [[6]]) < 0:
        i6 += 1

print(i2 * i6)
