import os
import re

def sanitize_filename(filename):
    # Remove any characters that aren't alphanumeric, underscore, hyphen, or period
    return re.sub(r'[^\w\-.]', '_', filename)

def rename_images(root_dir):
    character_counters = {}

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip the root directory itself
        if dirpath == root_dir:
            continue

        character_name = os.path.basename(dirpath)
        if character_name not in character_counters:
            character_counters[character_name] = 1

        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                old_path = os.path.join(dirpath, filename)
                extension = os.path.splitext(filename)[1]
                
                # Use a shorter naming convention
                new_filename = f"{character_name[:3]}_{character_counters[character_name]:03d}{extension}"
                new_path = os.path.join(dirpath, new_filename)
                
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")
                
                character_counters[character_name] += 1

if __name__ == "__main__":
    root_directory = "images/gallery/JMOSN-HAT"  # This path is correct based on your file structure
    rename_images(root_directory)
    print("Image renaming complete!")