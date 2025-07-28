from pkg_py.functions_split.ensure_pasted import ensure_pasted


def get_str_from_clipboard():
    # Get-Clipboard  # 클립보드 내용 확인
    return ensure_pasted()
