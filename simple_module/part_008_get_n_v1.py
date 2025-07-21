

# import win32process
# import win32gui
# import win32gui
# import pywin32
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_002_is_f import is_f


def get_n_v1(pnx):
    import os
    if is_f(pnx=pnx):
        return rf"{os.path.splitext(os.path.basename(pnx))[0]}"
    else:
        return os.path.basename(pnx)
