
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

# a and b are each of the list that need to be compared
for i, (a, b) in enumerate(x):
    # check if first list is smaller than second list, if so add index + 1 to total. eval() converst the string format to int format "[1, 2, 3]" -> [1, 2, 3]  
    if f(eval(a), eval(b)) < 0:
        t += i + 1
    
print(t)
