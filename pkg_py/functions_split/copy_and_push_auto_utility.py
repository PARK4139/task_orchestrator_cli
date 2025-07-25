
"# .gitignore",
".git",
".gitignore",
".idea",
".venv",
"__pycache__",
"pk_system.egg-info",
# os.system(command=rf"call {DEST_DIR}\pk_push_project_to_github.bat")
# 제외할 파일/디렉토리 이름
DEST_DIR = rf"{downloads_path}\auto_utility"
EXCLUDE_NAMES = {
SOURCE_DIR = rf"{downloads_path}\pk_system"
copy_except_blacklist(SOURCE_DIR, DEST_DIR, EXCLUDE_NAMES)
def copy_and_push_auto_utility():
downloads_path = os.path.join(os.environ["USERPROFILE"], "Downloads")
dst = rf"{DEST_DIR}\.gitignore"
except Exception as e:
except FileNotFoundError:
if os.path.exists(dst):
os.chdir(path=DEST_DIR)
os.remove(dst)  # 덮어쓰기
os.system(command=rf"call {DEST_DIR}\pk_push_project_to_github_hybrid.bat")
print(f"[ERROR] Source file not found: {src}")
print(f"[ERROR] Unexpected error: {e}")
print(f"[OK] Overwritten:\n{src}\n→ {dst}")
shutil.move(src, dst)  # 이동 및 이름 변경
src = rf"{DEST_DIR}\.gitignore_for_public"
try:
}
