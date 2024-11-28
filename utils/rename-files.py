import os

test_directory = "datasets/converted_dataset/test"

dirs = ["defect", "longberry", "peaberry", "premium"]

# Rename all files to class-count.jpg
for dir in dirs:
    dir_path = os.path.join(test_directory, dir)

    count = 0
    for file in os.listdir(dir_path):
        if file.endswith(".jpg"):
            old_path = os.path.join(dir_path, file)
            new_name = dir + "-" + str(count) + ".jpg"
            new_path = os.path.join(dir_path, new_name)
            os.rename(old_path, new_path)
            count += 1
