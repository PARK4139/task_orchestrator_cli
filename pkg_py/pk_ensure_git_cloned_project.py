# !/usr/bin/env python   # shebang
# -*- coding: utf-8 -*- # encoding declaration
__author__ = 'junghoon.park'

import inspect
import traceback

from colorama import init as pk_colorama_init

from pkg_py.functions_split.ensure_pnx_moveds_without_overwrite import ensure_pnx_moveds_without_overwrite
from pkg_py.system_object.directories import D_PKG_CACHE_PRIVATE, D_PK_RECYCLE_BIN
from pkg_py.system_object.directories  import D_PROJECT
# pk_#
from pkg_py.functions_split.get_n import get_n
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.reensure_pnx_moved_parmanently import reensure_pnx_moved_parmanently
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
from pkg_py.system_object.state_via_database import PkSqlite3DB

#, print_red
# from pkg_py.system_object.500_live_logic import ensure_command_excuted_to_os, get_n, reensure_pnx_moved_parmanently, does_pnx_exist, get_values_from_historical_file_routine
#, '[ TRY GUIDE ]', D_PROJECT, '[ UNIT TEST EXCEPTION DISCOVERED ]', D_PKG_CACHE_PRIVATE

ensure_colorama_initialized_once()

if __name__ == "__main__":
    try:

        # *** remove useless file
        f_historical = rf'{D_PKG_CACHE_PRIVATE}/historical_{get_n(__file__)}.txt'
        if does_pnx_exist(pnx=f_historical):
            # reensure_pnx_moved_parmanently(pnx=f_historical)
            ensure_pnx_moveds_without_overwrite(pnxs=[f_historical], dst=D_PK_RECYCLE_BIN)
        # ***

        db = PkSqlite3DB()

        func_n = inspect.currentframe().f_code.co_name

        key_name = "git_repo_url"
        git_repo_url = get_values_from_historical_file_routine(file_id = db.get_db_id(key_name, func_n), key_hint=f'{key_name}=', options_default=['pk_working'])

        key_name = "git_branch_name"
        git_branch_name = get_values_from_historical_file_routine(file_id=db.get_db_id(key_name, func_n), key_hint=f'{key_name}=', options_default=['pk_working'])

        key_name = "d_working"
        d_working = get_values_from_historical_file_routine(file_id=db.get_db_id(key_name, func_n), key_hint=f'{key_name}=', options_default=['pk_working'])

        std_list = ensure_command_excuted_to_os(f'git clone -b {git_branch_name} {git_repo_url} {d_working}')

    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
