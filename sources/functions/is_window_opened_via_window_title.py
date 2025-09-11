# @ensure_seconds_measured
def is_window_opened_via_window_title(window_title):
    import logging
    from sources.objects.pk_local_test_activate import LTA
    from sources.functions.get_list_without_none import get_list_without_none
    from sources.functions.get_windows_opened_with_hwnd import get_windows_opened_with_hwnd
    from sources.functions.log_aligned import log_aligned

    titles = get_windows_opened_with_hwnd()
    titles = get_list_without_none(working_list=titles)
    logging.debug(f'''window_title={window_title} len(window_title)={len(window_title)}{'%%%FOO%%%' if LTA else ''}''')
    msg_to_print = []
    for title, _ in titles:
        # logging.debug(f'''window_title == title={window_title == title} len(title)={len(title)} title={title} {'%%%FOO%%%' if LTA else ''}''')
        operator_literal = " 같다 " if len(window_title) == len(title) else " 다르다 "
        key = f"'{window_title}' 와 '{title}' 길이비교결과"
        value = rf"{len(window_title)}와 {len(title)}는 {operator_literal}"
        # gap = len(key) + len(title) + 2
        # gap = 100
        # gap = 100
        gap = 1
        log_aligned(key=key, value=value, gap=gap, seperator='')  # 너무 많은 로그를 생성하여 주석 처리
        if window_title == title:
            logging.debug(f"Window found: '{title}'")
            return 1
        elif window_title != title:
            msg_to_print.append(())
            continue
    logging.debug(f'''{window_title} is not opened {'%%%FOO%%%' if LTA else ''}''')
    for title, _ in titles:
        logging.debug(f'''title={title} {'%%%FOO%%%' if LTA else ''}''')
    return 0
