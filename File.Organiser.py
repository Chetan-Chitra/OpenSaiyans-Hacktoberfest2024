import os
import shutil

# Define the directory to organize
folder_to_organize = "/path/to/your/folder"  # Change this to your folder path

# Define file categories based on extensions
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx', '.csv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Video': ['.mp4', '.mkv', '.avi', '.mov', '.flv'],
    'Archives': ['.zip', '.tar', '.rar', '.gz'],
    'Scripts': ['.py', '.js', '.java', '.cpp', '.c', '.sh'],
    'Others': []
}

# Create folders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(folder_to_organize, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for filename in os.listdir(folder_to_organize):
    file_path = os.path.join(folder_to_organize, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    file_extension = os.path.splitext(filename)[1].lower()

    moved = False
    for folder, extensions in file_types.items():
        if file_extension in extensions:
            shutil.move(file_path, os.path.join(folder_to_organize, folder, filename))
            moved = True
            break

    # Move to 'Others' if file type is not recognized
    if not moved:
        shutil.move(file_path, os.path.join(folder_to_organize, 'Others', filename))

print("Files have been organized.")
