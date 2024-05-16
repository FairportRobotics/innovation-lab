import os
import shutil

# TODO: Make sure to edit classes.txt in the root directory before running this

base_dir = os.getcwd()
save_dir =  f"{base_dir}/images/processed".replace("\\", "/")
class_file = f"{save_dir}/classes.txt"

# Copy the classes over to the processed directory
shutil.copy(f"{base_dir}/classes.txt", class_file)

# Launch LabelImg
os.system(f"labelImg {save_dir} {class_file} {save_dir}")