

def print_and_save_log_to_file(msg, log_file_path):
    import logging

    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
    from pkg_py.functions_split.ensure_str_writen_to_f import ensure_str_writen_to_f
    logging.info(msg)
    ensure_pnx_made(pnx=log_file_path, mode="f")
    ensure_str_writen_to_f(msg=msg, f=log_file_path, mode="w")  # 내용 초기화


