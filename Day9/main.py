import numpy as np


def create_grid(N):
    """
    Create a grid containing only zeros.
    param N: grid size
    return: grid containing only zeros
    """

    return np.zeros((N,N))

def initial_pos(row, col, N):
    """
    Set initial posistion to head and tail
    param x: initial x-position
    param y: initial y-position
    """

    grid = create_grid(N)

    head = grid[row][col]
    tail = grid[row][col]

    return head, tail

def update_pos(movement, head, tail):
    """
    Update posisition of head and tail
    param movement: [direction, steps]
    param head: position to head
    param tail: posistion to tail
    """

    direction = movement[0]
    steps = int(movement[1])



    match direction:
        case "D":
            row = row - int(steps)
            col = col
            head = head[row][col]
        case "U":
            row = row + int(steps)
            col = col
        case "L":
            row = row
            col = col - int(steps)
            head = head[row][col]
        case "R":
            row = row
            col = col - int(steps)
            head = head[row][col]

    return head







# Open text.txt file and append movement at each step to movement_head
with open("text.txt", "r") as f:
    lines = f.readlines()

    # Array containing the direction the head is moving and the number of steps in that direction
    movement_head = []
    
    # Loop through each line and split ut string into action and number of steps
    for line in lines:
        action = line.split()
        movement_head.append(action)



