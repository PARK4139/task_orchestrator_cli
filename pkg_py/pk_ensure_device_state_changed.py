

if __name__ == "__main__":
    from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_slept import ensure_slept
    import keyboard
    ensure_printed(f'''detect hotkey %%%FOO%%%''', print_color="blue")
    while 1:
        ensure_console_cleared()
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('`'):
            ensure_printed("ctrl + alt + 1 pressed")
            continue
        if keyboard.is_pressed('alt') and keyboard.is_pressed('1'):
            ensure_printed("alt + 1 pressed")
            continue
        if keyboard.is_pressed('esc'):
            ensure_printed("esc pressed")
        ensure_slept(milliseconds=100)
        # ensure_slept(milliseconds=10)
