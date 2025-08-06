import os
import traceback

from pkg_py.functions_split.ensure_business_demo_copied_and_pushed import ensure_business_demo_copied_and_pushed
from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
from pkg_py.functions_split.ensure_git_project_pushed import ensure_git_project_pushed
from pkg_py.system_object.directories import D_PROJECT_MEMO
from pkg_py.system_object.directories  import D_PROJECT
from pkg_py.system_object.map_massages import PkMessages2025
# pk_#


if __name__ == "__main__":
    try:
        os.chdir(D_PROJECT)
        ensure_git_project_pushed(with_commit_massage=False)  # private repo
        # input(PkMessages2025.PRESS_ENTER_TO_PROCEED) # pk_option

        os.chdir(D_PROJECT_MEMO)
        ensure_git_project_pushed(with_commit_massage=False)  # private repo
        input(PkMessages2025.PRESS_ENTER_TO_PROCEED)

        ensure_business_demo_copied_and_pushed()  # public repo
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
