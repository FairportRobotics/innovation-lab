import os
import shutil
from tqdm import tqdm

n_training = 100 # The number of images you want in the training set
base_dir = "./images/processed/"
save_dir = "./data/"

training_set = set()
validation_set = set()


# Clean up the files and directories
if os.path.isdir(save_dir):
    shutil.rmtree(save_dir)

# Break files into training and validation
for file_name in os.listdir(base_dir):
    if ".txt" in file_name and file_name != "classes.txt":
        if len(training_set) < n_training:
            training_set.add(file_name)
        else:
            validation_set.add(file_name)

# Move files to their right spot
for path_part, label_file_names in [("train", training_set), ("val", validation_set)]:
    os.makedirs(f"{save_dir}{path_part}/labels/", exist_ok=True)
    os.makedirs(f"{save_dir}{path_part}/images/", exist_ok=True)
    for label_file_name in tqdm(label_file_names, desc=path_part):
        image_file_name = label_file_name.replace("txt", "jpg")
        shutil.copy(
            f"{base_dir}{label_file_name}",
            f"{save_dir}{path_part}/labels/{label_file_name}",
        )
        shutil.copy(
            f"{base_dir}{image_file_name}",
            f"{save_dir}{path_part}/images/{image_file_name}",
        )
