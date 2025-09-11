def is_os_windows():
    import platform

    if platform.system() == 'Windows':
        # if LTA:
        #     ensure_printed_once(f'''windows is detected {'%%%FOO%%%' if LTA else ''}''')
        return 1
    else:
        # if LTA:
        #     ensure_printed_once(f'''windows is not detected {'%%%FOO%%%' if LTA else ''}''')
        return 0
