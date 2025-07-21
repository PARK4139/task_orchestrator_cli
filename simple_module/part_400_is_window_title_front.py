from pkg_py.simple_module.part_401_get_front_window_title import get_front_window_title


def is_window_title_front(window_title):
    """탐색기창을 필터하기 위해서 만든 함수"""
    front_window_title = get_front_window_title()
    # pk_print(f'''window_title={window_title}  {'%%%FOO%%%' if LTA else ''}''',print_color="blue")
    # pk_print(f'''front_window_title={front_window_title}  {'%%%FOO%%%' if LTA else ''}''',print_color="blue")
    # pk_print(f'''len(window_title)={len(window_title)}  {'%%%FOO%%%' if LTA else ''}''',print_color="blue")
    # pk_print(f'''len(front_window_title)={len(front_window_title)}  {'%%%FOO%%%' if LTA else ''}''',print_color="blue")
    if not front_window_title is None:
        if window_title == front_window_title:
            return 1
    return 0
