from app.detect import detect_beans, crop_beans
import os

images_to_detect = ["multi-9-2.jpg", "multi-9-9.jpg", "multi-9-16.jpg", "multi-9-23.jpg", "multi-9-30.jpg",
                    "multi-16-2.jpg", "multi-16-9.jpg", "multi-16-16.jpg", "multi-16-23.jpg", "multi-16-30.jpg",
                    "multi-25-2.jpg", "multi-25-9.jpg", "multi-25-16.jpg", "multi-25-23.jpg", "multi-25-30.jpg"]

input_folder = "datasets\multiple_beans_test"

for img in images_to_detect:
    output_folder = "outputs_" + img.replace(".jpg", "")
    img_path = os.path.join(input_folder, img)
    result = detect_beans(img_path, 1024)
    crop_beans(result, img_path, output_folder)
