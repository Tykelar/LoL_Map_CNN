import os
import shutil

# === CONFIGURATION ===
split_dirs = ['train', 'val', 'test']
base_dir = './dataset'
target_dir = os.path.join(base_dir, 'stored')

def move_back_images():
    for split in split_dirs:
        split_path = os.path.join(base_dir, split)
        for root, _, files in os.walk(split_path):
            for file in files:
                if file.lower().endswith(('.jpg')):
                    relative_path = os.path.relpath(root, split_path)
                    src = os.path.join(root, file)
                    dst_dir = os.path.join(target_dir, relative_path)
                    os.makedirs(dst_dir, exist_ok=True)
                    dst = os.path.join(dst_dir, file)
                    shutil.move(src, dst)
                    print(f"Moved: {src} -> {dst}")

if __name__ == "__main__":
    move_back_images()
