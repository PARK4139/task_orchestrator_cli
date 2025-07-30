def get_drives_connected():
    import os
    import string

    from pkg_py.functions_split.ensure_printed import ensure_printed

    drives = []
    for letter in string.ascii_uppercase:
        drive = f"{letter}:\\"
        if os.path.exists(drive):
            drives.append(drive)
    ensure_printed(f"연결된 드라이브: {drives}")
    return drives
