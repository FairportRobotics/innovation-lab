import os
import shutil

# TODO: Make sure to edit classes.txt in the root directory before running this

base_dir = os.getcwd()
image_dir =  f"{base_dir}/images/processed".replace("\\", "/")
class_file = f"{image_dir}/classes.txt"

# Copy the classes over to the processed directory
shutil.copy(f"{base_dir}/classes.txt", class_file)

os.system(f"labelImg {image_dir} {class_file} {image_dir}")