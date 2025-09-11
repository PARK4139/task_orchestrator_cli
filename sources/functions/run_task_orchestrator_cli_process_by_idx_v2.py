def run_task_orchestrator_cli_process_by_idx_v2(pk_idx, pk_arg_list):
    from sources.functions.get_available_task_orchestrator_cli_process_pnx import get_available_task_orchestrator_cli_process_pnx
    import logging
    from sources.functions.run_task_orchestrator_cli_process_by_path import run_task_orchestrator_cli_process_by_path
    from sources.objects.pk_local_test_activate import LTA
    if pk_arg_list is None:
        pk_arg_list = []

    if LTA:
        logging.debug(f"pk_idx={pk_idx} %%%FOO%%%")
        for i, a in enumerate(pk_arg_list):
            logging.debug(f"pk_arg_list[{i}]={a} %%%FOO%%%")

    pnx = get_available_task_orchestrator_cli_process_pnx(pk_idx)

    if LTA:
        logging.debug(f"resolved file: {pnx} %%%FOO%%%")

    run_task_orchestrator_cli_process_by_path(pnx=pnx, pk_arg_list=pk_arg_list, LTA=LTA)
