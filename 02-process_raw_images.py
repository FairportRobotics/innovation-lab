import hashlib
import os
from PIL import Image

save_path = "./images/processed/"
# Create the directory if it's not created
if not os.path.isdir(save_path):
    os.makedirs(save_path)

# Loop over the directories
for dirs, subdir, files in os.walk("./images/raw"):
    # Loop over files
    for file in files:
        try:
            # Read the data
            img = Image.open(f"{dirs}/{file}")
            # Convert to RGB color palette
            img = img.convert("RGBA")
            img = img.convert("RGB")
            # Create a hash of the image
            hash = hashlib.md5(img.tobytes()).hexdigest()
            # Save the image as a jpg
            img.save(f"{save_path}{hash}.jpg")
        except:
            # Print a helpful message when something goes wrong
            print(f"ERROR: Could not standardize {file}")
