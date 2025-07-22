

def get_pnx_windows_style(pnx: str) -> str:
    import re
    path = pnx.replace('//', '/')
    path = re.sub(
        r'^/mnt/([A-Za-z])/',
        lambda m: f"{m.group(1).upper()}:/",
        path
    )
    return path.replace('/', '\\')
