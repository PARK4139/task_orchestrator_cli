def ensure_pnxs_moved_to_trash_bin(pnxs):
    from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
    from pkg_py.functions_split.ensure_pnxs_move_to_recycle_bin import ensure_pnxs_move_to_recycle_bin
    for pnx in pnxs:
        if does_pnx_exist(pnx):
            ensure_pnxs_move_to_recycle_bin(pnx=pnx)
