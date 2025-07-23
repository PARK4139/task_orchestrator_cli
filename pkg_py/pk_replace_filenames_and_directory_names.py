#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'pk == junghoon.park'

import inspect
import traceback
from pathlib import Path
from shutil import move

from colorama import init as pk_colorama_init
from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.pk_system_object.directories import D_PKG_TXT
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
from pkg_py.functions_split.ensure_pnx_removed import ensure_pnx_removed
from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_console_debuggable import ensure_console_debuggable

pk_colorama_init_once()


def pk_replace_filename_and_directory_name():
    func_n = inspect.currentframe().f_code.co_name

    key_name = "d_working"
    d_working = get_values_from_historical_file_routine(file_id=db.get_id(key_name,func_n), key_hint=f'{key_name}=', options_default=['pk_working'])


    f_files_to_replace = f"{D_PKG_TXT}/files_to_replace_via_{func_n}.txt"
    ensure_pnx_removed(pnx=f_files_to_replace)
    ensure_pnx_made(pnx=f_files_to_replace, mode='f')

    def load_replacements(path):
        replacements = []
        with open(path, encoding='utf-8') as f:
            for line in f:
                if "=>" in line:
                    src, dst = line.strip().split("=>")
                    replacements.append((src.strip(), dst.strip()))
        return replacements

    def is_hidden(filepath: Path):
        return any(part.startswith('.') for part in filepath.parts)

    def get_all_paths(root_dir):
        paths = [p for p in Path(root_dir).rglob("*") if not is_hidden(p)]
        dirs = sorted([p for p in paths if p.is_dir()], key=lambda x: len(str(x)), reverse=True)
        files = [p for p in paths if p.is_file()]
        return files + dirs

    def preview_renames(paths, replacements):
        preview = []
        for p in paths:
            new_name = p.name
            for old, new in replacements:
                new_name = new_name.replace(old, new)
            if new_name != p.name:
                preview.append(f"[RENAME] {p} → {new_name}")
        return preview

    def apply_renames(paths, replacements):
        results = []

        for p in paths:
            new_name = p.name
            for old, new in replacements:
                new_name = new_name.replace(old, new)

            if new_name == p.name:
                continue  # nothing to do

            new_path = p.with_name(new_name)
            if new_path.exists():
                results.append(f"[SKIPPED - EXISTS] {new_path}")
                continue

            try:
                move(str(p), str(new_path))
                results.append(f"[RENAMED] {p} → {new_path}")
            except Exception as e:
                results.append(f"[RENAME FAILED] {p}: {e}")

        return results

    print(f"\n[INFO] Scanning files and directories under '{d_working}'...")
    paths = get_all_paths(d_working)
    print(f"[INFO] Total {len(paths)} items found (files + directories).\n")

    # mkr..

    replacements = load_replacements(f_files_to_replace)
    if not replacements:
        print("[ERROR] No valid replacement rules found.")
        return

    print("[PREVIEW] The following renames will be applied:\n")
    preview = preview_renames(paths, replacements)
    for line in preview:
        print(line)

    print("\n[INFO] Press ENTER to apply the above changes. Press Ctrl+C to cancel.")
    input()

    results = apply_renames(paths, replacements)
    print("\n[INFO] Rename complete. Summary:\n")
    for line in results:
        print(line)


if __name__ == "__main__":
    try:
        pk_replace_filename_and_directory_name()
        if LTA:
            ensure_console_debuggable()
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)


