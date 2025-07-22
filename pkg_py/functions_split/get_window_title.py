def get_window_title(window_title_seg):
    from pkg_py.functions_split.get_set_from_list import get_set_from_list
    from pkg_py.functions_split.get_window_title_list import get_window_title_list

    window_title_list = get_window_title_list()
    window_title_set = get_set_from_list(window_title_list)
    for window_title in window_title_set:
        # if window_title_seg in window_title: # pk_option
        if window_title_seg == window_title:
            return window_title
