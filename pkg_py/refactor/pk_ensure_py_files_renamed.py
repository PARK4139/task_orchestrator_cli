from pkg_py.system_object.directories import D_WORKSPACE


def ensure_py_files_renamed():
    d_target = D_WORKSPACE
    prefix = "pk_"

    if not os.path.isdir(d_target):
        print(f"[SKIP] Directory not found: {d_target}")
        return

    for filename in os.listdir(d_target):
        if not filename.endswith('.py'):
            continue
        if filename == '__init__.py':
            continue
        if filename.startswith('ensure_'):
            continue
        if filename.startswith(prefix):
            continue

        src = os.path.join(d_target, filename)
        dst = os.path.join(d_target, prefix + filename)

        try:
            os.rename(src, dst)
            print(f"[RENAMED] {filename} → {prefix + filename}")
        except Exception as exception:
            ensure_do_exception_routine(traceback=traceback, exception=exception)
        finally:
            ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)


import os
import traceback

import ipdb

from pkg_py.functions_split.ensure_console_debuggable import ensure_console_debuggable
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.colorama_init_once import colorama_init_once
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

if __name__ == "__main__":
    try:
        colorama_init_once()
        ensure_window_title_replaced(get_nx(__file__))
        ensure_py_files_renamed()
        if LTA:
            ensure_console_debuggable(ipdb)
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
