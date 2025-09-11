from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_gemini_cli_enabled_interactive(__file__):
    from functions import ensure_slept, ensure_spoken
    from functions.ensure_gemini_cli_installed_for_one_session import ensure_gemini_cli_installed_for_one_session
    from functions.is_gemini_installed import is_gemini_installed
    from functions.is_window_opened_via_window_title import is_window_opened_via_window_title
    from sources.functions.ensure_gemini_cli_opened import ensure_gemini_cli_opened
    from sources.functions.ensure_gemini_cli_requests_processed_legacy import ensure_gemini_cli_requests_processed_legacy
    from sources.functions.ensure_window_maximized_like_human import ensure_window_maximized_like_human
    from sources.functions.ensure_window_to_front import ensure_window_to_front
    from sources.functions.get_gemini_cli_window_title import get_gemini_cli_window_title
    from sources.functions.get_gemini_prompt_starting import get_gemini_prompt_starting
    from sources.functions.is_gemini_opened import is_gemini_opened

    opened = is_gemini_opened()
    installed = is_gemini_installed()

    if not installed:
        ensure_gemini_cli_installed_for_one_session(installed)
        ensure_slept(seconds=60)

    if not opened:
        ensure_gemini_cli_opened(__file__=__file__, opened=opened)
        ensure_spoken(f'gemini 에게 스타팅 프롬프트 요청 시작')
        # ensure_slept(milliseconds=1000) # 실패 거의 없었음. # 이벤트로 만들 방법을 못찾음
        ensure_slept(milliseconds=500)
        ensure_gemini_cli_requests_processed_legacy([get_gemini_prompt_starting()])
        ensure_slept(milliseconds=80)
        ensure_slept(milliseconds=80)
        # ensure_slept(milliseconds=80)
    else:
        gemini_cli_window_title = get_gemini_cli_window_title()
        if is_window_opened_via_window_title(gemini_cli_window_title):
            ensure_spoken(f'gemini 가 이미 실행중입니다.')
            ensure_window_to_front(gemini_cli_window_title)
            ensure_window_maximized_like_human()
            ensure_spoken(f'', wait=True)
            return
