from functions.get_window_title_temp_for_cmd_exe import get_window_title_temp_for_cmd_exe
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_command_executed_like_human(cmd) -> None:
    # todo : return 할수 있도록 할수 있을까?
    from functions.run_cmd_exe import _SetupOps

    from sources.functions.run_cmd_exe import ensure_cmd_exe_executed
    from sources.functions import ensure_slept
    from sources.functions.ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard import \
        ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard
    from sources.functions.ensure_pressed import ensure_pressed
    from sources.functions.ensure_window_to_front import ensure_window_to_front

    # ensure_window_title_replaced(custom_title)

    custom_title = get_window_title_temp_for_cmd_exe()
    ensure_cmd_exe_executed(setup_op=_SetupOps.CUSTOM_TITLE, custom_title=custom_title)
    ensure_slept(milliseconds=80)

    ensure_window_to_front(window_title_seg=custom_title)
    ensure_slept(milliseconds=80)

    ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard(text=cmd)
    ensure_slept(milliseconds=80)
    ensure_pressed("enter")
