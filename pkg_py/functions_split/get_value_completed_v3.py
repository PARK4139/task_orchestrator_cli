
from pkg_py.functions_split.ensure_pk_system_exit_silent import ensure_pk_system_exit_silent
from pkg_py.functions_split.pk_measure_seconds import pk_measure_seconds


@pk_measure_seconds
def get_value_completed_v3(message, options):
    from pkg_py.pk_system_object.map_massages import PkMessages2025
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.pk_speak import pk_speak
    from pkg_py.functions_split.is_path_like import is_path_like


    from prompt_toolkit import prompt
    from prompt_toolkit.completion import WordCompleter, FuzzyCompleter
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    if message.strip() == "x":
        pk_speak(f"{func_n}() exited(intended)")
        return None

    seen = set()
    deduped = []
    options = options + [PkMessages2025.SHUTDOWN]
    for option in options:
        styled = option
        if isinstance(option, str):
            if is_path_like(option):
                styled = get_pnx_os_style(option)
        if styled not in seen:
            seen.add(styled)
            deduped.append(styled)

    # fzf 스타일 실시간 검색 완성 기능
    completer = FuzzyCompleter(WordCompleter(deduped, ignore_case=True))
    option_selected = prompt(message + " ", completer=completer)
    if option_selected.strip() == PkMessages2025.SHUTDOWN:
        ensure_pk_system_exit_silent()
        return
    return option_selected
