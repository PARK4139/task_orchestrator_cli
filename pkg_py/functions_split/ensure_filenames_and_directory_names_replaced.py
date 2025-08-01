from pkg_py.functions_split.get_file_id import get_file_id


def ensure_filenames_and_directory_names_replaced():
    import inspect
    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
    from pkg_py.functions_split.ensure_pnx_removed import ensure_pnx_removed
    from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
    from pkg_py.system_object.directories import D_PKG_TXT

    func_n = inspect.currentframe().f_code.co_name
    key_name = "d_working"
    d_working = get_values_from_historical_file_routine(file_id=get_file_id(key_name, func_n), key_hint=f'{key_name}=', options_default=['pk_working'], editable=True)

    f_files_to_replace = f"{D_PKG_TXT}/files_to_replace_via_{func_n}.txt"
    ensure_pnx_removed(pnx=f_files_to_replace)
    ensure_pnx_made(pnx=f_files_to_replace, mode='f')

    print(f"\n[INFO] Scanning files and directories under '{d_working}'...")
    paths = get_all_paths(d_working)
    print(f"[INFO] Total {len(paths)} items found (files + directories).\n")

    replacements = load_replacements(f_files_to_replace)
    if not replacements:
        print("[ERROR] No valid replacement rules found.")
        return

    print("[PREVIEW] The following renames will be applied:\n")
    for line in preview_renames(paths, replacements):
        print(line)

    print("\n[INFO] Press ENTER to apply the above changes. Press Ctrl+C to cancel.")
    input()

    print("\n[INFO] Rename in progress...\n")
    for line in apply_renames(paths, replacements):
        print(line)


def load_replacements(path):
    replacements = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            if "=>" in line:
                src, dst = line.strip().split("=>")
                replacements.append((src.strip(), dst.strip()))
    return replacements


def is_hidden(filepath: Path):
    return any(part.startswith('.') for part in filepath.parts)


def get_all_paths(root_dir):
    paths = [p for p in Path(root_dir).rglob("*") if not is_hidden(p)]
    dirs = sorted([p for p in paths if p.is_dir()], key=lambda x: len(str(x)), reverse=True)
    files = [p for p in paths if p.is_file()]
    return files + dirs


def preview_renames(paths, replacements):
    preview = []
    for p in paths:
        new_name = p.name
        for old, new in replacements:
            new_name = new_name.replace(old, new)
        if new_name != p.name:
            preview.append(f"[RENAME] {p} → {new_name}")
    return preview


def apply_renames(paths, replacements):
    results = []
    for p in paths:
        new_name = p.name
        for old, new in replacements:
            new_name = new_name.replace(old, new)

        if new_name == p.name:
            continue

        new_path = p.with_name(new_name)
        if new_path.exists():
            results.append(f"[SKIPPED - EXISTS] {new_path}")
            continue

        try:
            move(str(p), str(new_path))
            results.append(f"[RENAMED] {p} → {new_path}")
        except Exception as e:
            results.append(f"[RENAME FAILED] {p}: {e}")
    return results
