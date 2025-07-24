from pkg_py.functions_split.get_d_working_in_python import get_pwd_in_python
from pkg_py.functions_split.pk_colorama_init_once import pk_colorama_init_once
from pkg_py.functions_split.pk_copy import pk_copy
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.system_object.local_test_activate import LTA

pk_colorama_init_once()

pwd = get_pwd_in_python()
pk_copy(pwd)
pk_print(f'''pwd={pwd} {'%%%FOO%%%' if LTA else ''}''')
