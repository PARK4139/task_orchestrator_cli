from enum import Enum

from colorama import Fore


class ColormaColorMap(Enum):
    RED = 'red'
    GREEN = "GREEN"
    BLACK = "BLACK"
    YELLOW = "YELLOW"
    BLUE = "BLUE"
    MAGENTA = "MAGENTA"
    CYAN = "CYAN"
    WHITE = "WHITE"
    RESET = "RESET"
    LIGHTBLACK_EX = "LIGHTBLACK_EX"
    LIGHTRED_EX = "LIGHTRED_EX"
    LIGHTGREEN_EX = "LIGHTGREEN_EX"
    LIGHTYELLOW_EX = "LIGHTYELLOW_EX"
    LIGHTBLUE_EX = "LIGHTBLUE_EX"
    LIGHTMAGENTA_EX = "LIGHTMAGENTA_EX"
    LIGHTCYAN_EX = "LIGHTCYAN_EX"
    LIGHTWHITE_EX = "LIGHTWHITE_EX"


COLORAMA_CODE_MAP = {
    ColormaColorMap.BLACK: Fore.BLACK,
    ColormaColorMap.RED: Fore.RED,
    ColormaColorMap.GREEN: Fore.GREEN,
    ColormaColorMap.YELLOW: Fore.YELLOW,
    ColormaColorMap.BLUE: Fore.BLUE,
    ColormaColorMap.MAGENTA: Fore.MAGENTA,
    ColormaColorMap.CYAN: Fore.CYAN,
    ColormaColorMap.WHITE: Fore.WHITE,
    ColormaColorMap.RESET: Fore.RESET,
    ColormaColorMap.LIGHTBLACK_EX: Fore.LIGHTBLACK_EX,
    ColormaColorMap.LIGHTRED_EX: Fore.LIGHTRED_EX,
    ColormaColorMap.LIGHTGREEN_EX: Fore.LIGHTGREEN_EX,
    ColormaColorMap.LIGHTYELLOW_EX: Fore.LIGHTYELLOW_EX,
    ColormaColorMap.LIGHTBLUE_EX: Fore.LIGHTBLUE_EX,
    ColormaColorMap.LIGHTMAGENTA_EX: Fore.LIGHTMAGENTA_EX,
    ColormaColorMap.LIGHTCYAN_EX: Fore.LIGHTCYAN_EX,
    ColormaColorMap.LIGHTWHITE_EX: Fore.LIGHTWHITE_EX,
}


# dict가 보통 20~30% 더 빠름, class 보다
PK_ANSI_COLOR_MAP = {
    'RED': "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m",
    "GREY": "\033[90m",
    "BRIGHT_BLACK": "\033[90m",
    "BRIGHT_RED": "\033[91m",
    "BRIGHT_GREEN": "\033[92m",
    "BRIGHT_YELLOW": "\033[93m",
    "BRIGHT_BLUE": "\033[94m",
    "BRIGHT_MAGENTA": "\033[95m",
    "BRIGHT_CYAN": "\033[96m",
    "BRIGHT_WHITE": "\033[97m",
    "RESET_CODE": "\033[0m",
    "BLACK": "\033[30m",
    "RESET": "\033[0m",
}
ANSI_COLOR_MAP = PK_ANSI_COLOR_MAP

RESET_COLOR = "\033[0m"
