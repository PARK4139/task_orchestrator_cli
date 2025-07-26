

def is_os_windows():
    import platform
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.ensure_printed_once import ensure_printed_once

    if platform.system() == 'Windows':
        # if LTA:
        #     ensure_printed_once(f'''windows is detected {'%%%FOO%%%' if LTA else ''}''')
        return 1
    else:
        # if LTA:
        #     ensure_printed_once(f'''windows is not detected {'%%%FOO%%%' if LTA else ''}''')
        return 0
