from ultralytics import YOLO
import os
import cv2


def detect_beans(image, imgsz):
    model = YOLO("models/defect_detect_yolo.pt")
    # agnostic-nms - class-agnostic nms to get rid of multiple class predictions for the same bean
    return model.predict(image, agnostic_nms=True, imgsz=imgsz)


def crop_beans(results, img_path, output_folder):
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


def process_image(image, output_folder):
    results = detect_beans(image, 1024)
    crop_beans(results, image, output_folder)
