from ultralytics import YOLO
import torch

def train_detector():
    model = YOLO("yolov8m.pt")
    model.train(task="detect", data="datasets/bean_dataset/data.yaml",
                epochs=50, plots=True, patience=20, workers=0)

def train_classifier():
    model = YOLO("yolov8m-cls.pt")
    model.train(data="datasets/converted_dataset", epochs=25, plots=True, imgsz=256, workers=0)

torch.cuda.set_device(0)
print(torch.cuda.get_device_name())
train_detector()
