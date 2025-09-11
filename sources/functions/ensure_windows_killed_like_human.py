import logging

from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_windows_killed_like_human(window_title):
    # ensure_process_killed_by_window_title 보다 나은 느낌은 들었음. 검증필요
    from sources.functions import ensure_slept
    from sources.functions.ensure_pressed import ensure_pressed
    from sources.functions.ensure_window_to_front import ensure_window_to_front
    from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
    from sources.functions.is_window_title_front import is_window_title_front

    while 1:
        if not is_window_opened_via_window_title(window_title):
            logging.debug(f'{window_title} 가 없습니다')
            break
        ensure_window_to_front(window_title)
        ensure_slept(milliseconds=80)
        if is_window_title_front(window_title):
            ensure_pressed("alt", "f4")
            logging.debug(f'창 닫기를 시도했습니다')
        else:
            logging.debug(f'{window_title}이 앞에 있지 않아 창 닫기를 시도하지 않았습니다.')
