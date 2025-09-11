from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_str_from_clipboard():
    from sources.functions.get_text_from_clipboard import get_text_from_clipboard
    # Get-Clipboard  # 클립보드 내용 확인
    return get_text_from_clipboard()
