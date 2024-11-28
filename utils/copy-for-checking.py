import os
import csv
import ast
import shutil

input_folder = "datasets/test_dataset_singles"
input_file = "multi-16-24.jpg"
output = "C:\\Users\\julka\\Desktop\\test\\25 test"

with open("datasets/multiple-bean-files.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")

    for row in reader:
        if row[0] == input_file:
            files = row[1]

for file in ast.literal_eval(files):
    source_path = os.path.join(input_folder, file)
    dest_path = os.path.join(output, file)

    if os.path.exists(source_path):
        shutil.copy(source_path, dest_path)
        print(f"Copied {file}")
