def get_list_from_f(f):
    from pkg_py.pk_system_layer_100_Local_test_activate import LTA
    from pkg_py.pk_system_layer_encodings import Encoding
    from pkg_py.simple_module.part_014_pk_print import pk_print
    from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style

    import os
    import traceback

    f = get_pnx_os_style(f)
    pk_print(f'''f={f}''')

    if f is None:
        return []

    try:
        if os.path.exists(f):
            # with open(file=f,mode= 'r', encoding=Encoding.UTF8.value) as f:
            # with open(file=f, 'r', errors='ignore') as f:
            with open(file=f, mode='r', encoding=Encoding.UTF8.value, errors='ignore') as f:
                lines = f.readlines()  # from file.ext to ["한줄","한줄","한줄"]
                # mkr_f 내용을 디스크에 강제로 기록
                # os.fsync(f.fileno())
                if lines is None:
                    return []
                return lines
    except:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}" ''', print_color='red')
