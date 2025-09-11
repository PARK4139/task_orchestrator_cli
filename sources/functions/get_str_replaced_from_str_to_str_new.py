
from tkinter import UNDERLINE
from selenium.webdriver.chrome.options import Options

from sources.functions.does_pnx_exist import is_pnx_existing
import logging
from sources.functions.set_pk_context_state import set_pk_context_state
from gtts import gTTS
from sources.objects.pk_etc import PK_UNDERLINE

import logging


def get_str_replaced_from_str_to_str_new(item_str, from_str, to_str):
    logging.debug(f'''item_str="{item_str}"''')
    logging.debug(f'''from_str="{from_str}"''')
    logging.debug(f'''to_str="{to_str}"''')
    if not isinstance(item_str, str):
        raise TypeError("item_str must be a string.")
    if not isinstance(from_str, str):
        raise TypeError("from_str must be a string.")
    if not isinstance(to_str, str):
        raise TypeError("to_str must be a string.")
    item_str = item_str.replace(from_str, to_str)
    logging.debug(f'''item_str="{item_str}"''')
    return item_str
