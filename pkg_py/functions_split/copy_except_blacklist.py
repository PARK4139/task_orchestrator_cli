
"""
# 디렉토리 제외
# 파일 복사
Args:
Copy files from src_dir to dst_dir excluding any files or directories
continue
copied_count += 1
copied_count = 0
def copy_except_blacklist(src_dir, dst_dir, exclude_names):
dirs[:] = [d for d in dirs if d not in exclude_names]
dst_dir (str): Destination directory.
dst_path = os.path.join(dst_dir, rel_path)
exclude_names (set): Set of names (files or folders) to exclude.
for file in files:
for root, dirs, files in os.walk(src_dir):
if file in exclude_names:
if not os.path.exists(dst_dir):
os.makedirs(dst_dir)
os.makedirs(os.path.dirname(dst_path), exist_ok=True)
print(f"[COPIED] {rel_path}")
print(f"[{PkMessages2025.DONE}] {copied_count} file(s) copied to '{dst_dir}'.")
rel_path = os.path.relpath(src_path, src_dir)
shutil.copy2(src_path, dst_path)
src_dir (str): Source directory.
src_path = os.path.join(root, file)
whose names match those in exclude_names.
