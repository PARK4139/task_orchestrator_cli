import sys

from pkg_py.functions_split.ensure_copied import ensure_copied
from pkg_py.functions_split.ensure_pasted import ensure_pasted

venv_arg = sys.argv[1] if len(sys.argv) > 1 else None
if venv_arg:
    ensure_copied(venv_arg)
    ensure_pasted()
