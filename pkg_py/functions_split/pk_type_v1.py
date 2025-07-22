

def pk_type_v1(text: str, interval: float = 0.1):  # "Setting it to 0.0 makes the loss retrievable."
    from pkg_py.pk_system_object.Local_test_activate import LTA
    from pkg_py.functions_split.pk_print import pk_print
    import pyautogui
    pyautogui.write(text, interval=interval)
    pk_print(working_str=rf'''Typed: "{text}"  {'%%%FOO%%%' if LTA else ''}''')


