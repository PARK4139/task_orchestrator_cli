def ensure_process_killed_via_wmic(process_img_n=None, debug_mode=True):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    if process_img_n is not None:
        logging.debug(rf"{func_n}() 동작 조건 충족")
    else:
        logging.debug(rf"{func_n}() 동작 조건 불충족")
        return

    if process_img_n is not None:
        process_img_n = process_img_n.replace("\'", "")
        process_img_n = process_img_n.replace("\"", "")
        ensure_command_executed(f'wmic process where name="{process_img_n}" delete ')


