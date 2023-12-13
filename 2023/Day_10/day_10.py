direction = {
    "|": [(0, 1), (0, -1)],
    "-": [(1, 0), (-1, 0)],
    "L": [(1, 1), (-1, -1)],
    "J": [(-1, 1), (1, -1)],
    "7": [(-1, -1), (1, 1)],
    "F": [(1, -1), (-1, 1)],
    "S": ""
}
maze = []
for i, row in enumerate(open("example.txt").read().split("\n")):
    maze.append([])
    for char in row:
        maze[i].append(char)



