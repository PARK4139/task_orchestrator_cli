

def is_os_windows():
    import platform
    from pkg_py.pk_system_layer_100_Local_test_activate import LTA
    from pkg_py.simple_module.part_016_pk_print_once import pk_print_once

    if platform.system() == 'Windows':
        if LTA:
            pk_print_once(f'''windows is detected {'%%%FOO%%%' if LTA else ''}''')
        return 1
    else:
        if LTA:
            pk_print_once(f'''windows is not detected {'%%%FOO%%%' if LTA else ''}''')
        return 0
