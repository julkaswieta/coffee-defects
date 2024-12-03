import torch
import torchvision
import time
import copy
import os
import csv
from torchvision import models, transforms, datasets
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder

model = models.resnet18(pretrained=True)

# values required by ResNet
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]

# select the device the model training will run on
device = torch.device("cuda")
print(device)


# Define the transforms for the images in the dataset
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(256),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)
    ]),
    'valid': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)
    ]),
}

# Load in the data
data_directory = "./datasets/converted_dataset"

image_datasets = {x: ImageFolder(os.path.join(data_directory, x),
                                 data_transforms[x])
                  for x in ['train', 'valid']}

dataloaders = {x: DataLoader(image_datasets[x], batch_size=4,
                             shuffle=True, num_workers=0)
               for x in ['train', 'valid']}

dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'valid']}
class_names = image_datasets['train'].classes

# Freeze the pre-trained layers
for param in model.parameters():
    param.requires_grad = False

# Modify the fully connected layer to consist of 4 FC layers
# the number of features that the current FC was accepting
input_features = model.fc.in_features

model.fc = nn.Linear(input_features, 4)

# Choose optimizer, criterion and scheduler
optimizer = optim.SGD(model.fc.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)

# Send the model to the device that will train it
model = model.to(device)

# train the model


def train_model(model, criterion, optimizer, scheduler, num_epochs=25):
    since = time.time()

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)

        # Each epoch has a training and validation phase
        for phase in ['train', 'valid']:
            if phase == 'train':
                model.train()  # Set model to training mode
            else:
                model.eval()   # Set model to evaluate mode

            running_loss = 0.0
            running_corrects = 0

            # Iterate over data.
            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)

                # forward
                # track history if only in train
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    # backward + optimize only if in training phase
                    if phase == 'train':
                        optimizer.zero_grad()
                        loss.backward()
                        optimizer.step()

                # statistics
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)

            if phase == 'train':
                scheduler.step()

            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = running_corrects.double() / dataset_sizes[phase]

            print('{} Loss: {:.4f} Acc: {:.4f}'.format(
                phase, epoch_loss, epoch_acc))

            with open("resnet-output.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                # Epoch, phase, loss, accuracy
                formatted_accuracy = "{:.4f}".format(epoch_acc)
                writer.writerows(
                    [[epoch, phase, epoch_loss, formatted_accuracy]])

            # deep copy the model
            if phase == 'valid' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())

        print()

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))
    print('Best val Acc: {:4f}'.format(best_acc))

    # load best model weights
    model.load_state_dict(best_model_wts)
    torch.save(model.state_dict(), "trained_cnn.pt")

    return model


epochs = 25

model = train_model(model, criterion, optimizer, scheduler, epochs)
