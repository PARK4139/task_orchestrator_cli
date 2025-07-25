import os
import traceback

from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.system_object.directories import D_PROJECT_MEMO
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.workspace.pk_workspace import ensure_git_project_pushed, copy_and_push_auto_utility

if __name__ == "__main__":
    try:
        os.chdir(D_PROJECT)
        ensure_git_project_pushed(with_commit_massage=False) # private repo
        # input(PkMessages2025.PRESS_ENTER_TO_PROCEED) # pk_option


        os.chdir(D_PROJECT_MEMO)
        ensure_git_project_pushed(with_commit_massage=False) # private repo
        input(PkMessages2025.PRESS_ENTER_TO_PROCEED)


        copy_and_push_auto_utility() # public repo

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
