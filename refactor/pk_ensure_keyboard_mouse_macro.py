part_742_ensure_vpc_os_poweroff
import inspect
import logging
import os
import time

import pyautogui

from pkg_py.pk_paste_as_auto import pk_copy
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_color_map import PK_ANSI_COLOR_MAP
from pkg_py.pk_system_layer_directories import D_DESKTOP
from pkg_py.simple_module.ensure_elapsed_time_logged import ensure_elapsed_time_logged
from pkg_py.simple_module.ensure_pk_system_exit_silent import ensure_pk_system_exit_silent
from pkg_py.simple_module.ensure_start_time_logged import ensure_start_time_logged
from pkg_py.simple_module.get_file_id import get_file_id
from pkg_py.simple_module.get_value_by_file_id import get_value_by_file_id
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_132_get_str_from_f import get_str_from_f
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.pk_ensure_loop_delayed_at_loop_foot import pk_ensure_loop_delayed_at_loop_foot
from pkg_py.simple_module.pk_initialize_and_customize_logging_config import pk_initialize_and_customize_logging_config
from pkg_py.simple_module.pk_type import pk_type
from pkg_py.workspace import pk_ensure_keyboard_mouse_macro


class PkMacroRoutines:
    ENSURE_PYCHARM_CODE_OPTIMIZED = None  # for auto-completion

    _localized_texts = {
        "ENSURE_PYCHARM_CODE_OPTIMIZED": {"kr": "PyCharm 코드 최적화", "en": "Optimize PyCharm Code"}
    }

    @classmethod
    def set_lang(cls, lang: str):
        if lang not in ('kr', 'en'):
            raise ValueError(f"Unsupported language: {lang}")
        for key, val in cls._localized_texts.items():
            setattr(cls, key, val.get(lang, f"[{key}]"))


PkMacroRoutines.set_lang("kr")

if __name__ == "__main__":
    pk_initialize_and_customize_logging_config(__file__)
    pyautogui.FAILSAFE = False  # Prevent abrupt exception on mouse move to top-left
    routine = PkMacroRoutines.ENSURE_PYCHARM_CODE_OPTIMIZED
    pk_ensure_keyboard_mouse_macro(routine)
