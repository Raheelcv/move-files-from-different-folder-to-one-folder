import os
import shutil

# Define the path to your main folder (where all date-wise folders are stored)
source_folder = r'C:\Users\rahee\Downloads\dataset\ICF_RYK_head_dataset'

# Define the path to the target folder where you want to move all images
target_folder = r'C:\Users\rahee\Downloads\dataset\ICF_RYK_head_dataset\output'

# Make sure the target folder exists, or create it
os.makedirs(target_folder, exist_ok=True)

# Loop through all subfolders in the main folder
for root, _, files in os.walk(source_folder):
    for file in files:
        # Check if the file is an image (add more extensions if needed)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', 'txt')):
            # Define the full path to the source and destination
            source_path = os.path.join(root, file)
            destination_path = os.path.join(target_folder, file)

            # Move the file to the target folder
            shutil.move(source_path, destination_path)
            print(f"Moved: {source_path} to {destination_path}")

print("All images have been moved to the target folder.")
