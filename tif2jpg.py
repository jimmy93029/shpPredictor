import os
from PIL import Image

from_dirname = "test3"
to_dirname = "train3"

directory_path = f"C:\\Users\\ACER\\Desktop\\Project\\{from_dirname}"
file_list = os.listdir(directory_path)

destination = f"C:\\Users\\ACER\\Desktop\\Project\\{to_dirname}"
os.mkdir(destination)

for file in file_list:
    file_path = os.path.join(directory_path, file)
    im = Image.open(file_path)

    dest = os.path.join(destination, file)
    im.save(f'{dest}.jpg')