import inspect
import logging
import os
import os.path
import re
import traceback

from pkg_py.functions_split.backup_workspace import backup_workspace
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
from pkg_py.functions_split.restore_workspace_from_latest_archive import restore_workspace_from_latest_archive
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.directories import D_PK_FUNCTIONS_SPLIT, D_PKG_ARCHIVED
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.system_object.directories_reuseable import D_PROJECT


def replace_in_file(file_path, old_str, new_str):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_str not in content:
        logging.info(f"[{PkMessages2025.SKIPPED}] {file_path} (No target string found)")
        return False
    new_content = content.replace(old_str, new_str)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    logging.info(f"[{PkMessages2025.INSERTED}] Replaced '{old_str}' with '{new_str}' in: {file_path}")
    return True


def walk_and_replace(target_dir, old_str, new_str, exts=None):
    changed_files = []
    for root, _, files in os.walk(target_dir):
        for fname in files:
            if exts and not any(fname.endswith(ext) for ext in exts):
                continue
            file_path = os.path.join(root, fname)
            try:
                if replace_in_file(file_path, old_str, new_str):
                    changed_files.append(file_path)
            except Exception as e:
                logging.error(f"[ERROR] {file_path} - {e}")
    logging.info(f"Total files changed: {len(changed_files)}")


def walk_and_regex_replace(target_dir, pattern, repl, exts=None, dry_run=True):
    changed_files = []
    # 1. 대상 파일 전체 목록 수집
    all_files = []
    for root, _, files in os.walk(target_dir):
        for fname in files:
            if exts and not any(fname.endswith(ext) for ext in exts):
                continue
            file_path = os.path.join(root, fname)
            all_files.append(file_path)
    total_files = len(all_files)

    # 2. 진행률과 함께 파일 처리
    for idx, file_path in enumerate(all_files, 1):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if not re.search(pattern, content):
                # logging.info(f"[{idx}/{total_files}] [{mkr..}] [{PkMessages2025.SKIPPED}] {file_path} (Pattern not found)")
                continue
            new_content = re.sub(pattern, repl, content)
            if dry_run:
                if content != new_content:
                    logging.info(f"[{idx}/{total_files}] [{PkMessages2025.DRY_RUN}] Would replace pattern '{pattern}' with '{repl}' in: {file_path}")
                    changed_files.append(file_path)
            else:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                logging.info(f"[{idx}/{total_files}] [{PkMessages2025.INSERTED}] Replaced pattern '{pattern}' with '{repl}' in: {file_path}")
                changed_files.append(file_path)
        except Exception as e:
            logging.error(f"[{idx}/{total_files}] [ERROR] {file_path} - {e}")
    logging.info(f"{len(changed_files)}/{total_files} files {'to be changed' if dry_run else 'changed'}")
    return changed_files


def pk_ensure_filecontents_renamed_from_old_str_to_new_str():
    while True:
        func_n = inspect.currentframe().f_code.co_name

        if LTA:
            d_working = D_PKG_PY
            old_str = r"pkg_py\.functions_split\.part_\d+_"  # part_{숫자}_ 패턴을 pkg_py.functions_split.으로 변경
            new_str = "pkg_py.functions_split."
            exts = [".py", ".txt"]
        else:
            key_name = "d_working"
            d_working = get_values_from_historical_file_routine(
                file_id=get_file_id(key_name, func_n),
                key_hint=f'{key_name}=',
                options_default=[D_PK_FUNCTIONS_SPLIT, D_PKG_PY]
            )[0]

            key_name = "old_str"
            old_str = get_values_from_historical_file_routine(
                file_id=get_file_id(key_name, func_n),
                key_hint=f'{key_name}=',
                options_default=["old_string"]
            )[0]

            key_name = "new_str"
            new_str = get_values_from_historical_file_routine(
                file_id=get_file_id(key_name, func_n),
                key_hint=f'{key_name}=',
                options_default=["new_string"]
            )[0]

            key_name = "exts"
            exts = get_values_from_historical_file_routine(
                file_id=get_file_id(key_name, func_n),
                key_hint=f'{key_name}= (예: .py,.txt)',
                options_default=[".py,.txt"]
            )[0]

        if not os.path.isdir(d_working):
            logging.info(f"[{PkMessages2025.PATH_NOT_FOUND}] {d_working}")
            return

        python_filenames = [f for f in os.listdir(d_working) if f.endswith('.py')]
        python_files = [os.path.join(d_working, f) for f in python_filenames]
        if not python_files:
            logging.info(f"[{PkMessages2025.LISTED}] No .py files found.")
            return

        exec_mode = get_value_completed(
            key_hint=f"{PkMessages2025.MODE}=",
            values=[PkMessages2025.DRY_RUN, PkMessages2025.EXECUTION]
        ).strip()

        dry_run = None
        if exec_mode == PkMessages2025.DRY_RUN:
            dry_run = True
            logging.info(f"[{PkMessages2025.MODE}] {f'{PkMessages2025.DRY_RUN}' if dry_run else PkMessages2025.EXECUTION}")
        elif exec_mode == PkMessages2025.EXECUTION:
            dry_run = False
            logging.info(f"[{PkMessages2025.MODE}] {f'{PkMessages2025.DRY_RUN}' if dry_run else PkMessages2025.EXECUTION}")

        if exec_mode == PkMessages2025.DRY_RUN:
            walk_and_regex_replace(d_working, old_str, new_str, exts=exts, dry_run=dry_run)
        elif exec_mode == PkMessages2025.EXECUTION:

            # 1. backup
            logging.info(f"[{PkMessages2025.STARTED}] {PkMessages2025.BACKUP}")
            archive_path = backup_workspace(D_PKG_ARCHIVED, d_working, func_n)
            logging.info(f"[{PkMessages2025.FINISHED}] {PkMessages2025.BACKUP}")

            # 2. work
            walk_and_regex_replace(d_working, old_str, new_str, exts=exts, dry_run=dry_run)

            # 3. after service
            decision = get_value_completed(
                key_hint=f"{PkMessages2025.AFTER_SERVICE}=",
                values=[rf"{PkMessages2025.ORIGIN} {PkMessages2025.DELETE}", PkMessages2025.REVERT],
            )
            if decision == rf"{PkMessages2025.ORIGIN} {PkMessages2025.DELETE}":
                for path in python_files:
                    try:
                        os.remove(path)  # TODO   move to 휴지통    as  origiin   or tar.bz2
                        logging.info(f"[{PkMessages2025.REMOVED}] {os.path.basename(path)}")
                    except Exception as e:
                        logging.info(f"[{PkMessages2025.ERROR}] Failed to remove {path}: {e}")
            else:
                try:
                    logging.info(f"[{PkMessages2025.STARTED}] {PkMessages2025.REVERTED}")
                    restore_workspace_from_latest_archive(D_PKG_ARCHIVED, d_working)
                    logging.info(f"[{PkMessages2025.DONE}] {PkMessages2025.REVERTED}")
                except Exception as e:
                    logging.error(f"[{PkMessages2025.ERROR}] {PkMessages2025.AUTO} {PkMessages2025.REVERTED}")
                    logging.error(f"[{PkMessages2025.RETRY}] {PkMessages2025.AUTO} {PkMessages2025.REVERTED}")
                    if archive_path:
                        restore_workspace_from_latest_archive(D_PKG_ARCHIVED, d_working)
                        logging.info(f"[{PkMessages2025.DONE}] {PkMessages2025.AUTO} {PkMessages2025.REVERTED}")
                    raise


if __name__ == "__main__":
    from pkg_py.functions_split.initialize_and_customize_logging_config import initialize_and_customize_logging_config
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.pk_ensure_finally_routine_done import pk_ensure_finally_routine_done

    initialize_and_customize_logging_config(__file__=__file__)
    try:
        pk_ensure_filecontents_renamed_from_old_str_to_new_str()
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        pk_ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
