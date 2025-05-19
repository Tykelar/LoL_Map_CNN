import os
import shutil

# === CONFIGURATION ===
source_folder = "./dataset"
destination_folder = "./dataset/stored"

# === FUNCTION TO PARSE AND MOVE FILES ===
def organize_images():
    for filename in os.listdir(source_folder):
        if not filename.lower().endswith(('.jpg')):
            continue  # Skip non-jpg files

        parts = filename.split()
        
        # Handle GLOB type: "Match<id> Glob <time> <red/blue>.jpg"
        if "Glob" in parts:
            match_id = parts[0]
            color = parts[-1].split('.')[0]  # Remove extension
            if color not in ['red', 'blue']:
                continue  # Skip unknown color

            dest = os.path.join(destination_folder, "glob", color)
        
        # Handle IND type: "Match<id> Ind <True/False> <role>.jpg"
        elif "Ind" in parts:
            match_id = parts[0]
            win_status = parts[2].lower()  # true or false
            role = parts[3].split('.')[0]  # remove extension

            if role not in ['adc', 'top', 'jungle', 'support', 'mid']:
                continue  # Skip unknown roles (broken naming)

            dest = os.path.join(destination_folder, "ind", role, win_status)
        
        else:
            continue  # Skip unknown format

        # Create destination directory if it doesn't exist
        os.makedirs(dest, exist_ok=True)

        # Move file
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(dest, filename)
        shutil.move(src_path, dst_path)
        print(f"Moved: {filename} → {dest}")

# === RUN SCRIPT ===
if __name__ == "__main__":
    organize_images()
