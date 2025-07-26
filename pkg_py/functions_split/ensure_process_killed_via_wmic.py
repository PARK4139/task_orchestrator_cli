def ensure_process_killed_via_wmic(process_img_n=None, debug_mode=True):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    if process_img_n is not None:
        ensure_printed(rf"{func_n}() 동작 조건 충족")
    else:
        ensure_printed(rf"{func_n}() 동작 조건 불충족")
        return

    if process_img_n is not None:
        process_img_n = process_img_n.replace("\'", "")
        process_img_n = process_img_n.replace("\"", "")
        ensure_command_excuted_to_os(f'wmic process where name="{process_img_n}" delete ')


