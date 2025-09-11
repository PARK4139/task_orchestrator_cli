from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI

import logging


def sum_via_txt_f():
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    f_func_n_txt = rf'{D_TASK_ORCHESTRATOR_CLI}\task_orchestrator_cli_sensitive\{func_n}.txt'
    ensure_pnx_made(pnx=f_func_n_txt, mode="f")
    ensure_pnx_opened_by_ext(f_func_n_txt)

    texts = get_list_from_f(f=f_func_n_txt)
    # texts=texts.split("\n")
    texts = get_list_striped_element(working_list=texts)
    total = 0
    for text in texts:
        if text is not None:
            total += int(text.strip())
    [logging.debug(item) for item in texts]
    logging.debug(f'''len(texts)={len(texts)}''')
    logging.debug(f'''total={total}''')
