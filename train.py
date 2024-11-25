from ultralytics import YOLO

model = model = YOLO("yolov8m.pt")

model.train(data="datasets/data.yaml", epochs=3)
