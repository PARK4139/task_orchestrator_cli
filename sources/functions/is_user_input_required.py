from sources.objects.pk_local_test_activate import LTA
import logging


def is_user_input_required(user_input: str):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    # 수정 필요.
    user_input = user_input.strip()
    logging.debug(rf'''user_input="{user_input}"  {'%%%FOO%%%' if LTA else ''}''')
    if is_only_no(user_input):
        user_input = int(user_input)
    else:
        ensure_spoken_v2("you can input only number, please input only number again", comma_delay=0.98)
        return None
    return user_input
