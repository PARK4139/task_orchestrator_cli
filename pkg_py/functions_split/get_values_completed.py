

# import win32gui
# import win32gui
# import pywin32


def get_values_completed(key_hint, values):
    """
    tab_completer_nested_iterable: [
        ['.jpg',  '.jpeg', '.png',  '.webp', '.jfif'],
        ['mp4',   'mkv',   'avi']
    ]
    반환: 사용자가 선택한 하위 리스트 (sample: ['mp4','mkv','avi'])
    """
    # lazy import
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import WordCompleter
    from prompt_toolkit.shortcuts import CompleteStyle

    # 1) 리스트 전체를 문자열로 표시할 후보 준비
    display_map = {str(lst): lst for lst in values}
    candidates = list(display_map.keys())

    completer = WordCompleter(
        candidates,
        ignore_case=True,
        match_middle=True,
    )

    chosen = prompt(
        key_hint,
        completer=completer,
        complete_while_typing=True,
        complete_style=CompleteStyle.COLUMN,
    ).strip()

    # 2) 선택한 문자열에 대응하는 실제 리스트 반환
    return display_map.get(chosen, [])
