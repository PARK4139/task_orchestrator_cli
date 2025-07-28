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
            # 먼저 UTF-8로 시도
            try:
                with open(file=f, mode='r', encoding=Encoding.UTF8.value, errors='ignore') as f_obj:
                    lines = f_obj.readlines()
                    if lines is None:
                        return []
                    return lines
            except UnicodeDecodeError:
                # UTF-8 실패 시 UTF-16으로 시도
                try:
                    with open(file=f, mode='r', encoding='utf-16', errors='ignore') as f_obj:
                        lines = f_obj.readlines()
                        if lines is None:
                            return []
                        return lines
                except UnicodeDecodeError:
                    # UTF-16도 실패 시 cp949로 시도
                    with open(file=f, mode='r', encoding='cp949', errors='ignore') as f_obj:
                        lines = f_obj.readlines()
                        if lines is None:
                            return []
                        return lines
    except:
        ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}" ''', print_color='red')
        return []
