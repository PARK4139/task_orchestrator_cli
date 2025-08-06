

def get_value_completed_v4(message, option_values):
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import WordCompleter, FuzzyCompleter
    from pkg_py.functions_split.ensure_spoken import ensure_spoken
    from pkg_py.functions_split.is_path_like import is_path_like
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    if message.strip() == "x":
        ensure_spoken(f"{func_n}() exited(intended)")
        return None

    seen = set()
    deduped = []

    for item in option_values:
        # None 값은 건너뛰기
        if item is None:
            continue
        styled = item
        if isinstance(item, str) and is_path_like(item):
            styled = get_pnx_os_style(item)
        if styled not in seen:
            seen.add(styled)
            deduped.append(styled)

    completer = FuzzyCompleter(WordCompleter(deduped, ignore_case=True))

    #  Loop until non-empty input
    while True:
        try:
            user_input = prompt(message + " ", completer=completer).strip()
            if user_input:
                return user_input
            print("️ 입력이 비어 있습니다. 다시 입력해주세요.")
        except (KeyboardInterrupt, EOFError):
            print(" 입력이 취소되었습니다.")
            return None


