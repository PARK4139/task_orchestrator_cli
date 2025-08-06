def ensure_pnx_moveds_without_overwrite(pnxs, dst):
    from pkg_py.functions_split.ensure_pnx_moved import ensure_pnx_moved

    for pnx in pnxs:
        ensure_pnx_moved(pnx=pnx, d_dst=dst)
