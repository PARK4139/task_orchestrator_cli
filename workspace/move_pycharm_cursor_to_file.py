def move_pycharm_cursor_to_file(__file__):
    filename_to_dst = os.path.basename(__file__)
    pk_copy(filename_to_dst)
    pk_sleep(100)
    open_pycharm_parrete()
    pk_sleep(500)
    paste_and_enter()
    logging.info(f"[{PkMessages2025.MOVED}] {filename_to_dst}")


