def move_pycharm_cursor_to_file(__file__):
    import logging
    import logging
    import os
    from sources.functions.ensure_text_saved_to_clipboard import ensure_text_saved_to_clipboard

    from sources.functions.open_pycharm_parrete import open_pycharm_parrete_like_human
    from sources.functions.paste_and_enter import paste_and_enter_like_human
    from sources.functions.ensure_slept import ensure_slept
    
    from sources.objects.pk_map_texts import PkTexts

    filename_to_dst = os.path.basename(__file__)
    ensure_text_saved_to_clipboard(filename_to_dst)
    ensure_slept(100)
    open_pycharm_parrete_like_human()
    ensure_slept(500)
    paste_and_enter_like_human()
    logging.debug(f"[{PkTexts.MOVED}] {filename_to_dst}")
