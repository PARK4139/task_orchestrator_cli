
# from project_database.test_project_database import MySqlUtil
)
) == PkMessages2025.PREVIEW
).strip().rstrip('_')
D_PKG_ARCHIVED = rf"{os.environ['USERPROFILE']}\Downloads\pk_system\pkg_archived"
archive_path = backup_workspace(D_PKG_ARCHIVED, d_working, func_n)
d_working = rf"{os.environ['USERPROFILE']}\Downloads\pk_system\pkg_py\workspace"
decision = get_value_completed(
def pk_ensure_functions_splited_v1():
elif decision == PkMessages2025.REVERT:
else:
ensure_pk_system_exit_silent()
except Exception as e:
for idx, path in enumerate(full_paths):
for path in full_paths:
from pkg_py.functions_split.ensure_pk_system_exit_silent import ensure_pk_system_exit_silent
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.refactor.pk_ensure_functions_splited import restore_workspace_from_latest_archive, split_by_top_level_def, backup_workspace
from pkg_py.system_object.map_massages import PkMessages2025
full_paths = [os.path.join(d_working, f) for f in py_files]
func_n = inspect.currentframe().f_code.co_name
if decision == rf"{PkMessages2025.ORIGIN} {PkMessages2025.DELETE}":
if not full_paths:
if not os.path.isdir(d_working):
if not prefix:
if preview_mode:
import inspect
import logging
import os
import os.path
key_hint="Prefix=",
key_hint=f"{PkMessages2025.AFTER_SERVICE}=",
key_hint=f"{PkMessages2025.MODE}=",
logging.info(f"[{PkMessages2025.ERROR}] Failed to remove {path}: {e}")
logging.info(f"[{PkMessages2025.LISTED}] No .py files found.")
logging.info(f"[{PkMessages2025.PATH_NOT_FOUND}] {d_working}")
logging.info(f"[{PkMessages2025.REMOVED}] {os.path.basename(path)}")
logging.info(f"[{idx + 1}/{len(full_paths)}] {os.path.basename(path)}")
os.remove(path)
prefix = None
prefix = get_value_completed(
preview_mode = get_value_completed(
py_files = [f for f in os.listdir(d_working) if f.endswith('.py')]
restore_workspace_from_latest_archive(D_PKG_ARCHIVED, d_working)
return
split_by_top_level_def(d_working, filepath=path, prefix=prefix, preview=False)
split_by_top_level_def(d_working, filepath=path, prefix=prefix, preview=True)
try:
values=["splited", ""]
values=[PkMessages2025.PREVIEW, f"{PkMessages2025.DEFAULT} {PkMessages2025.EXECUTION}"]
values=[rf"{PkMessages2025.ORIGIN} {PkMessages2025.DELETE}", PkMessages2025.REVERT, rf"{PkMessages2025.WORK} {PkMessages2025.SHUTDOWN}"],
