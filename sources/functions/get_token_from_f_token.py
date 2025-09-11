import toml
import random
import platform
from prompt_toolkit.styles import Style
import logging
from sources.functions.get_nx import get_nx
from sources.objects.pk_etc import PK_UNDERLINE

from sources.objects.pk_local_test_activate import LTA
import logging


def get_token_from_f_token(f_token, initial_str):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    ensure_token_file_generated(f=f_token, initial_str=initial_str)
    logging.debug(rf'''f_token_nx="{get_nx(f_token)}"  {'%%%FOO%%%' if LTA else ''}''')
    token = get_str_from_file(pnx=f_token)
    token = token.replace("\n", "")
    token = token.strip()
    logging.debug(rf'''token="{token}"  {'%%%FOO%%%' if LTA else ''}''')
    if token == "" or token == "\n":
        logging.debug(rf'''token is empty  {'%%%FOO%%%' if LTA else ''}''')
        import ipdb
        ipdb.set_trace()
    return token
