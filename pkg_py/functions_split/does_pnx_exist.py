def does_pnx_exist(pnx=None, nx=None):
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_pnx_list import get_pnx_list
    from pkg_py.functions_split.get_d_working import get_d_working
    import os
    # if LTA:
        # ensure_printed(f'''pnx={pnx} {'%%%FOO%%%' if LTA else ''}''')
    # pnx = get_pnx_os_style(pnx)
    if not pnx:
        if not nx:
            ensure_printed(f'''해당 함수는 pnx nx 둘 중 하나만 설정되어야합니다. {'%%%FOO%%%' if LTA else ''}''', print_color='red')
    if pnx:
        if os.path.exists(pnx):
            return 1
        else:
            # ensure_printed(f'''{pnx}  {'%%%FOO%%%' if LTA else ''} ''')
            return 0
    if nx:
        if pnx in get_pnx_list(d_working=get_d_working(), with_walking=0):
            if nx not in pnx:
                return 0
