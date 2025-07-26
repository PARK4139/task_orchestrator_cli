import sys

from pkg_py.functions_split.copy import copy
from pkg_py.functions_split.paste import paste





venv_arg = sys.argv[1] if len(sys.argv) > 1 else None
if venv_arg:
    pk_copy(venv_arg)
    pk_paste()
