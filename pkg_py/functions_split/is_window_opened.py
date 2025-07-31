# def is_window_opened(window_title_seg):
#     from pkg_py.functions_split.get_windows_opened import get_windows_opened
#     from pkg_py.functions_split.get_list_without_none import get_list_without_none
#     windows_titles_opened = get_windows_opened()
#     windows_titles_opened = get_list_without_none(working_list=windows_titles_opened)
#
#     # print_list_as_vertical(working_list=windows_titles_opened, working_list_n="windows_titles_opened")
#
#     for windows_title_opened in windows_titles_opened:
#         if window_title_seg in windows_title_opened:
#             # ensure_printed(f'''{windows_title_opened}" 창이 열려 있습니다''')
#             return 1
#     # ensure_printed(f'''{window_title_seg}" 창이 닫혀 있습니다''')
#     return 0


def is_window_opened(window_title_seg):
    import inspect

    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_list_removed_none import get_list_removed_none
    from pkg_py.functions_split.get_windows_opened import get_windows_opened
    from pkg_py.system_object.local_test_activate import LTA
    func_n = inspect.currentframe().f_code.co_name
    if LTA:
        ensure_printed(str_working=rf'''%%%FOO%%%''')

    windows_titles_opened = get_windows_opened()
    windows_titles_opened = get_list_removed_none(items=windows_titles_opened)

    for windows_title_opened in windows_titles_opened:
        if LTA:
            # ensure_printed(rf'''windows_title_opened="{windows_title_opened}" %%%FOO%%%''') # pk_option
            pass
        if window_title_seg in windows_title_opened:
            if LTA:
                ensure_printed(f'''"windows_title_opened={windows_title_opened}" 창이 열려 있습니다''')
            return True
    if LTA:
        ensure_printed(f'''"{window_title_seg}" 창이 닫혀 있습니다''')
    return False
