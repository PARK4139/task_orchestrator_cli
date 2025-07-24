import inspect
import logging
import os
import os.path

from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.refactor.pk_ensure_functions_splited import restore_workspace_from_latest_archive, split_by_top_level_def, backup_workspace
from pkg_py.functions_split.ensure_pk_system_exit_silent import ensure_pk_system_exit_silent
from pkg_py.functions_split.get_value_completed import get_value_completed


# import win32process
# import win32gui
# import win32gui
# import pywin32
# import pywin32
# from project_database.test_project_database import MySqlUtil


def pk_ensure_functions_splited_v1():
    func_n = inspect.currentframe().f_code.co_name

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

    preview_mode = get_value_completed(
        key_hint=f"{PkMessages2025.MODE}=",
        values=[PkMessages2025.PREVIEW, f"{PkMessages2025.DEFAULT} {PkMessages2025.EXECUTION}"]
    ) == PkMessages2025.PREVIEW

    prefix = get_value_completed(
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
        logging.info(f"[{idx + 1}/{len(full_paths)}] {os.path.basename(path)}")
        split_by_top_level_def(d_working, filepath=path, prefix=prefix, preview=False)

    decision = get_value_completed(
        key_hint=f"{PkMessages2025.AFTER_SERVICE}=",
        values=[rf"{PkMessages2025.ORIGIN} {PkMessages2025.DELETE}", PkMessages2025.REVERT, rf"{PkMessages2025.WORK} {PkMessages2025.SHUTDOWN}"],
    )
    if decision == rf"{PkMessages2025.ORIGIN} {PkMessages2025.DELETE}":
        for path in full_paths:
            try:
                os.remove(path)
                logging.info(f"[{PkMessages2025.REMOVED}] {os.path.basename(path)}")
            except Exception as e:
                logging.info(f"[{PkMessages2025.ERROR}] Failed to remove {path}: {e}")
    elif decision == PkMessages2025.REVERT:
        restore_workspace_from_latest_archive(D_PKG_ARCHIVED, d_working)
    else:
        ensure_pk_system_exit_silent()
