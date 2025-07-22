import toml
import random
import platform
from prompt_toolkit.styles import Style
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.pk_system_object.etc import PK_UNDERLINE

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def get_token_from_f_token(f_token, initial_str):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    generate_token_f(f=f_token, initial_str=initial_str)
    pk_print(working_str=rf'''f_token_nx="{get_nx(f_token)}"  {'%%%FOO%%%' if LTA else ''}''')
    token = get_str_from_txt_f(pnx=f_token)
    token = token.replace("\n", "")
    token = token.strip()
    pk_print(working_str=rf'''token="{token}"  {'%%%FOO%%%' if LTA else ''}''')
    if token == "" or token == "\n":
        pk_print(working_str=rf'''token is empty  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        import ipdb
        ipdb.set_trace()
    return token
