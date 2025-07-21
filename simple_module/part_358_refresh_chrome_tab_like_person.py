from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front


def refresh_chrome_tab_like_person(url_to_close):
    import inspect
    import time

    func_n = inspect.currentframe().f_code.co_name
    # minimize_all_windows()
    # window_title_seg=get_window_title(window_title_seg="Chrome")
    window_titles = get_window_title_list()

    time_limit_seconds = 10
    time_s = time.time()
    for window_title_seg in window_titles:
        if "chrome".lower() in window_title_seg.lower():
            if time_limit_seconds == 50:
                pk_print(working_str=rf'''window_title="{window_title_seg}"  {'%%%FOO%%%' if LTA else ''}''')
            while 1:
                elapsed_time = time.time() - time_s
                if elapsed_time > time_limit_seconds:
                    break
                ensure_window_to_front(window_title_seg=window_title_seg)
                pk_sleep(milliseconds=15)
                pk_press("ctrl", "l")
                pk_sleep(milliseconds=15)
                url_dragged = get_txt_dragged()
                if url_dragged == url_to_close:
                    pk_print(working_str=rf'''url_to_close="{url_to_close}"  {'%%%FOO%%%' if LTA else ''}''')
                    pk_print(working_str=rf'''url_dragged="{url_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
                    pk_press("f5")
                    # restore_all_windows()
                    return
