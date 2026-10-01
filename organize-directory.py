import os
import shutil

def organize_directory(path):
    
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)): 
            continue  # Skip directories
        
        # Extract the file extension and format directory name
        
        # name.jpg
        filename, file_extension = os.path.splitext(file)
        directory = file_extension[1:].upper() 
        
        if not directory:
            directory = "Other"
        
        new_dir_path = os.path.join(path, directory)
        # usr/dir/JPG
        
        os.makedirs(new_dir_path, exist_ok=True)
        
        # Move the file to the new directory
        shutil.move(os.path.join(path, file), os.path.join(new_dir_path, file))
        print(f"Moved {file} --> {new_dir_path}")
        

def main():
    target_dir = "/Users/adjoda/personal/DEV/UDEMY/python-code/test_dir"

    if not os.path.exists(target_dir):
        print(f"Folder does not exist: {target_dir}")
        return

    organize_directory(target_dir)

if __name__ == "__main__":
    main()

