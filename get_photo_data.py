import os

# r = raw string
folder_path = r"D:\Work\_PythonSuli\kezdo-230701\photos"

# check if path exists
assert os.path.exists(folder_path), f"Path does not exist: {folder_path}"

# check if folder_path is a directory
assert os.path.isdir(folder_path), f"Path must be a directory. {folder_path}"

# get all files and folders from folder_path
files = os.listdir(folder_path)

for i in files:
    full_path = os.path.join(folder_path, i)
    print(full_path)