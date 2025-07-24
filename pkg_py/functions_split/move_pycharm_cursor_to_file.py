

def move_pycharm_cursor_to_file(__file__):
    import logging
    import os

    from pkg_py.functions_split.open_pycharm_parrete import open_pycharm_parrete
    from pkg_py.functions_split.paste_and_enter import paste_and_enter
    from pkg_py.functions_split.pk_sleep import pk_sleep
    from pkg_py.pk_paste_as_auto import pk_copy
    from pkg_py.system_object.map_massages import PkMessages2025

    filename_to_dst = os.path.basename(__file__)
    pk_copy(filename_to_dst)
    pk_sleep(100)
    open_pycharm_parrete()
    pk_sleep(500)
    paste_and_enter()
    logging.info(f"[{PkMessages2025.MOVED}] {filename_to_dst}")


