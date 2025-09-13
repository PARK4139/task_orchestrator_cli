from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING


def ensure_functionsed_v2():
    from sources.functions.backup_workspace import backup_workspace
    import inspect
    import logging
    import logging
    from sources.functions.ensure_value_completed import ensure_value_completed
    from sources.objects.task_orchestrator_cli_directories import D_ARCHIVED
    import os.path
    from sources.objects.pk_map_texts import PkTexts
    from sources.functions.restore_workspace_from_latest_archive import restore_workspace_from_latest_archive
    from sources.functions.split_by_top_level_def import split_by_top_level_def
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    while True:
        d_working = D_PK_WORKING # pk_option
        D_PKG_ARCHIVED = D_ARCHIVED

        if not os.path.isdir(d_working):
            logging.debug(f"[{PkTexts.PATH_NOT_FOUND}] {d_working}")
            return

        py_files = [f for f in os.listdir(d_working) if f.endswith('.py')]
        full_paths = [os.path.join(d_working, f) for f in py_files]

        if not full_paths:
            logging.debug(f"[{PkTexts.LISTED}] No .py files found.")
            return

        exec_mode = ensure_value_completed(
            key_hint=f"{PkTexts.MODE}=",
            options=[PkTexts.PREVIEW, f"{PkTexts.DEFAULT} {PkTexts.EXECUTION}"]
        ).strip()
        prefix = ensure_value_completed(
            key_hint="Prefix=",
            options=["splited", ""]
        ).strip().rstrip('_')
        if not prefix:
            prefix = None

        archive_path = None
        if exec_mode == PkTexts.PREVIEW:
            for path in full_paths:
                split_by_top_level_def(d_working, filepath=path, prefix=prefix, preview=True)
        elif exec_mode == f"{PkTexts.DEFAULT} {PkTexts.EXECUTION}":
            archive_path = backup_workspace(D_PKG_ARCHIVED, d_working, func_n)
            for idx, path in enumerate(full_paths):
                logging.debug(f"[{idx + 1}/{len(full_paths)}] {os.path.basename(path)}")
                split_by_top_level_def(d_working, filepath=path, prefix=prefix, preview=False)
            decision = ensure_value_completed(
                key_hint=f"{PkTexts.AFTER_SERVICE}=",
                options=[rf"{PkTexts.ORIGIN} {PkTexts.DELETE}", PkTexts.REVERT],
            )
            if decision == rf"{PkTexts.ORIGIN} {PkTexts.DELETE}":
                for path in full_paths:
                    try:
                        os.remove(path)
                        logging.debug(f"[{PkTexts.REMOVED}] {os.path.basename(path)}")
                    except Exception as e:
                        logging.debug(f"[{PkTexts.ERROR}] Failed to remove {path}: {e}")
            else:
                restore_workspace_from_latest_archive(D_PKG_ARCHIVED, d_working)
