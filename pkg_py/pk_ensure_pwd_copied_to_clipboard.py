from pkg_py.functions_split.get_d_working_in_python import get_pwd_in_python
from pkg_py.functions_split.colorama_init_once import colorama_init_once
from pkg_py.functions_split.copy import copy
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.local_test_activate import LTA

colorama_init_once()

pwd = get_pwd_in_python()
pk_copy(pwd)
ensure_printed(f'''pwd={pwd} {'%%%FOO%%%' if LTA else ''}''')
