from pkg_py.functions_split.pk_paste import pk_paste


def get_str_from_clipboard():
    # Get-Clipboard  # 클립보드 내용 확인
    return pk_paste()
