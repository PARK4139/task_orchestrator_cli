import os

def remove_pk_prefix_from_filenames():
    current_dir = os.getcwd()
    for filename in os.listdir(current_dir):
        if filename.startswith("pk_"):
            new_name = filename[3:]  # 'pk_' 제거
            src = os.path.join(current_dir, filename)
            dst = os.path.join(current_dir, new_name)
            if os.path.exists(dst):
                print(f"❗ Skipping (already exists): {new_name}")
                continue
            os.rename(src, dst)
            print(f"✅ Renamed: {filename} → {new_name}")

if __name__ == "__main__":
    remove_pk_prefix_from_filenames()
