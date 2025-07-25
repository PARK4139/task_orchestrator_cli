
ap = additional_path.strip()
cleaned_paths = []
cleaned_paths.append(ap)
cleaned_paths.append(path)
current_path = os.environ.get("PATH", "")
def update_system_path_with_deduplication(additional_path: str = None):
final_path = ";".join(cleaned_paths)
for path in path_list:
if additional_path:
if ap and ap.lower() not in seen:
if len(final_path) > 1024:
if path and path.lower() not in seen:
import os
os.system(f'setx PATH "{final_path}"')
path = path.strip()
path_list = current_path.split(";")
print("PATH too long! setx may truncate it.")
print("PATH updated with deduplication.")
seen = set()
seen.add(path.lower())
