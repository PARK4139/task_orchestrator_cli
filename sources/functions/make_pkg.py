from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI


def make_pkg(dst):
    """wsl rar   wsl unrar   bz.exe  의존 """
    pnxs_required = get_pnxs_from_d_working(d_working=D_TASK_ORCHESTRATOR_CLI, with_walking=True)
    exclude_paths = [
        rf"{D_TASK_ORCHESTRATOR_CLI}\.git",
        rf"{D_TASK_ORCHESTRATOR_CLI}\.idea",
        rf"{D_TASK_ORCHESTRATOR_CLI}\.venv_windows",
        rf"{D_TASK_ORCHESTRATOR_CLI}\__pycache__",
    ]
    pnxs_required = [path for path in pnxs_required if path not in exclude_paths]

    # backup
    # ensure_pnx_backed_up_to_dst(src=PROJECT_D, dst=ARCHIVED)

    # del # remove됨...유의
    ensure_pnxs_move_to_recycle_bin(pnxs=[dst])

    # make
    ensure_pnx_made(pnx=dst, mode='d')

    # cp
    for pnx in pnxs_required:
        copy_pnx_with_overwrite(pnx=pnx, dst=dst)

    # compress
    compress_pnx(src=dst, dst=D_DESKTOP, with_timestamp=0)

    # del
    # ensure_pnx_moved_to_trash_bin(pnx=dst)

    # decompress
    # decompress_pnx(src= rf"{dst}.rar", dst=DESKTOP)
