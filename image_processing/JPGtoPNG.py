import sys
import os
from PIL import Image

input_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):               # Making the new folder if not existent
    os.makedirs(output_folder)

for file in os.listdir(input_folder):           # Loop through every file
    img = Image.open(f"{input_folder}{file}")       # Opening each file
    clean_name = os.path.splitext(file)[0]          # Cleaning the name and removing .jpg
    img.save(f"{output_folder}{clean_name}.png", "png")     # Saving the converted png file
    print("All done!!")

