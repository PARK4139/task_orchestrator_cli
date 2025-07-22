

def pk_press_v1(*presses: str, interval=0.0):
    import pyautogui
    while 1:
        # single key press
        if len(presses) == 1:
            if "+" in presses[0]:
                key_list = []
                key_list = presses[0].split("+")
                key_list = get_list_striped_element(key_list)
                pyautogui.hotkey(*key_list, interval=interval)
                tmp = ' + '.join(i for i in presses)
                pk_print(working_str=rf'''{tmp}  {'%%%FOO%%%' if LTA else ''}''')
                break
            if presses == "pgup":
                presses = "pageup"
            elif presses == "pgdn":
                presses = "pagedown"
            for i in pyautogui.KEYBOARD_KEYS:
                if str(i) == str(presses[0]):
                    pyautogui.press(str(presses[0]), interval=interval)
                    pk_print(working_str=rf'''{i}  {'%%%FOO%%%' if LTA else ''}''')
                    break
                else:
                    pass
        # hotkey press
        else:
            pyautogui.hotkey(*presses, interval=interval)
            tmp = ' + '.join(i for i in presses)
            pk_print(working_str=rf'''{tmp}  {'%%%FOO%%%' if LTA else ''}''')
        # pk_sleep(milliseconds=100)
        break


