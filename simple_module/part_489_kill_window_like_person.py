from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front


def kill_window_like_person(window_title_seg):
    pk_print(f'''window_title_seg="{window_title_seg}"''')
    pk_print(
        f'''window_title_seg == is_front_window_title(window_title_seg=window_title_seg)="{window_title_seg == is_front_window_title(window_title_seg=window_title_seg)}"''')
    while 1:
        if not is_front_window_title(window_title_seg=window_title_seg):
            ensure_window_to_front(window_title_seg=window_title_seg)
        if is_front_window_title(window_title_seg=window_title_seg):
            pk_press("alt", "f4")
        if not is_window_opened(window_title_seg=window_title_seg):
            pk_print(f'''  {'%%%FOO%%%' if LTA else ''}" {window_title_seg} 창를 닫았습니다''', print_color='blue')
            return
