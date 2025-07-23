from pkg_py.functions_split.get_value_completed import get_value_completed


def pk_ensure_functions_splited_v2():
    from pkg_py.functions_split.backup_workspace import backup_workspace
    import inspect
    import logging
    import os
    import os.path
    from pkg_py.pk_system_object.map_massages import PkMessages2025
    from pkg_py.functions_split.restore_workspace_from_latest_archive import restore_workspace_from_latest_archive
    from pkg_py.functions_split.split_by_top_level_def import split_by_top_level_def
    func_n = inspect.currentframe().f_code.co_name

    while True:
        d_working = rf"{os.environ['USERPROFILE']}\Downloads\pk_system\pkg_py\workspace"
        D_PKG_ARCHIVED = rf"{os.environ['USERPROFILE']}\Downloads\pk_system\pkg_archived"

        if not os.path.isdir(d_working):
            logging.info(f"[{PkMessages2025.PATH_NOT_FOUND}] {d_working}")
            return

        py_files = [f for f in os.listdir(d_working) if f.endswith('.py')]
        full_paths = [os.path.join(d_working, f) for f in py_files]

        if not full_paths:
            logging.info(f"[{PkMessages2025.LISTED}] No .py files found.")
            return

        exec_mode = get_value_completed(
            key_hint=f"{PkMessages2025.MODE}=",
            values=[PkMessages2025.PREVIEW, f"{PkMessages2025.DEFAULT} {PkMessages2025.EXECUTION}"]
        ).strip()
        prefix = get_value_completed(
            key_hint="Prefix=",
            values=["splited", ""]
        ).strip().rstrip('_')
        if not prefix:
            prefix = None

        archive_path = None
        if exec_mode == PkMessages2025.PREVIEW:
            for path in full_paths:
                split_by_top_level_def(d_working, filepath=path, prefix=prefix, preview=True)
        elif exec_mode == f"{PkMessages2025.DEFAULT} {PkMessages2025.EXECUTION}":
            archive_path = backup_workspace(D_PKG_ARCHIVED, d_working, func_n)
            for idx, path in enumerate(full_paths):
                logging.info(f"[{idx + 1}/{len(full_paths)}] {os.path.basename(path)}")
                split_by_top_level_def(d_working, filepath=path, prefix=prefix, preview=False)
            decision = get_value_completed(
                key_hint=f"{PkMessages2025.AFTER_SERVICE}=",
                values=[rf"{PkMessages2025.ORIGIN} {PkMessages2025.DELETE}", PkMessages2025.REVERT],
            )
            if decision == rf"{PkMessages2025.ORIGIN} {PkMessages2025.DELETE}":
                for path in full_paths:
                    try:
                        os.remove(path)
                        logging.info(f"[{PkMessages2025.REMOVED}] {os.path.basename(path)}")
                    except Exception as e:
                        logging.info(f"[{PkMessages2025.ERROR}] Failed to remove {path}: {e}")
            else:
                restore_workspace_from_latest_archive(D_PKG_ARCHIVED, d_working)
