import inspect
import logging
import logging
import os
import os.path

from sources.objects.pk_map_texts import PkTexts










def ensure_functionsed_v1():
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    d_working = rf"{os.environ['USERPROFILE']}\Downloads\task_orchestrator_cli\resources\workspace"
    D_PKG_ARCHIVED = rf"{os.environ['USERPROFILE']}\Downloads\task_orchestrator_cli\pkg_archived"

    if not os.path.isdir(d_working):
        logging.debug(f"[{PkTexts.PATH_NOT_FOUND}] {d_working}")
        return

    py_files = [f for f in os.listdir(d_working) if f.endswith('.py')]
    full_paths = [os.path.join(d_working, f) for f in py_files]

    if not full_paths:
        logging.debug(f"[{PkTexts.LISTED}] No .py files found.")
        return

    preview_mode = ensure_value_completed(
        key_hint=f"{PkTexts.MODE}=",
        values=[PkTexts.PREVIEW, f"{PkTexts.DEFAULT} {PkTexts.EXECUTION}"]
    ) == PkTexts.PREVIEW

    prefix = ensure_value_completed(
        key_hint="Prefix=",
        values=["splited", ""]
    ).strip().rstrip('_')
    if not prefix:
        prefix = None

    if preview_mode:
        for path in full_paths:
            split_by_top_level_def(d_working, filepath=path, prefix=prefix, preview=True)
        return

    archive_path = backup_workspace(D_PKG_ARCHIVED, d_working, func_n)

    for idx, path in enumerate(full_paths):
        logging.debug(f"[{idx + 1}/{len(full_paths)}] {os.path.basename(path)}")
        split_by_top_level_def(d_working, filepath=path, prefix=prefix, preview=False)

    decision = ensure_value_completed(
        key_hint=f"{PkTexts.AFTER_SERVICE}=",
        values=[rf"{PkTexts.ORIGIN} {PkTexts.DELETE}", PkTexts.REVERT, rf"{PkTexts.WORK} {PkTexts.SHUTDOWN}"],
    )
    if decision == rf"{PkTexts.ORIGIN} {PkTexts.DELETE}":
        for path in full_paths:
            try:
                os.remove(path)
                logging.debug(f"[{PkTexts.REMOVED}] {os.path.basename(path)}")
            except Exception as e:
                logging.debug(f"[{PkTexts.ERROR}] Failed to remove {path}: {e}")
    elif decision == PkTexts.REVERT:
        restore_workspace_from_latest_archive(D_PKG_ARCHIVED, d_working)
    else:
        ensure_task_orchestrator_cli_exit_silent()
