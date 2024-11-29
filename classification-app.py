from ultralytics import YOLO
import os
import cv2
import time

# Upload image
image_path = "datasets/multiple_beans_test/multi-16-24.jpg"
output_folder = "outputs" + str(int(time.time()))
detect_model = YOLO("models/bean_defect_detect.pt")
classify_model = YOLO("runs\\classify\\train7\\weights\\best.pt")


def detect_beans(model, image, imgsz):
    # agnostic-nms - class-agnostic nsm to get rid of multiple class predictions for the same bean
    return model.predict(image, agnostic_nms=True, imgsz=imgsz)


def crop_beans(results):
    # Code from: https://github.com/ultralytics/ultralytics/issues/5097
    result = results[0]

    # Extract bounding boxes
    boxes = result.boxes
    coords = boxes.xyxy.tolist()
    classes = boxes.cls.tolist()

    # crop the image into predicted objects
    img = cv2.imread(image_path)
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


results = detect_beans(detect_model, image_path, 1024)
results[0].show()
crop_beans(results)
process_single_beans()
