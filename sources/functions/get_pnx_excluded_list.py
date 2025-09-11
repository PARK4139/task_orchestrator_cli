from sources.objects.pk_local_test_activate import LTA
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
import logging
from pathlib import Path


def get_pnx_excluded_list(d_working_list, exclusion_list):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    f_func_n_txt = rf"{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/{func_n}.txt"
    f_func_n_txt = Path(f_func_n_txt)
    ensure_pnx_made(pnx=f_func_n_txt, mode='f')
    logging.debug(f'''func_n={func_n}  {'%%%FOO%%%' if LTA else ''}''')
    logging.debug(f'''f_func_n_txt={f_func_n_txt}  {'%%%FOO%%%' if LTA else ''}''')
    logging.debug(f'''d_working_list={d_working_list}  {'%%%FOO%%%' if LTA else ''}''')
    make_pnx_interested_list_to_f_txt_x(d_working_list=d_working_list, exclusion_list=exclusion_list)
    return get_list_from_f(f=f_func_n_txt)
