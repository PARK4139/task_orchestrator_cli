from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front


def kill_chrome_tab_like_person(url_to_kill):
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    window_titles = get_window_title_list()
    loop_limit = 50
    for window_title_seg in window_titles:
        if "chrome".lower() in window_title_seg.lower():
            pk_print(working_str=rf'''window_title="{window_title_seg}"  {'%%%FOO%%%' if LTA else ''}''')
            loop_cnt = 0
            while 1:
                ensure_window_to_front(window_title_seg=window_title_seg)
                if loop_cnt == loop_limit:
                    break
                loop_cnt = loop_cnt + 1
                pk_sleep(milliseconds=15)
                pk_press("ctrl", "l")
                pk_sleep(milliseconds=15)
                url_dragged = get_txt_dragged()
                if url_dragged == url_to_kill:
                    pk_print(working_str=rf'''url_to_close="{url_to_kill}"  {'%%%FOO%%%' if LTA else ''}''')
                    pk_print(working_str=rf'''url_dragged="{url_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
                    pk_press("ctrl", "w")
                    # restore_all_windows()
                    return
