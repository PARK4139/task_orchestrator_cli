

def ensure_pnx_backed_ups_biggest():
    from sources.objects.pk_etc import BIGGEST_PNXS
    import logging
    from sources.functions.compress_pnx_via_bz import compress_pnx_via_bz
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    logging.debug(f"biggest_pnxs에 대한 백업을 시도합니다")
    for biggest_target in BIGGEST_PNXS:
        compress_pnx_via_bz(f'{biggest_target}')
