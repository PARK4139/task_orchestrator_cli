from sources.objects.pk_local_test_activate import LTA
from sources.objects.encodings import Encoding
import logging


def get_str_from_f(f):
    import os
    import traceback
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    logging.debug(f'''f={f}''')

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
        logging.debug(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}" ''')
        return ""
