
cleaned_paths = []
cleaned_paths.append(path)
current_path = os.environ.get("PATH", "")
def ensure_window_os_variable_path_deduplicated():
else:
final_path = ";".join(cleaned_paths)
for i, p in enumerate(cleaned_paths, 1):
for path in path_list:
if len(final_path) > 1024:
if path and path.lower() not in seen:
if result == 0:
import os
path = path.strip()
path_list = current_path.split(";")
print("[ERROR] Failed to update system PATH.")
print("[SUCCESS] System PATH deduplicated and updated successfully.")
print("[WARNING] PATH is too long. 'setx' may truncate it.")
print("\n[PATH] Final deduplicated PATH entries:")
print(f"[PATH_ENTRY {str(i).zfill(2)}] {p}")
result = os.system(f'setx PATH "{final_path}"')
seen = set()
seen.add(path.lower())
