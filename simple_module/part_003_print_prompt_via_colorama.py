

from enum import Enum

from colorama import Fore
from pkg_py.pk_system_layer_color_map import COLORAMA_CODE_MAP


def print_prompt_via_colorama(prompt: str, colorama_code: Enum, flush, line_feed_mode=1):
    color_code = COLORAMA_CODE_MAP.get(colorama_code, Fore.RESET)
    end_char = '' if line_feed_mode == 0 else '\n'
    print(f"{color_code}{prompt}", end=end_char, flush=flush)
