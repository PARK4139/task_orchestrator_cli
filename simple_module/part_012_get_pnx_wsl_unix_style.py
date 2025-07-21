

def get_pnx_wsl_unix_style(pnx: str) -> str:
    import re
    # 1) 백슬래시 → 슬래시
    normalized = pnx.replace("\\", "/")

    # 2) 드라이브 레터 변환 (sample: C:/foo → /mnt/c/foo)
    normalized = re.sub(
        r"^([A-Za-z]):/",
        lambda m: f"/mnt/{m.group(1).lower()}/",
        normalized
    )

    return normalized
