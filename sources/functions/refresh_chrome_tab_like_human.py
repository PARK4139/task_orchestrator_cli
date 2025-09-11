from sources.functions.ensure_window_to_front import ensure_window_to_front

import logging
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_window_to_front import ensure_window_to_front


def refresh_chrome_tab_like_human(url_to_close):
    import inspect
    import time

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    # ensure_windows_minimized()
    # window_title_seg=get_window_title(window_title_seg="Chrome")
    window_titles = get_window_titles()

    time_limit_seconds = 10
    time_s = time.time()
    for window_title_seg in window_titles:
        if "chrome".lower() in window_title_seg.lower():
            if time_limit_seconds == 50:
                logging.debug(rf'''window_title="{window_title_seg}"  {'%%%FOO%%%' if LTA else ''}''')
            while 1:
                elapsed_time = time.time() - time_s
                if elapsed_time > time_limit_seconds:
                    break
                ensure_window_to_front(window_title_seg)
                ensure_slept(milliseconds=15)
                ensure_pressed("ctrl", "l")
                ensure_slept(milliseconds=15)
                url_dragged = get_txt_dragged()
                if url_dragged == url_to_close:
                    logging.debug(rf'''url_to_close="{url_to_close}"  {'%%%FOO%%%' if LTA else ''}''')
                    logging.debug(rf'''url_dragged="{url_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
                    ensure_pressed("f5")
                    # restore_all_windows()
                    return
