from ultralytics import YOLO
import os
import cv2
import time

detect_model = YOLO("models/defect_detect_yolo.pt")
classify_model = YOLO("models/defect_classify_yolo.pt")


def detect_beans(model, image, imgsz):
    # agnostic-nms - class-agnostic nsm to get rid of multiple class predictions for the same bean
    return model.predict(image, agnostic_nms=True, imgsz=imgsz)


def crop_beans(results, img_path):
    # Code from: https://github.com/ultralytics/ultralytics/issues/5097
    result = results[0]

    # Extract bounding boxes
    boxes = result.boxes
    coords = boxes.xyxy.tolist()
    classes = boxes.cls.tolist()

    # crop the image into predicted objects
    img = cv2.imread(img_path)
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through the bounding boxes
    for i, box in enumerate(coords):
        class_name = result.names[classes[i]]
        x1, y1, x2, y2 = box
        # Crop the object using the bounding box coordinates
        cropped_object = img[int(y1):int(y2), int(x1):int(x2)]
        # Save the cropped object as an image
        filename = class_name + str(i) + '.jpg'
        path = os.path.join(output_folder, filename)
        cv2.imwrite(path, cropped_object)


def process_single_beans():
    outputs = []
    for image in os.listdir(output_folder):
        img_path = os.path.join(output_folder, image)
        # the point is to replace this with a classification model
        results = detect_beans(classify_model, img_path, 256)
        if results and results[0].boxes:  # Ensure results and boxes are not empty
            # Get the class name of the first detected object
            class_id = results[0].boxes[0].cls[0].item()
            class_name = results[0].names[class_id]
            outputs.append((image, class_name))

    for item in outputs:
        print(item)


images_to_detect = ["multi-9-2.jpg", "multi-9-9.jpg", "multi-9-16.jpg", "multi-9-23.jpg", "multi-9-30.jpg",
                    "multi-16-2.jpg", "multi-16-9.jpg", "multi-16-16.jpg", "multi-16-23.jpg", "multi-16-30.jpg",
                    "multi-25-2.jpg", "multi-25-9.jpg", "multi-25-16.jpg", "multi-25-23.jpg", "multi-25-30.jpg"]

# images_to_detect = ["multi-25-2.jpg", "multi-16-4.jpg"]

input_folder = "datasets\multiple_beans_test"

for img in images_to_detect:
    output_folder = "outputs_" + img.replace(".jpg", "")
    img_path = os.path.join(input_folder, img)
    result = detect_beans(detect_model, img_path, 1024)
    crop_beans(result, img_path)
