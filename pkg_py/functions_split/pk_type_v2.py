def pk_type_v2(text: str, interval: float = 0.1):
    from pkg_py.functions_split.switch_to_keyboard_mode_to_english_at_windows import switch_to_keyboard_mode_to_english_at_windows
    import pyautogui
    import platform
    """
    Types given text with optional IME switching on Windows.
    """
    from pkg_py.pk_system_object.local_test_activate import LTA
    from pkg_py.functions_split.pk_print import pk_print

    if text is None:
        pk_print(f'''text is None {'%%%FOO%%%' if LTA else ''}''')

        return

    system = platform.system()

    if system == "Windows":
        switch_to_keyboard_mode_to_english_at_windows()
    elif system in ("Linux", "Darwin"):
        print("[info] IME switching is not supported on this OS. Please ensure input is in English.")
    else:
        print(f"[info] Unknown OS: {system}. IME switching skipped.")

    pyautogui.write(text, interval=interval)
    pk_print(working_str=rf'''Typed: "{text}"  {'%%%FOO%%%' if LTA else ''}''')
