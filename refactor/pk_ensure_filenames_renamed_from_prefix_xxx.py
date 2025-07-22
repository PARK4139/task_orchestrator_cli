import inspect
import os
import re
import traceback

from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
from pkg_py.functions_split.pk_initialize_and_customize_logging_config import pk_initialize_and_customize_logging_config
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_directories import D_FUNCTIONS_SPLIT
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE


def get_rename_map(d_working):
    part_pattern = re.compile(r"^(part_\d+_)(.+\.py)$")
    rename_map = {}
    for fname in os.listdir(d_working):
        match = part_pattern.match(fname)
        if match:
            new_name = match.group(2)
            rename_map[fname] = new_name
    return rename_map


def rename_files(d_working, rename_map, dry_run=True):
    updated_rename_map = {}
    for old_filename, new_filename in rename_map.items():
        old_path = os.path.join(d_working, old_filename)
        base, ext = os.path.splitext(new_filename)
        new_name = new_filename
        new_path = os.path.join(d_working, new_name)
        counter = 1
        while os.path.exists(new_path):
            new_name = f"{base}_DUPLICATED_{counter}{ext}"
            new_path = os.path.join(d_working, new_name)
            counter += 1
        updated_rename_map[old_filename] = new_name
        if dry_run:
            print(f"[{PkMessages2025.PREVIEW}] Rename: {old_filename} -> {new_name}")
        else:
            os.rename(old_path, new_path)
            print(f"[{PkMessages2025.RENAMED}] Rename: {old_filename} -> {new_name}")
    return updated_rename_map


def pk_ensure_filenames_renamed_from_prefix_xxx(mode=None):
    func_n = inspect.currentframe().f_code.co_name
    if LTA:
        d_working = D_FUNCTIONS_SPLIT
    else:
        key_name = "d_working"
        d_working = get_values_from_historical_file_routine(file_id=get_file_id(key_name, func_n), key_hint=f'{key_name}=', values_default=[D_FUNCTIONS_SPLIT])
    if mode is None:
        if LTA:
            exec_mode = PkMessages2025.EXECUTION
        else:
            exec_mode = get_value_completed(
                key_hint=f"{PkMessages2025.MODE}=",
                values=[PkMessages2025.PREVIEW, PkMessages2025.EXECUTION]
            ).strip()
    else:
        exec_mode = mode
    dry_run = exec_mode == PkMessages2025.PREVIEW
    rename_map = get_rename_map(d_working)
    rename_files(d_working, rename_map, dry_run=dry_run)
    return rename_map


if __name__ == "__main__":
    try:
        pk_initialize_and_customize_logging_config(__file__=__file__)
        pk_ensure_filenames_renamed_from_prefix_xxx()
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
