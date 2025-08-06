



from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


def kill_chrome_tab(url_to_close):
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    window_titles = get_window_titles()
    loop_limit = 50
    for window_title_seg in window_titles:
        if "chrome".lower() in window_title_seg.lower():
            ensure_printed(str_working=rf'''window_title="{window_title_seg}"  {'%%%FOO%%%' if LTA else ''}''')
            loop_cnt = 0
            while 1:
                ensure_window_to_front(window_title_seg=window_title_seg)
                if loop_cnt == loop_limit:
                    break
                loop_cnt = loop_cnt + 1
                ensure_slept(milliseconds=15)
                ensure_pressed("ctrl", "l")
                ensure_slept(milliseconds=15)
                url_dragged = get_text_dragged()
                if url_dragged == url_to_close:
                    ensure_printed(str_working=rf'''url_to_close="{url_to_close}"  {'%%%FOO%%%' if LTA else ''}''')
                    ensure_printed(str_working=rf'''url_dragged="{url_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
                    ensure_pressed("ctrl", "w")
                    # restore_all_windows()
                    return
