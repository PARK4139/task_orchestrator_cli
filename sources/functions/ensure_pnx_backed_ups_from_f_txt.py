from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI


def ensure_pnx_backed_ups_from_f_txt(dst):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    f_txt = rf'{D_TASK_ORCHESTRATOR_CLI}\task_orchestrator_cli_sensitive\{func_n}.txt'
    ensure_pnx_made(pnx=D_TASK_ORCHESTRATOR_CLI_SENSITIVE, mode="d")
    ensure_pnx_made(pnx=f_txt, mode="f")
    # open_pnx(f_func_n_txt)
    texts = get_list_from_f(f=f_txt)
    texts = get_list_deduplicated(working_list=texts)
    texts = get_list_striped_element(working_list=texts)
    for text in texts:
        pk_ensure_pnx_backed_up(pnx_working=text, d_dst=dst)
