from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_gemini_cli_opened(__file__, opened=None):
    import time
    import traceback

    from functions.ensure_spoken import ensure_spoken
    from functions.ensure_console_paused import ensure_console_paused
    from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
    from functions.ensure_gemini_auth_chrome_window_detected import ensure_gemini_auth_chrome_window_detected

    from sources.functions.ensure_window_to_front import ensure_window_to_front
    from sources.functions.get_gemini_cli_window_title import get_gemini_cli_window_title
    from sources.functions.is_gemini_opened import is_gemini_opened

    from sources.functions import ensure_slept
    from sources.functions.ensure_command_executed_like_human import ensure_command_executed_like_human

    try:
        if opened is None:
            opened = is_gemini_opened()

        if not opened:
            ensure_command_executed_like_human("gemini", __file__)
            # ensure_slept(seconds=3)

            # pk_* : time limit loop
            time_seconds_limit = 3000
            time_s = time.time()
            while True:
                elapsed = time.time() - time_s
                if elapsed > time_seconds_limit:
                    ensure_spoken("크롬 제미나이 로그인인증창 미탐지 간주")
                    break
                if ensure_gemini_auth_chrome_window_detected():
                    ensure_spoken("로그인 버튼을 눌러주세요")
                    ensure_console_paused()
                    break
                else:
                    break
                ensure_slept(milliseconds=80)
        else:
            gemini_cli_window_title = get_gemini_cli_window_title()
            ensure_window_to_front(gemini_cli_window_title)
            ensure_slept(milliseconds=80)
    except:
        ensure_debug_loged_verbose(traceback)
    finally:
        ensure_spoken(wait=True)
