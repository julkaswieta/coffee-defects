from ultralytics import YOLO

# Upload image
image_path = "C:\\Users\\julka\\Desktop\\test\\peaberry-90.jpg"

detect_model = YOLO("models/bean_defect_detect.pt")
results = detect_model.predict(image_path)

count = 0
# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    confidence = boxes.conf
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen]
    result.save(filename="result.jpg")  # save to disk
    print(confidence)
