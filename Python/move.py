import os
import shutil

folder_path = "/Users/joel/Library/CloudStorage/OneDrive-UniversityofTexasatSanAntonio/UTSA/EPICS/Python"
target_folder_prefix = "Folder"
num_target_folders = 5
image_formats = [".jpg", ".jpeg", ".png", ".gif"]  # Add more formats as needed

def distribute_images_to_folders(folder_path, target_folder_prefix, num_target_folders, image_formats):
    images = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext in image_formats:
                images.append(filename)
    
    images_per_folder = len(images) // num_target_folders
    
    for i in range(num_target_folders):
        target_folder_name = f"{target_folder_prefix}_{i+1}"
        os.makedirs(target_folder_name, exist_ok=True)
        
        start_index = i * images_per_folder
        end_index = (i + 1) * images_per_folder if i < num_target_folders - 1 else len(images)
        
        for image_index in range(start_index, end_index):
            image_name = images[image_index]
            source_path = os.path.join(folder_path, image_name)
            target_path = os.path.join(target_folder_name, image_name)
            shutil.move(source_path, target_path)
            print(f"Moved: {image_name} -> {target_folder_name}")

if __name__ == "__main__":
    distribute_images_to_folders(folder_path, target_folder_prefix, num_target_folders, image_formats)
