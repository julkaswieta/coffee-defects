import os
import shutil

input_dataset_dir = "./datasets"
output_dataset_dir = "./converted_dataset"

mode_directories = ["/train", "/valid", "/test"]
classes = ["defect", "longberry", "peaberry", "premium"]


for mode in mode_directories:
    mode_dir = output_dataset_dir + mode
    # create output dir
    os.makedirs(mode_dir, exist_ok=True)
    # print(f"Created dir: {mode_dir}")

    labels_dir = input_dataset_dir + mode + "/labels"
    images_dir = input_dataset_dir + mode + "/images"

    # print(f"Labels: {labels_dir} \t Images: {images_dir}")

    # create class directories within mode directory
    for class_name in classes:
        class_dir = os.path.join(mode_dir, class_name)
        os.makedirs(class_dir, exist_ok=True)
        # print(f"Make dir: {class_dir}")

    # go through all label files
    for label_file in os.listdir(labels_dir):

        if label_file.endswith(".txt"):
            with open(os.path.join(labels_dir, label_file), "r") as file:
                lines = file.readlines()

            if lines:
                class_id = int(lines[0].split()[0])
                class_name = classes[class_id]
                image_name = label_file.replace(".txt", ".jpg")
                image_path = os.path.join(images_dir, image_name)

                if (os.path.exists(image_path)):
                    # copy the image to the correct class folder
                    shutil.copyfile(image_path, os.path.join(
                        mode_dir, class_name, image_name))
                else:
                    print(f"Warning: Image file {image_path} not found.")
