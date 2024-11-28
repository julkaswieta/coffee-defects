import os
import random
import csv
import math
from PIL import Image

single_bean_imgs_folder = "datasets/test_dataset_singles"
output_directory = "datasets/multiple_beans_test"
os.makedirs(output_directory, exist_ok=True)

img_filenames = [filename for filename in os.listdir(single_bean_imgs_folder)]
random.shuffle(img_filenames)  # shuffle to get random ordering

num_beans_per_img = [9, 16, 25]  # 50 imgs in total
final_img_size = 500

# there's 1600 imgs in the folder so there will be 32 sets of trios of images 32 x [9, 16, 25]
for img_set in range(32):
    for img_size in num_beans_per_img:
        # choose files
        chosen_imgs = img_filenames[:img_size]
        img_filenames = img_filenames[img_size:]

        multi_img_filename = "multi-" + \
            str(img_size) + "-" + str(img_set) + ".jpg"
        multi_img_path = os.path.join(output_directory, multi_img_filename)
        print(multi_img_path)

        with open("datasets/mutliple-bean-files.csv", "a", newline="") as file:
            writer = csv.writer(file)
            # filename, files inside
            writer.writerow([multi_img_filename, chosen_imgs])

        # open the images
        images = [Image.open(os.path.join(single_bean_imgs_folder, img))
                  for img in chosen_imgs]

        img_per_column = int(math.sqrt(img_size))

        column_size = int(500 / img_per_column)
        new_img_size = (column_size, column_size)

        images = [img.resize(new_img_size) for img in images]

        # create the image
        new_image = Image.new("RGB", (final_img_size, final_img_size))

        for i, img in enumerate(images):
            # Ensure x is an integer
            x = (i % img_per_column) * new_img_size[0]
            y = (i // img_per_column) * \
                new_img_size[1]  # Ensure y is an integer
            new_image.paste(img, (x, y))

        # save the image
        new_image.save(multi_img_path)
        print(f"Saved file to {multi_img_path}")
