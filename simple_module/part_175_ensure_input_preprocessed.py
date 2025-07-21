from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def ensure_input_preprocessed(working_str, upper_seconds_limit, return_default):
    # 이거 windows 에서망 동작하는 함수?
    import time

    pk_time_s = time.time()
    user_input = None
    while 1:
        elapsed = time.time() - pk_time_s
        if elapsed >= upper_seconds_limit:
            pk_print(f'''elapsed >= upper_seconds_limit {'%%%FOO%%%' if LTA else ''}''')
            pk_print(f'''user_input={user_input} {'%%%FOO%%%' if LTA else ''}''')
            if not user_input:
                return return_default
            else:
                return user_input
        user_input = pk_input_with_timeout(working_str=rf'{working_str}',
                                           timeout_secs=int(upper_seconds_limit - elapsed))
        if user_input is None:
            user_input = ""
        user_input = user_input.strip()
        if user_input == "":
            return return_default
        elif user_input != "":
            return user_input
