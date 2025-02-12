import os
import shutil

# Define the path to your main folder (where all date-wise folders are stored)
source_folder = r'C:\Users\rahee\Downloads\dataset\ICF_RYK_head_dataset'

# Define the path to the target folder where you want to move matched files
target_folder = r'C:\Users\rahee\Downloads\dataset\ICF_RYK_head_dataset\output'

# Make sure the target folder exists, or create it
os.makedirs(target_folder, exist_ok=True)

# Initialize a counter for moved files
moved_files_count = 0

# Loop through all subfolders in the main folder
for root, _, files in os.walk(source_folder):
    for file in files:
        # Check if the file name starts with 'ICF-AO6' and ends with .jpg or .png
        if file.startswith('ICF-AO6') and (file.endswith('.jpg') or file.endswith('.png')):
            # Define the full path to the source and destination
            source_path = os.path.join(root, file)
            destination_path = os.path.join(target_folder, file)

            # Move the file to the target folder
            try:
                shutil.move(source_path, destination_path)
                print(f"Moved: {source_path} to {destination_path}")
                moved_files_count += 1
            except Exception as e:
                print(f"Failed to move {source_path}: {e}")

# Summary of results
if moved_files_count == 0:
    print("No files starting with 'ICF-AO6' were found.")
else:
    print(f"Total files moved: {moved_files_count}")



