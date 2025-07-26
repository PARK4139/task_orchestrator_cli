import toml
import random
import platform
from prompt_toolkit.styles import Style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.etc import PK_UNDERLINE

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def get_token_from_f_token(f_token, initial_str):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    generate_token_f(f=f_token, initial_str=initial_str)
    ensure_printed(str_working=rf'''f_token_nx="{get_nx(f_token)}"  {'%%%FOO%%%' if LTA else ''}''')
    token = get_str_from_txt_f(pnx=f_token)
    token = token.replace("\n", "")
    token = token.strip()
    ensure_printed(str_working=rf'''token="{token}"  {'%%%FOO%%%' if LTA else ''}''')
    if token == "" or token == "\n":
        ensure_printed(str_working=rf'''token is empty  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        import ipdb
        ipdb.set_trace()
    return token
