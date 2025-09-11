from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_gemini_auth_chrome_window_detected():
    import traceback

    from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose

    from functions import ensure_slept, ensure_spoken
    from functions.ensure_drag_changed_printed import get_txt_dragged
    from functions.ensure_pressed import ensure_pressed
    from functions.ensure_window_to_front import ensure_window_to_front

    try:
        ensure_window_to_front(window_title_seg="Chrome")
        ensure_pressed("ctrl", "l")
        ensure_slept(milliseconds=80)
        url = get_txt_dragged()
        reference = "https://developers.google.com/gemini-code-assist/auth"
        if reference in url:
            ensure_spoken("크롬 제미나이 로그인인증창 탐지 되었습니다")
            return True
        else:
            ensure_spoken("크롬 제미나이 로그인인증창 미탐지 되었습니다")
            return False
    except:
        ensure_debug_loged_verbose(traceback)
    finally:
        ensure_spoken(wait=True)
