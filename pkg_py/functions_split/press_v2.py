
# 단일 키 처리
# 여러 키 조합 처리
converted = [convert_key(k) for k in presses]
def convert_key(key: str) -> str:
def pk_press_v2(*presses: str, interval=0.0):
else:
from pkg_py.functions_split.get_list_striped_element import get_list_striped_element
from pkg_py.functions_split.print import pk_print
from pkg_py.system_object.alias_keyboard_map import alias_keyboard_map
from pkg_py.system_object.local_test_activate import LTA
if "+" in presses[0]:
if key in pyautogui.KEYBOARD_KEYS:
if len(presses) == 1:
import pyautogui
key = convert_key(presses[0])
key_list = [convert_key(k) for k in key_list]
key_list = get_list_striped_element(presses[0].split("+"))
pk_print(str_working=f"[WARN] Unsupported key: {key}")
pk_print(str_working=rf'''{key}  {'%%%FOO%%%' if LTA else ''}''')
pk_print(str_working=rf'''{tmp}  {'%%%FOO%%%' if LTA else ''}''')
pyautogui.hotkey(*converted, interval=interval)
pyautogui.hotkey(*key_list, interval=interval)
pyautogui.press(key, interval=interval)
return alias_keyboard_map.get(key.lower().strip(), key.lower().strip())
tmp = ' + '.join(converted)
tmp = ' + '.join(key_list)
