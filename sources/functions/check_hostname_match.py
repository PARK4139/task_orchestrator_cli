def check_hostname_match(target_hostname_value: str, match_type: str, pc_name_for_log: str) -> bool:
    import inspect

    import logging
    from sources.functions.get_hostname import get_hostname
    from sources.objects.pk_etc import PK_BLANK
    from sources.objects.pk_local_test_activate import LTA
    try:
        hostname = get_hostname()
        if LTA:
            logging.debug(f"Current hostname: {hostname}")
        is_match = False
        if match_type == "contains":
            is_match = target_hostname_value.lower() in hostname.lower()
        elif match_type == "equals":
            is_match = target_hostname_value.lower() == hostname.lower()
        else:
            logging.debug(f"Invalid match_type: {match_type}")
            return False

        if is_match:
            if LTA:
                # Use inspect to get the calling function's name for more specific logging
                caller_name = inspect.currentframe().f_back.f_code.co_name
                logging.debug(f"This is {pc_name_for_log} ({caller_name.replace("_", PK_BLANK)})")
            return True
        else:
            if LTA:
                logging.debug(f"This is not {pc_name_for_log}")
            return False

    except Exception as e:
        logging.debug(f"Failed to check if {pc_name_for_log}: {e}")
        return False

