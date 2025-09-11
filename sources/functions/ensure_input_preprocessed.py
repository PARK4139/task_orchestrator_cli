


def ensure_input_preprocessed(str_working, upper_seconds_limit, return_default):
    import time
    import logging
    from sources.functions.input_with_timeout import input_with_timeout
    from sources.objects.pk_local_test_activate import LTA

    pk_time_s = time.time()
    user_input = None
    while 1:
        elapsed = time.time() - pk_time_s
        if elapsed >= upper_seconds_limit:
            logging.debug(f'''elapsed >= upper_seconds_limit {'%%%FOO%%%' if LTA else ''}''')
            logging.debug(f'''user_input={user_input} {'%%%FOO%%%' if LTA else ''}''')
            if not user_input:
                return return_default
            else:
                return user_input
        user_input = input_with_timeout(str_working=rf'{str_working}',
                                           timeout_secs=int(upper_seconds_limit - elapsed))
        if user_input is None:
            user_input = ""
        user_input = user_input.strip()
        if user_input == "":
            return return_default
        elif user_input != "":
            return user_input
