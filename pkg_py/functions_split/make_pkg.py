from pkg_py.pk_system_object.directories_reuseable import D_PROJECT


def make_pkg(dst):
    """wsl rar   wsl unrar   bz.exe  의존 """
    pnxs_required = get_pnx_list_from_d_working(d_working=D_PROJECT, with_walking=1)
    exclude_paths = [
        rf"{D_PROJECT}\.git",
        rf"{D_PROJECT}\.idea",
        rf"{D_PROJECT}\.venv",
        rf"{D_PROJECT}\__pycache__",
    ]
    pnxs_required = [path for path in pnxs_required if path not in exclude_paths]

    # backup
    # back_up_pnx_to_dst(src=PROJECT_D, dst=ARCHIVED)

    # del # remove됨...유의
    move_pnx_to_pk_recycle_bin(pnx=dst)

    # make
    ensure_pnx_made(pnx=dst, mode='d')

    # cp
    for pnx in pnxs_required:
        copy_pnx_with_overwrite(pnx=pnx, dst=dst)

    # compress
    compress_pnx(src=dst, dst=D_DESKTOP, with_timestamp=0)

    # del
    # move_pnx_to_trash_bin(pnx=dst)

    # decompress
    # decompress_pnx(src= rf"{dst}.rar", dst=DESKTOP)
