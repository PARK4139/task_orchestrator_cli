def ensure_pnx_removed(pnx):
    from sources.functions.does_pnx_exist import is_pnx_existing
    from sources.functions.get_nx import get_nx
    from sources.functions.ensure_pnxs_move_to_recycle_bin import ensure_pnxs_move_to_recycle_bin
    import logging
    from sources.objects.pk_local_test_activate import LTA

    import os
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    if not is_pnx_existing(pnx):
        logging.debug(f'''삭제할 {get_nx(pnx)} 가 없습니다. {'%%%FOO%%%' if LTA else ''}''')
        return
    if is_pnx_existing(pnx):
        # 1
        # if is_f(pnx):
        #     cmd = rf'echo y | del /f "{pnx}"'
        # else:
        #     cmd = rf'echo y | rmdir /s "{pnx}"'
        # ensure_command_executed(cmd=cmd)

        # 2
        # if does_pnx_exist(pnx):
        #     os.remove(pnx)

        # 3
        ensure_pnxs_move_to_recycle_bin(pnxs=[pnx])
    if not os.path.exists(pnx):
        logging.debug(rf"[{func_n}] pnx={pnx} {'%%%FOO%%%' if LTA else ''}")
    else:
        logging.debug(rf"[{func_n}] pnx={pnx} {'%%%FOO%%%' if LTA else ''}")
