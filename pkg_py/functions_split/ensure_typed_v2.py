def ensure_typed_v2(text: str, interval: float = 0.1):
    from pkg_py.functions_split.switch_to_keyboard_mode_to_english_at_windows import switch_to_keyboard_mode_to_english_at_windows
    import pyautogui
    import platform
    """
    Types given text with optional IME switching on Windows.
    """
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.ensure_printed import ensure_printed

    if text is None:
        ensure_printed(f'''text is None {'%%%FOO%%%' if LTA else ''}''')

        return

    system = platform.system()

    if system == "Windows":
        switch_to_keyboard_mode_to_english_at_windows()
    elif system in ("Linux", "Darwin"):
        print("[info] IME switching is not supported on this OS. Please ensure input is in English.")
    else:
        print(f"[info] Unknown OS: {system}. IME switching skipped.")

    pyautogui.write(text, interval=interval)
    ensure_printed(str_working=rf'''Typed: "{text}"  {'%%%FOO%%%' if LTA else ''}''')
