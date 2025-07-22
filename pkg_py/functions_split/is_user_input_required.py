from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def is_user_input_required(user_input: str):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    # 수정 필요.
    user_input = user_input.strip()
    pk_print(working_str=rf'''user_input="{user_input}"  {'%%%FOO%%%' if LTA else ''}''')
    if is_only_no(user_input):
        user_input = int(user_input)
    else:
        pk_speak_v2("you can input only number, please input only number again", comma_delay=0.98)
        return None
    return user_input
