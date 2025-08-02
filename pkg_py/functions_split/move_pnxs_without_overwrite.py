def move_pnxs_without_overwrite(pnxs, dst):
    from pkg_py.functions_split.move_pnx import move_pnx

    for pnx in pnxs:
        move_pnx(pnx=pnx, d_dst=dst)
