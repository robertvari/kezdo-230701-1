import json

with open("photo_data.json") as f:
    photo_data = json.load(f)
    print(photo_data["D:\\Work\\_PythonSuli\\kezdo-230701\\photos\\IMG_1099.JPG"]["date"])