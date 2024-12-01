import os
import csv
import ast
import shutil

input_folder = "datasets/test_dataset_singles"
input_file = "multi-16-24.jpg"
output = "C:\\Users\\julka\\Desktop\\test"

images_to_detect = ["multi-9-2.jpg", "multi-9-9.jpg", "multi-9-16.jpg", "multi-9-23.jpg", "multi-9-30.jpg",
                    "multi-16-2.jpg", "multi-16-9.jpg", "multi-16-16.jpg", "multi-16-23.jpg", "multi-16-30.jpg",
                    "multi-25-2.jpg", "multi-25-9.jpg", "multi-25-16.jpg", "multi-25-23.jpg", "multi-25-30.jpg"]

# images_to_detect = ["multi-9-2.jpg", "multi-9-9.jpg"]

for img in images_to_detect:
    output_folder = os.path.join(output, img.replace(".jpg", ""))
    os.makedirs(output_folder, exist_ok=True)

    with open("datasets/multiple-bean-files.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")

        for row in reader:
            if row[0] == img:
                files = row[1]

    for file in ast.literal_eval(files):
        source_path = os.path.join(input_folder, file)
        dest_path = os.path.join(output_folder, file)

        if os.path.exists(source_path):
            shutil.copy(source_path, dest_path)
            print(f"Copied {file}")
