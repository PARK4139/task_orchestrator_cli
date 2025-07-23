def pk_press_v2(*presses: str, interval=0.0):
    from pkg_py.pk_system_object.local_test_activate import LTA
    from pkg_py.pk_system_object.alias_keyboard_map import alias_keyboard_map
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.functions_split.get_list_striped_element import get_list_striped_element
    import pyautogui

    def convert_key(key: str) -> str:
        return alias_keyboard_map.get(key.lower().strip(), key.lower().strip())

    # 단일 키 처리
    if len(presses) == 1:
        if "+" in presses[0]:
            key_list = get_list_striped_element(presses[0].split("+"))
            key_list = [convert_key(k) for k in key_list]
            pyautogui.hotkey(*key_list, interval=interval)
            tmp = ' + '.join(key_list)
            pk_print(working_str=rf'''{tmp}  {'%%%FOO%%%' if LTA else ''}''')
        else:
            key = convert_key(presses[0])
            if key in pyautogui.KEYBOARD_KEYS:
                pyautogui.press(key, interval=interval)
                pk_print(working_str=rf'''{key}  {'%%%FOO%%%' if LTA else ''}''')
            else:
                pk_print(working_str=f"[WARN] Unsupported key: {key}")
    else:
        # 여러 키 조합 처리
        converted = [convert_key(k) for k in presses]
        pyautogui.hotkey(*converted, interval=interval)
        tmp = ' + '.join(converted)
        pk_print(working_str=rf'''{tmp}  {'%%%FOO%%%' if LTA else ''}''')
