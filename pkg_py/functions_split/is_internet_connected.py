def is_internet_connected():
    from pkg_py.functions_split.ping import ping
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.pk_system_object.local_test_activate import LTA
    if not ping(ip='8.8.8.8'):  # google.com DNS
        pk_print(f'''internet not connected. {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return True
    pk_print(f'''internet is connected. {'%%%FOO%%%' if LTA else ''}''', print_color='green')
    return False
