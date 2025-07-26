from pkg_py.functions_split.get_list_differenced import get_list_differenced
from pkg_py.functions_split.get_list_that_element_applyed_via_func import get_list_that_element_applyed_via_func
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_list_from_d_working import get_pnxs_from_d_working
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.workspace.pk_workspace import ensure_process_killed_by_window_title_seg


def kill_pk_program_list():
    f_list_a = get_pnxs_from_d_working(d_working=D_PKG_PY, with_walking=0)
    f_list_a = get_list_that_element_applyed_via_func(func=get_pnx_os_style, working_list=f_list_a)
    f_list_b = [
        rf"{D_PKG_PY}\system_object.static_logic.py"
        rf"{D_PKG_PY}\pk_kill_pk_program.py",
    ]
    f_list_b = get_list_that_element_applyed_via_func(func=get_pnx_os_style, working_list=f_list_b)
    f_list = get_list_differenced(list_a=f_list_a, list_b=f_list_b)
    for f in f_list:
        ensure_process_killed_by_window_title_seg(window_title_seg=get_nx(f))
    if not LTA:
        kill_self_pk_program(self_f='pk_kill_pk_program.py')
