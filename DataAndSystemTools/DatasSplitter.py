import os
import shutil
import random

# === CONFIGURATION ===
base_input_dir = "../dataset/stored"
base_output_dir = "../dataset"
train_split = 0.7
val_split = 0.15
test_split = 0.15

# === FUNCTION TO SPLIT DATA ===
def split_dataset():
    for root, dirs, _ in os.walk(base_input_dir):
        for dir_name in dirs:
            class_dir = os.path.join(root, dir_name)
            images = [f for f in os.listdir(class_dir) if f.lower().endswith(('.jpg'))]

            random.shuffle(images)

            total = len(images)
            train_end = int(total * train_split)
            val_end = train_end + int(total * val_split)

            sets = {
                'train': images[:train_end],
                'val': images[train_end:val_end],
                'test': images[val_end:]
            }

            # Detect subfolder path (e.g., red/ or adc/true/)
            rel_path = os.path.relpath(class_dir, base_input_dir)

            for set_name, set_images in sets.items():
                target_dir = os.path.join(base_output_dir, set_name, rel_path)
                os.makedirs(target_dir, exist_ok=True)
                for img in set_images:
                    src = os.path.join(class_dir, img)
                    dst = os.path.join(target_dir, img)
                    shutil.move(src, dst)
                print(f"Moved {len(set_images)} images to {set_name}/{rel_path}")

# === RUN SCRIPT ===
if __name__ == "__main__":
    split_dataset()
