import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    """Move all .jpg files from source_folder to destination_folder."""
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Get list of files in source folder
    files = os.listdir(source_folder)
    
    # Counter for moved files
    moved_count = 0
    
    # Iterate through files and move .jpg files
    for file in files:
        if file.lower().endswith('.jpg'):
            source_path = os.path.join(source_folder, file)
            dest_path = os.path.join(destination_folder, file)
            shutil.move(source_path, dest_path)
            print(f"Moved: {file} to {destination_folder}")
            moved_count += 1
    
    if moved_count == 0:
        print("No .jpg files found in the source folder.")
    else:
        print(f"Total .jpg files moved: {moved_count}")

def main():
    """Main function to run the automation script."""
    # Define source and destination folders
    source_folder =  "D:\source"  
    destination_folder = "D:\jpg_files" 
    
    print(f"Moving .jpg files from '{source_folder}' to '{destination_folder}'...")
    try:
        move_jpg_files(source_folder, destination_folder)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
