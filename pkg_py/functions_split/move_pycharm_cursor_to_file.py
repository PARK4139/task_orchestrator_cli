def move_pycharm_cursor_to_file(__file__):
    import logging
    import os
    from pkg_py.functions_split.ensure_copied import ensure_copied

    from pkg_py.functions_split.open_pycharm_parrete import open_pycharm_parrete
    from pkg_py.functions_split.paste_and_enter import paste_and_enter
    from pkg_py.functions_split.ensure_slept import ensure_slept
    
    from pkg_py.system_object.map_massages import PkMessages2025

    filename_to_dst = os.path.basename(__file__)
    ensure_copied(filename_to_dst)
    ensure_slept(100)
    open_pycharm_parrete()
    ensure_slept(500)
    paste_and_enter()
    logging.info(f"[{PkMessages2025.MOVED}] {filename_to_dst}")
