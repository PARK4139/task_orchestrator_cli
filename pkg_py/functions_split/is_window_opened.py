def is_window_opened(window_title_seg):
    from pkg_py.functions_split.get_list_without_none import get_list_without_none
    from pkg_py.system_object.gui_util import get_windows_opened
    windows_titles_opened = get_windows_opened()
    windows_titles_opened = get_list_without_none(working_list=windows_titles_opened)

    # print_list_as_vertical(working_list=windows_titles_opened,working_list_n="windows_titles_opened")

    for windows_title_opened in windows_titles_opened:
        if window_title_seg in windows_title_opened:
            # ensure_printed(f'''{windows_title_opened}" 창이 열려 있습니다''')
            return 1
    # ensure_printed(f'''{window_title_seg}" 창이 닫혀 있습니다''')
    return 0
