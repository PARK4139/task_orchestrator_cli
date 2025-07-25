
# hotkey press
# pk_sleep(milliseconds=100)
# single key press
break
def pk_press_v1(*presses: str, interval=0.0):
elif presses == "pgdn":
else:
for i in pyautogui.KEYBOARD_KEYS:
if "+" in presses[0]:
if len(presses) == 1:
if presses == "pgup":
if str(i) == str(presses[0]):
import pyautogui
key_list = []
key_list = get_list_striped_element(key_list)
key_list = presses[0].split("+")
pass
pk_print(str_working=rf'''{i}  {'%%%FOO%%%' if LTA else ''}''')
pk_print(str_working=rf'''{tmp}  {'%%%FOO%%%' if LTA else ''}''')
presses = "pagedown"
presses = "pageup"
pyautogui.hotkey(*key_list, interval=interval)
pyautogui.hotkey(*presses, interval=interval)
pyautogui.press(str(presses[0]), interval=interval)
tmp = ' + '.join(i for i in presses)
while 1:
