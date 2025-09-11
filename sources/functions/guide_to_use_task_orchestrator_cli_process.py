

from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def guide_to_use_task_orchestrator_cli_process(task_orchestrator_cli_process_pnx_list, nx_by_user_input):
    from sources.objects.pk_local_test_activate import LTA
    
    from sources.functions.get_nx import get_nx
    import logging
    if LTA:
        logging.debug(f'''{'%%%FOO%%%' if LTA else ''}''')
    for idx, pnx_working in enumerate(task_orchestrator_cli_process_pnx_list):

        if nx_by_user_input in pnx_working:
            if LTA:
                logging.debug(f'''pnx_working={pnx_working} {'%%%FOO%%%' if LTA else ''}''')
            if nx_by_user_input in get_nx(pnx_working):

                if nx_by_user_input != get_nx(pnx_working):
                    print(rf'''{'[ TRY GUIDE ]'} pk {idx} ({get_nx(pnx_working)}) {'%%%FOO%%%' if LTA else ''}''')
            else:
                if LTA:
                    logging.debug(f'''{'%%%FOO%%%' if LTA else ''}''')
                break
