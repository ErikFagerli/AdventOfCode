with open("text.txt", "r") as f:
    file = f.readlines()

class Directory:
  def __init__(self, name, parent=None):
    self.name = name
    self.parent = parent
    self.children = {}
    self.files = {}

# Parse the input and create the tree-like data structure
root = Directory("/")
current_dir = root
for index, line in enumerate(file):
  if line.startswith("$ cd"):
    # Parse the cd command and update the current directory
    parts = line.split()
    if parts[2] == "/":
      # Switch to the root directory
      current_dir = root
    elif parts[2] == "..":
      # Move to the parent directory
      if current_dir.parent is not None:
        current_dir = current_dir.parent
    else:
      # Move to a child directory
      if current_dir.children is not None and parts[2] in current_dir.children:
        current_dir = current_dir.children[parts[2]]
      else:
        # The target directory doesn't exist, ignore the cd command
        pass
  elif line.startswith("$ ls"):
    # Parse the ls command and add the listed files and directories to the current directory
    for entry in file[index+1:]:
      parts = entry.split()
      if parts[0] == "dir":
        # Add a new child directory to the current directory
        current_dir.children[parts[1]] = Directory(parts[1], current_dir)
      elif parts[1] == "cd":
        break  
      else:
        # Add a new file to the current directory
        current_dir.files[parts[1]] = int(parts[0])
# Calculate the total size of each directory
def calculate_size(dir):
  # Start with the size of all the files in this directory
  size = sum(dir.files.values())

  # Add the size of all the child directories
  for child in dir.children.values():
    size += calculate_size(child)
    

  return size

# Find all the directories with a total size of at most 100000
directories = []
def find_directories(dir):
  if calculate_size(dir) <= 100000:
    directories.append(dir)

  # Recurse into the child directories
  for child in dir.children.values():
    find_directories(child)

find_directories(root)

# Calculate the sum of the total sizes of the found directories 
result = sum(calculate_size(dir) for dir in directories)

print(result)

def calculate_size_dir(dir):
    value = 0
    for child in dir.children.values():
        sum(dir.children.values())

calculate_size_dir(root)


