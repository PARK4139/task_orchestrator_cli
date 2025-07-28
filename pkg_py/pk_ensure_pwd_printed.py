from pkg_py.functions_split.get_d_working_in_python import get_pwd_in_python
from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once

ensure_colorama_initialized_once()
pwd = get_pwd_in_python()
print(pwd)
