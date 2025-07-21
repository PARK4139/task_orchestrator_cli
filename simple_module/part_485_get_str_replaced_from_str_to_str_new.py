# import win32process
from tkinter import UNDERLINE
from selenium.webdriver.chrome.options import Options
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from gtts import gTTS
from pkg_py.pk_system_layer_etc import PK_UNDERLINE

from pkg_py.simple_module.part_014_pk_print import pk_print


def get_str_replaced_from_str_to_str_new(item_str, from_str, to_str):
    pk_print(f'''item_str="{item_str}"''')
    pk_print(f'''from_str="{from_str}"''')
    pk_print(f'''to_str="{to_str}"''')
    if not isinstance(item_str, str):
        raise TypeError("item_str must be a string.")
    if not isinstance(from_str, str):
        raise TypeError("from_str must be a string.")
    if not isinstance(to_str, str):
        raise TypeError("to_str must be a string.")
    item_str = item_str.replace(from_str, to_str)
    pk_print(f'''item_str="{item_str}"''')
    return item_str
