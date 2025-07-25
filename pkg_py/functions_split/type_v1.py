
def pk_type_v1(text: str, interval: float = 0.1):  # "Setting it to 0.0 makes the loss retrievable."
from pkg_py.functions_split.print import pk_print
from pkg_py.system_object.local_test_activate import LTA
import pyautogui
pk_print(str_working=rf'''Typed: "{text}"  {'%%%FOO%%%' if LTA else ''}''')
pyautogui.write(text, interval=interval)
