# Create set where boulder are going to be in
b = set()

# Depth of abyss
abyss = 0

# Loop that creates every grid spot where boulders are placed
for line in open("text.txt"):
    x =  [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]

    for (x1, y1), (x2, y2) in zip(x, x[1:]):

        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                b.add(x + y * 1j)
                abyss = max(abyss, y + 1)

t = 0

while 500 not in b:
    # Start position of falling sand
    s = 500
    while True:
        # Check if sand falls in abyss. If it falls, all possible locations are filled and we exit loop.
        if s.imag >= abyss:
            break
        # Check if grid spot is not occupied by either sand or boulder.
        # If it is not, update position of sand and check again. 
        if s + 1j not in b:
            s += 1j
            continue
        if s + 1j - 1 not in b:
            s += 1j - 1
            continue
        if s + 1j + 1 not in b:
            s += 1j + 1
            continue
        # If all downwards locations are occupied, the sand comes to rest. Updated b and t and check next grain of sand.
        break
    b.add(s)
    t += 1

print(t)
       