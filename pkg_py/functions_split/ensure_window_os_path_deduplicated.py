def ensure_window_os_path_deduplicated():
    import os

    current_path = os.environ.get("PATH", "")
    path_list = current_path.split(";")

    seen = set()
    cleaned_paths = []

    for path in path_list:
        path = path.strip()
        if path and path.lower() not in seen:
            seen.add(path.lower())
            cleaned_paths.append(path)

    final_path = ";".join(cleaned_paths)

    if len(final_path) > 1024:
        print("[WARNING] PATH is too long. 'setx' may truncate it.")

    result = os.system(f'setx PATH "{final_path}"')
    if result == 0:
        print("[SUCCESS] System PATH deduplicated and updated successfully.")
    else:
        print("[ERROR] Failed to update system PATH.")

    print("\n[PATH] Final deduplicated PATH entries:")
    for i, p in enumerate(cleaned_paths, 1):
        print(f"[PATH_ENTRY {str(i).zfill(2)}] {p}")


