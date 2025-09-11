from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.functions.get_nx import get_nx


@ensure_seconds_measured
def ensure_command_executed_like_human(text, __file__):
    # todo : return 에 대해서 개선필요
    from sources.functions.ensure_window_title_replaced import ensure_window_title_replaced

    from sources.functions.run_cmd_exe import ensure_cmd_exe_executed
    from sources.functions import ensure_slept
    from sources.functions.ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard import \
        ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard
    from sources.functions.ensure_pressed import ensure_pressed
    from sources.functions.ensure_window_to_front import ensure_window_to_front

    ensure_window_title_replaced(rf"{get_nx(__file__)}_child_process")

    ensure_cmd_exe_executed()
    ensure_slept(milliseconds=80)

    window_title_seg = rf'cmd.exe'
    ensure_window_to_front(window_title_seg)
    ensure_slept(milliseconds=80)

    ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard(text=text)
    ensure_slept(milliseconds=80)
    ensure_pressed("enter")
    # std_str = get_str_from_clipboard()
