v = set([(0, 0)])

# Make rope that is length of 10
R = [[0, 0] for _ in range(10)]

# Loop through each direction and length of direction
for line in open("text.txt"):
    x, y = line.split() # x = direction, y = length
    y = int(y)

    # Loop through each length
    for _ in range(y):
        # Check which direction head is moving
        dx = 1 if x == "R" else -1 if x == "L" else 0
        dy = 1 if x == "U" else -1 if x == "D" else 0

        # Update head position of rope
        R[0][0] += dx
        R[0][1] += dy

        for i in range(9):
            # I use H and T, so that i dont have to change from previouse part
            H = R[i]
            T = R[i + 1]

            _x = H[0] - T[0]
            _y = H[1] - T[1]

            # Check if tail have to move diagonal or up or down and update tails position
            if abs(_x) > 1 or abs(_y) > 1:
                if _x == 0:
                    T[1] += _y // 2
                elif _y == 0:
                    T[0] += _x // 2
                else:
                    T[0] += 1 if _x > 0 else -1
                    T[1] += 1 if _y > 0 else -1

        # Need to add the last value of the rope
        v.add(tuple(R[-1]))

# Check number of positions tail has been to
print(len(v))