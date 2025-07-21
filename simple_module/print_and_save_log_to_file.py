

def print_and_save_log_to_file(msg, log_file_path):
    import logging

    from pkg_py.simple_module.part_001_ensure_pnx_made import ensure_pnx_made
    from pkg_py.simple_module.part_002_write_str_to_f import write_str_to_f
    logging.info(msg)
    ensure_pnx_made(pnx=log_file_path, mode="f")
    write_str_to_f(msg=msg, f=log_file_path, mode="w")  # 내용 초기화


