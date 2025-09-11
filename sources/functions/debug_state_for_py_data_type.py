def debug_state_for_py_data_type(pk_stamp, data_working, highlight_config_dict=None, with_LTA=1):
    from sources.functions.input_with_timeout import input_with_timeout
    import logging
    from sources.objects.pk_local_test_activate import LTA

    import time
    if with_LTA == 1:
        if LTA == 1:
            if data_working:
                if isinstance(data_working, list):
                    for element in data_working:
                        # logging.debug(f'''element={element} {'%%%FOO%%%' if LTA else ''}''')
                        logging.debug(element, highlight_config_dict)
                elif isinstance(data_working, dict):
                    for key, value in data_working.items():
                        logging.debug(f'{key}: {value}', highlight_config_dict)
                elif isinstance(data_working, str):
                    logging.debug(f'{data_working}', highlight_config_dict)

            pk_time_limit = 30
            pk_time_s = time.time()
            while 1:
                elapsed = time.time() - pk_time_s
                if elapsed >= pk_time_limit:
                    logging.debug(f'''time out (pk_time_limit={pk_time_limit}) {'%%%FOO%%%' if LTA else ''}''')
                    break
                user_input = input_with_timeout(
                    str_working=rf'[?] [?] Press Enter to continue.',
                    timeout_secs=int(pk_time_limit - elapsed))
                if not user_input:
                    user_input = ""
                if user_input == "":
                    break
    elif with_LTA == 0:  # LTA=0 이더라도 출력은 그대로 쓸때
        if data_working:
            if isinstance(data_working, list):
                for element in data_working:
                    logging.debug(element, highlight_config_dict)
            elif isinstance(data_working, dict):
                for key, value in data_working.items():
                    logging.debug(f'{key}: {value}', highlight_config_dict)
            elif isinstance(data_working, str):
                logging.debug(f'{data_working}', highlight_config_dict)
