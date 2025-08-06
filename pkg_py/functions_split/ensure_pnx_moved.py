


def ensure_pnx_moved(pnx, d_dst, with_overwrite=0, sequential_mode=0):
    from pkg_py.functions_split.ensure_pnx_moved_v2 import ensure_pnx_moved_v2
    ensure_pnx_moved_v2(pnx=pnx, d_dst=d_dst, with_overwrite=with_overwrite, sequential_mode=sequential_mode)
