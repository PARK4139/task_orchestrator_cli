def is_pnx_existing(pnx=None, nx=None):
    from functions.ensure_console_paused import ensure_console_paused
    from pathlib import Path
    from sources.objects.pk_local_test_activate import LTA
    import logging
    from sources.functions.get_pnxs import get_pnxs
    from sources.functions.get_d_working import get_d_working
    from sources.objects.pk_map_texts import PkTexts

    if not pnx:
        if not nx:
            logging.warning(f'''{PkTexts.PNX_NX_ONLY_ONE_SET}. {'%%%FOO%%%' if LTA else ''}''')
            ensure_console_paused()

    if pnx:
        path = Path(pnx)
        if path.exists():
            logging.debug(rf"{pnx} does exist")
            return True
        else:
            logging.debug(rf"{pnx} does not exist")
            return False

    if nx:
        # nx 기반 검색 로직 (기존 로직 유지)
        pnxs = get_pnxs(d_working=get_d_working(), with_walking=False)
        for path_str in pnxs:
            if nx in Path(path_str).name:
                logging.debug(rf"{pnx} does exist")
                return True
        logging.debug(rf"{pnx} does not exist")
        return False
