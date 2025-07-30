import pyautogui

from pkg_py.functions_split.pk_ensure_keyboard_mouse_macro import pk_ensure_keyboard_mouse_macro
from pkg_py.functions_split.initialize_and_customize_logging_config import initialize_and_customize_logging_config


class PkMacroRoutines:
    ENSURE_PYCHARM_CODE_OPTIMIZED = None  # for auto-completion

    _localized_texts = {
        "ENSURE_PYCHARM_CODE_OPTIMIZED": {"kr": "PyCharm module script 최적화 매크로", "en": "Optimize PyCharm Code"}
    }

    @classmethod
    def set_lang(cls, lang: str):
        if lang not in ('kr', 'en'):
            raise ValueError(f"Unsupported language: {lang}")
        for key, val in cls._localized_texts.items():
            setattr(cls, key, val.get(lang, f"[{key}]"))

PkMacroRoutines.set_lang("kr")

if __name__ == "__main__":
    initialize_and_customize_logging_config(__file__)
    pyautogui.FAILSAFE = False  # Prevent abrupt exception on mouse move to top-left
    routine = PkMacroRoutines.ENSURE_PYCHARM_CODE_OPTIMIZED
    pk_ensure_keyboard_mouse_macro(routine)
