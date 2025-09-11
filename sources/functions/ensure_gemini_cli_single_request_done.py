from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_gemini_cli_single_request_done():
    import logging

    from sources.objects.pk_local_test_activate import LTA

    from sources.functions.get_gemini_cli_window_title import get_gemini_cli_window_title

    from sources.functions import ensure_spoken
    from sources.functions.ensure_text_clicked_via_ocr_without_timelimit import \
        ensure_text_clicked_via_ocr_without_timelimit

    from sources.functions import ensure_slept
    from sources.functions.ensure_window_to_front import ensure_window_to_front

    msg = rf"프롬프트 수행시작"
    if not LTA:
        ensure_spoken(msg)
    logging.debug(rf"msg={msg}")

    gemini_cli_window_title = get_gemini_cli_window_title()
    try:
        text = 'Type your message'  # gemini_prompt_done_signiture_text
        if ensure_text_clicked_via_ocr_without_timelimit(text=text):
            ensure_spoken(rf"단일 프롬프트 수행완료.")
            ensure_window_to_front(gemini_cli_window_title)
            ensure_slept(milliseconds=80)
            # ensure_slept(milliseconds=500)
        else:
            ensure_window_to_front(gemini_cli_window_title)
            ensure_slept(milliseconds=80)
    except:
        msg = rf"프롬프트 수행완료 되었습니까?"
        ensure_spoken(msg)
        answer = input(
            "y/n=")  # TODO : GUI 로 ensure_answer_input_via_window_popup(options=[yes, no]) fallback 으로 input() 사용
        if answer.strip().lower() == 'y':
            ensure_spoken(rf"단일 프롬프트 수행완료.")
            ensure_window_to_front(gemini_cli_window_title)
            ensure_slept(milliseconds=80)
