# !/usr/bin/env python   # shebang
# -*- coding: utf-8 -*- # encoding declaration
__author__ = 'junghoon.park'

import inspect
import traceback

from colorama import init as pk_colorama_init
from pkg_py.pk_system_object.directories import D_PKG_TXT
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.functions_split.get_n import get_n
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.remove_pnx_parmanently import remove_pnx_parmanently
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB

#, print_red
# from pkg_py.pk_system_object.500_live_logic import cmd_to_os, get_n, remove_pnx_parmanently, does_pnx_exist, get_values_from_historical_file_routine
#, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, D_PKG_TXT

pk_colorama_init_once()

if __name__ == "__main__":
    try:

        # *** remove useless file
        f_historical = rf'{D_PKG_TXT}/historical_{get_n(__file__)}.txt'
        if does_pnx_exist(pnx=f_historical):
            remove_pnx_parmanently(pnx=f_historical)
        # ***

        db = PkSqlite3DB()

        func_n = inspect.currentframe().f_code.co_name

        key_name = "git_repo_url"
        git_repo_url = get_values_from_historical_file_routine(file_id = db.get_id(key_name,func_n) , key_hint=f'{key_name}=', values_default=['pk_working'])

        key_name = "git_branch_name"
        git_branch_name = get_values_from_historical_file_routine(file_id=db.get_id(key_name,func_n), key_hint=f'{key_name}=', values_default=['pk_working'])

        key_name = "d_working"
        d_working = get_values_from_historical_file_routine(file_id=db.get_id(key_name,func_n), key_hint=f'{key_name}=', values_default=['pk_working'])

        std_list = cmd_to_os(f'git clone -b {git_branch_name} {git_repo_url} {d_working}')

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
