from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_files_useless_gathered():
    import os

    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.functions.ensure_pnx_made import ensure_pnx_made
    from sources.functions.get_list_from_f import get_list_from_f
    from sources.functions.is_empty_d import is_empty_d
    from sources.functions.ensure_pnxs_move_to_recycle_bin import ensure_pnxs_move_to_recycle_bin
    from sources.functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI, D_PK_RECYCLE_BIN
    from sources.objects.task_orchestrator_cli_files import F_USELESS_FILE_NAMES_TXT

    import inspect
    import traceback

    from sources.functions.does_pnx_exist import is_pnx_existing
    from sources.functions.ensure_exception_routine_done import ensure_exception_routine_done
    from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
    import logging
    from sources.functions.get_file_id import get_file_id
    from sources.functions.get_historical_list import get_historical_list
    from sources.functions.get_list_calculated import get_list_calculated
    from sources.functions.get_list_sorted import get_list_sorted
    from pathlib import Path
    from sources.functions.ensure_value_completed import ensure_value_completed
    from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_PK_WORKING
    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.pk_map_texts import PkTexts

    try:

        from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()
        d_working = None
        if LTA:
            key_name = "d_working"
            file_to_working = get_file_id(key_name, func_n)
            historical_pnxs = get_historical_list(f=file_to_working)
            options = historical_pnxs + get_list_sorted(working_list=[D_PK_WORKING, D_DOWNLOADS], mode_asc=1)
            d_working = ensure_value_completed(key_hint='d_working', options=options)
            logging.debug(f'''len(historical_pnxs)={len(historical_pnxs)} {'%%%FOO%%%' if LTA else ''}''')
            logging.debug(f'''len(options)={len(options)} {'%%%FOO%%%' if LTA else ''}''')
            d_working = Path(d_working)
            values_to_save = [v for v in [d_working] + historical_pnxs + options if is_pnx_existing(pnx=v)]
            values_to_save = get_list_calculated(origin_list=values_to_save, dedup=True)
            ensure_list_written_to_f(f=file_to_working, working_list=values_to_save, mode="w")

        editable = True  # pk_option

        useless_file_names_txt = F_USELESS_FILE_NAMES_TXT
        if editable:
            ensure_pnx_opened_by_ext(pnx=useless_file_names_txt)

        dst = rf"{D_PK_RECYCLE_BIN}\pk_useless"
        ensure_pnx_made(pnx=dst, mode="d")
        logging.debug(f'''dst={dst}  {'%%%FOO%%%' if LTA else ''}''')
        if not is_empty_d(d_src=dst):
            ensure_command_executed(cmd=rf'explorer "{dst}" ', encoding='cp949')

        os.chdir(d_working)

        # string_clipboard_bkp=get_text_from_clipboard()


        userless_files = set()
        useless_files = get_list_from_f(useless_file_names_txt)
        # open_pnx(pnx=useless_file_names_txt, debug_mode=True)
        for useless_f_nx in useless_files:
            if useless_f_nx is not None:
                useless_f_nx = useless_f_nx.strip()
                useless_f_nx = useless_f_nx.strip("\n")
                cmd = f'dir /b /s "{useless_f_nx}"'
                useless_files = ensure_command_executed(cmd=cmd, encoding='cp949')
                if useless_files is None:
                    useless_files = []
                for uleless_f in useless_files:
                    if is_pnx_existing(pnx=uleless_f):
                        userless_files.add(uleless_f)

        os.chdir(D_TASK_ORCHESTRATOR_CLI)
        if len(userless_files) == 0:
            logging.debug(f'''len(useless_f_set)={len(userless_files)}  {'%%%FOO%%%' if LTA else ''}''')
            return
        else:
            for useless_f in userless_files:
                # ensure_pnx_moved(pnx=useless_f, d_dst=dst)  # todo : fix:외장드라이브에서는 안되는듯
                ensure_pnxs_move_to_recycle_bin(pnxs=[useless_f])
        logging.debug(rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''')
    except Exception as exception:
        ensure_exception_routine_done(__file__=__file__,traceback=traceback, exception=exception)
