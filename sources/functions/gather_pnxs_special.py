from sources.functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
import logging
from sources.functions.is_window_opened import is_window_opened
from sources.functions.get_d_working import get_d_working


def gather_pnxs_special():
    import inspect
    import os
    import traceback

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    d_func_n = rf"{D_TASK_ORCHESTRATOR_CLI}\{func_n}"  # func_n_d 에 저장
    ensure_pnx_made(pnx=d_func_n, mode="d")

    ensure_pnx_opened_by_ext(pnx=d_func_n)

    if not is_window_opened(window_title_seg=func_n):
        ensure_pnx_opened_by_ext(pnx=d_func_n)

    starting_d = get_d_working()

    dst = d_func_n
    if not os.path.exists(dst):
        return
    services = os.path.dirname(dst)
    os.chdir(services)
    storages = []
    cmd = rf'dir /b /s "{D_DOWNLOADS}"'
    lines = ensure_command_executed_like_human_as_admin(cmd)
    for line in lines:
        if line.strip() != "":
            storages.append(line.strip())

    logging.debug(rf'archive_py 는 storage 목록 에서 제외')
    withouts = ['archive_py']
    for storage in storages:
        for without in withouts:
            if is_pattern_in_prompt(prompt=storage, pattern=without, with_case_ignored=False):
                storages.remove(storage)
    for storage in storages:
        print(storage)

    logging.debug(rf'이동할 storage 목록 중간점검 출력 시도')
    for storage in storages:
        print(os.path.abspath(storage))

    if not storages:
        logging.debug(rf'이동할 storage 목록 이 없어 storage 이동을 할 수 없습니다')
    else:
        logging.debug(rf'이동할 storage 목록 출력 시도')
        for storage in storages:
            print(os.path.abspath(storage))
        logging.debug(rf'목적지 생성 시도')
        if not os.path.exists(dst):
            os.makedirs(dst)
        for storage in storages:
            # print(src)
            try:
                logging.debug(rf'storage 이동 시도')
                ensure_pnx_moved(storage, dst)
            except FileNotFoundError:
                logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")

            except Exception as e:
                logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")

    os.chdir(starting_d)
