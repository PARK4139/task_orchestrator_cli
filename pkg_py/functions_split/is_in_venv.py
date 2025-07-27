from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025


def is_in_venv():
    from pkg_py.functions_split.ensure_printed import ensure_printed
    import os
    import sys
    if "VIRTUAL_ENV" in os.environ:
        ensure_printed(f'''[{PkMessages2025.DATA}] venv is activated {'%%%FOO%%%' if LTA else ''}''')
        some_condition = 1
        print(some_condition)
        sys.exit(0)  # %errorlevel%=0  # 성공
    else:
        ensure_printed(f'''[{PkMessages2025.DATA}] venv is not activated {'%%%FOO%%%' if LTA else ''}''')
        some_condition = 0
        print(some_condition)
        sys.exit(1)  # %errorlevel%=1  # 실패`