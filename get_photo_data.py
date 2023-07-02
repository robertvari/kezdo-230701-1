import os
from PIL import Image, ExifTags

# r = raw string
folder_path = r"D:\Work\_PythonSuli\kezdo-230701\photos"

# check if path exists
assert os.path.exists(folder_path), f"Path does not exist: {folder_path}"

# check if folder_path is a directory
assert os.path.isdir(folder_path), f"Path must be a directory. {folder_path}"

# get all files and folders from folder_path
files = os.listdir(folder_path)
allowed_extensions = [".jpg", ".jpeg"]

for i in files:
    full_path = os.path.join(folder_path, i)
    
    # check if extension in allowed_extensions
    extension = os.path.splitext(full_path)[-1]
    if not extension.lower() in allowed_extensions:
        continue

    # open image
    img = Image.open(full_path)
    
    # get the size of the image
    size = img.size

    # get exif data from image
    exif_data = img._getexif()
    if not exif_data:
        continue

    model = exif_data.get(0x0110)
    print(i, model)