from collections import deque

# Convert text file into a grid
grid = [list(x) for x in open("text.txt").read().strip().split("\n")]

# Iterate through each row and column
for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == "S":
            sr = r
            sc = c
            grid[r][c] = "a"
        if item == "E":
            er = r
            ec = c
            grid[r][c] = "z"

# Create a priority que
q = deque()
q.append((0, sr, sc))

# Create visited set 
vis = {(sr, sc)}

while q:
    # Get height, row, and column of the position we are at
    d, r, c = q.popleft()
    # Check all neighbours. Down, up, right, left
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        # Check if we are outside of grid
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        # Check if we have already visited neighbour
        if (nr, nc) in vis:
            continue
        # Check if neighbour has an higher altitude than 1
        if ord(grid[nr][nc]) - ord(grid[r][c]) > 1:
            continue
        # Check if the next node is the neigbour. This should only activate when we are at second last node
        if nr == er and nc == ec:
            print(d + 1)
            exit(0)
        # Add the neighbour to the visited set and que
        vis.add((nr, nc))
        q.append((d + 1, nr, nc))
        