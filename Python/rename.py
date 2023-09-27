import os

folder_path = "/Users/joel/Library/CloudStorage/OneDrive-UniversityofTexasatSanAntonio/UTSA/EPICS/Python"
image_formats = [".jpg", ".jpeg", ".png", ".gif"]  # Add more formats as needed JD

def rename_images_in_folder(folder_path, image_formats):
    image_count = 0
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext in image_formats:
                image_count += 1
                new_filename = f"Vianca{image_count:02d}{file_ext}"
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    rename_images_in_folder(folder_path, image_formats)
