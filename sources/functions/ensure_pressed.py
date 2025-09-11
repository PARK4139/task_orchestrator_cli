def ensure_pressed(*presses: str, interval=0.0):
    import logging
    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.alias_keyboard_map import alias_keyboard_map
    from sources.functions.get_list_striped_element import get_list_striped_element
    from sources.functions.is_os_linux import is_os_linux
    import pyautogui

    def convert_key(key: str) -> str:
        return alias_keyboard_map.get(key.lower().strip(), key.lower().strip())

    # Linux에서 GUI 환경이 없는 경우 처리
    if is_os_linux():
        try:
            # DISPLAY 환경변수 확인
            import os
            if not os.environ.get('DISPLAY'):
                logging.debug("GUI 환경이 없어 키 입력을 시뮬레이션할 수 없습니다.")
                return
        except Exception:
            logging.debug("GUI 환경 확인 실패")
            return

    # 단일 키 처리
    if len(presses) == 1:
        if "+" in presses[0]:
            key_list = get_list_striped_element(presses[0].split("+"))
            key_list = [convert_key(k) for k in key_list]
            try:
                pyautogui.hotkey(*key_list, interval=interval)
                tmp = ' + '.join(key_list)
                logging.debug(rf'''"{tmp}" is pressed {'%%%FOO%%%' if LTA else ''}''')
            except Exception as e:
                logging.debug(f"키 입력 실패: {e}")
        else:
            key = convert_key(presses[0])
            if key in pyautogui.KEYBOARD_KEYS:
                try:
                    pyautogui.press(key, interval=interval)
                    logging.debug(rf'''{key} pressed {'%%%FOO%%%' if LTA else ''}''')
                except Exception as e:
                    logging.debug(f"키 입력 실패: {e}")
            else:
                logging.debug(f"[WARN] Unsupported key: {key}")
    else:
        # 여러 키 조합 처리
        converted = [convert_key(k) for k in presses]
        try:
            pyautogui.hotkey(*converted, interval=interval)
            tmp = ' + '.join(converted)
            logging.debug(rf'''{tmp}  {'%%%FOO%%%' if LTA else ''}''')
        except Exception as e:
            logging.debug(f"키 입력 실패: {e}")
