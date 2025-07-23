def is_window_title_opened(window_title):
    from pkg_py.pk_system_object.local_test_activate import LTA
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.functions_split.get_list_without_none import get_list_without_none
    from pkg_py.pk_interface_graphic_user import get_windows_opened

    window_titles_opened = get_windows_opened()
    window_titles_opened = get_list_without_none(working_list=window_titles_opened)
    for window_title_opened in window_titles_opened:
        if window_title != window_title_opened:
            continue
        if window_title == window_title_opened:
            if LTA:
                pk_print(f'''window_title={window_title}  {'%%%FOO%%%' if LTA else ''}''')
                pk_print(f'''window_title_opened={window_title_opened}  {'%%%FOO%%%' if LTA else ''}''')
            return 1
    return 0
