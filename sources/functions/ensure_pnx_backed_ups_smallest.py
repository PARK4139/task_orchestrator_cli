

import logging


def ensure_pnx_backed_ups_smallest():
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    logging.debug(f"smallest_pnxs에 대한 백업을 시도합니다")
    for target in SMALLEST_PNXS:
        compress_pnx_via_bz(f'{target}')
