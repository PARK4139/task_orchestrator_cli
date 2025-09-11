from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_target_enabled(editor, target, mode="sync"):
    from sources.functions.ensure_window_maximized_like_human import ensure_window_maximized_like_human

    from pathlib import Path

    import logging

    from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
    from sources.functions.ensure_window_to_front import ensure_window_to_front
    from sources.functions.get_execute_cmd_with_brakets import get_cmd_chains
    from sources.functions.get_nx import get_nx

    from sources.functions.ensure_command_executed import ensure_command_executed
    for _ in [editor, target]:
        _ = Path(_)
        if not _.exists():
            logging.debug(rf"{_} is not existing")
            return
    if not is_window_opened_via_window_title(get_nx(target)):
        ensure_command_executed(cmd=f'start "" {get_cmd_chains(editor, target)}', mode=mode)
    # ensure_window_to_front(get_nx(target))
    # ensure_pressed("win", "up")
    # ensure_pressed("f11")
    # ensure_window_maximized_like_human()
