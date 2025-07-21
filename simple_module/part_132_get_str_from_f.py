from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.simple_module.part_014_pk_print import pk_print


def get_str_from_f(f):
    import os
    import traceback
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    pk_print(f'''f={f}''')

    if f is None:
        return ""

    try:
        if os.path.exists(f):
            # f 읽기
            with open(file=f, mode='r', encoding=Encoding.UTF8.value, errors='ignore') as f:
                content = f.read()  # f 내용을 문자열로 읽기
                if content is None:
                    return ""
                return content
    except:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}" ''', print_color='red')
        return ""
