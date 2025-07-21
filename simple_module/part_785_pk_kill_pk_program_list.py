from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program


def pk_kill_pk_program_list():
    f_list_a = get_pnx_list_from_d_working(d_working=D_PKG_PY, with_walking=0)
    f_list_a = get_list_that_element_applyed_via_func(func=get_pnx_os_style, working_list=f_list_a)
    f_list_b = [
        rf"{D_PKG_PY}\pk_core.py",
        rf"{D_PKG_PY}\pk_core_class.py",
        rf"{D_PKG_PY}\pk_system_layer_static_logic.py"
        rf"{D_PKG_PY}\pk_kill_pk_program.py",
    ]
    f_list_b = get_list_that_element_applyed_via_func(func=get_pnx_os_style, working_list=f_list_b)
    f_list = get_list_differenced(list_a=f_list_a, list_b=f_list_b)
    for f in f_list:
        pk_kill_process_by_window_title_seg(window_title_seg=get_nx(f))
    if not LTA:
        kill_self_pk_program(self_f='pk_kill_pk_program.py')
