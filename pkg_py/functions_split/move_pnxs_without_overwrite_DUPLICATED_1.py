

def move_pnxs_without_overwrite(pnxs, dst):
    for pnx in pnxs:
        move_pnx(pnx=pnx, d_dst=dst)
