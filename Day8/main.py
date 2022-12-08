import numpy as np

grid = []

with open("text.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        row_grid = []
        line = line.rstrip("\n")
        for number in line:
            number = int(number)
            row_grid.append(number)
        grid.append(row_grid)


grid = np.array(grid)

clear_view = 0
tree_score = 0

for index_row, row in enumerate(grid):
    for index_column, tree_value in enumerate(row):

        # Left, Rightm Up, Down
        left_view = np.flip(row[:index_column])
        right_view = row[index_column+1:]

        column = grid.take([index_column], axis=1)
       
        up_view = np.flip(column[:index_row])
        down_view = column[index_row+1:]

        # Part 1
        # if index_row == 0 or index_column == 0 or index_row == 98 or index_column == 98:
        #     clear_view += 1
        #     continue
        # elif tree_value > np.max(left_view) or tree_value > np.max(right_view) or tree_value > np.max(up_view) or tree_value > np.max(down_view):
        #     clear_view += 1
        #     continue

        # Part 2
        right_score = 0
        left_score = 0
        up_score = 0
        down_score = 0

        # Check left side
        if len(left_view) == 0:
            left_score += 0
        else:
            for tree_left in left_view:
                if tree_value > tree_left:
                    left_score += 1
                else:
                    left_score += 1
                    break
        tree_score_left = left_score
            

        # Check right side
        if len(right_view) == 0:
            right_score += 0
        else:
            for tree_right in right_view:
                if tree_value > tree_right:
                    right_score += 1
                else:
                    right_score += 1
                    break
        tree_score_right = right_score
            

        # Check up side
        if len(up_view) == 0:
            up_score += 0
        else:
            for tree_up in up_view:
                if tree_value > tree_up:
                    up_score += 1
                else:
                    up_score += 1
                    break
        tree_score_up = up_score
            

        # Check down side
        if len(down_view) == 0:
            down_score += 0
        else:
            for tree_down in down_view:
                if tree_value > tree_down:
                    down_score += 1
                else:
                    down_score += 1
                    break
        tree_score_down = down_score
            

        tree_score_temp = tree_score_left * tree_score_right * tree_score_up * tree_score_down

        if tree_score_temp > tree_score:
            tree_score = tree_score_temp

print(tree_score)
