from ultralytics import YOLO

model = YOLO("yolov8s.pt")

model.train(task="detect", data="datasets/bean_dataset/data.yaml",
            epochs=20, plots=True)
