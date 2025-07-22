

def get_pnx_unix_style(pnx):
    pnx = pnx.replace(f"\\", rf"/")
    pnx = pnx.strip()
    return pnx
