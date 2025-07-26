def get_list_from_f(f):
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.encodings import Encoding
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style

    import os
    import traceback

    f = get_pnx_os_style(f)
    ensure_printed(f'''f={f}''')

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
        ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}" ''', print_color='red')
