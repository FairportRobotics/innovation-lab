from ultralytics import YOLO
import os

epochs = 300
base_dir = os.getcwd()
yaml_file_name = "custom.yaml"
train = f"{base_dir}/data/train".replace("/", "\\")
val = f"{base_dir}/data/val".replace("/", "\\")
class_names = []
nc = 0

# Build the list of classes and the number of classes
with open("./classes.txt") as file:
    for line in file:
        class_names.append(line.strip())
        nc += 1

# Create the YAML file used in the training process
with open(f"{base_dir}/{yaml_file_name}", "w") as file:
    file.write(f"train: {train}\n")
    file.write(f"val: {val}\n")
    file.write(f"nc: {nc}\n")
    names = '", "'.join(class_names)
    file.write(f'names: ["{names}"]')


# Train the model
model = YOLO("yolov8s.pt")
model.train(data=yaml_file_name, epochs=epochs)
metrics = model.val()
print("Check " + metrics.save_dir)
