import os
import shutil

base_dir = os.getcwd()
image_dir =  f"{base_dir}/images/raw".replace("\\", "/")
save_dir = image_dir.replace("raw", "processed")
class_file = f"{save_dir}/classes.txt"

shutil.copy(f"{base_dir}/classes.txt", class_file)

os.system(f"labelImg {image_dir} {class_file} {save_dir}")