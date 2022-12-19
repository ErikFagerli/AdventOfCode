

def surface_area(droplet):
  # Determine the bounding box of the droplet
  min_x = min(cube[0] for cube in droplet)
  max_x = max(cube[0] for cube in droplet)
  min_y = min(cube[1] for cube in droplet)
  max_y = max(cube[1] for cube in droplet)
  min_z = min(cube[2] for cube in droplet)
  max_z = max(cube[2] for cube in droplet)

  # Create a 3D grid with the size of the bounding box
  grid = [[[False for _ in range(min_z, max_z+1)]
            for _ in range(min_y, max_y+1)]
           for _ in range(min_x, max_x+1)]

  # Mark the positions of the cubes in the droplet as occupied
  for cube in droplet:
    x, y, z = cube
    grid[x-min_x][y-min_y][z-min_z] = True

  # Count the number of exposed sides for each occupied cell
  exposed_sides = 0
  for x in range(len(grid)):
    for y in range(len(grid[0])):
      for z in range(len(grid[0][0])):
        if not grid[x][y][z]:
          continue
        # Check the six adjacent cells
        if x == 0 or not grid[x-1][y][z]:
          exposed_sides += 1
        if x == len(grid)-1 or not grid[x+1][y][z]:
          exposed_sides += 1
        if y == 0 or not grid[x][y-1][z]:
          exposed_sides += 1
        if y == len(grid[0])-1 or not grid[x][y+1][z]:
          exposed_sides += 1
        if z == 0 or not grid[x][y][z-1]:
          exposed_sides += 1
        if z == len(grid[0][0])-1 or not grid[x][y][z+1]:
          exposed_sides += 1

  return exposed_sides

def create_tuples(file):
    droplets = []
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            line = line.split(",")
            droplet = tuple(map(int, line))
            droplets.append(droplet)

    return droplets

def main():
    droplets = create_tuples("text.txt")
    exposed_sides = surface_area(droplets)

    print(exposed_sides)


if __name__ == "__main__":
    main()