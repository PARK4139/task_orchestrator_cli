from pkg_py.functions_split.get_d_working_in_python import get_pwd_in_python
from pkg_py.functions_split.colorama_init_once import colorama_init_once


colorama_init_once()

pwd = get_pwd_in_python()
print(pwd)
