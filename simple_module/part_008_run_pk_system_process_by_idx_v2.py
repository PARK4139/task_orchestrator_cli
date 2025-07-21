

# import pywin32
# import pywin32
# from project_database.test_project_database import MySqlUtil

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def run_pk_system_process_by_idx_v2(pk_idx, pk_arg_list):
    #
    #
    if pk_arg_list is None:
        pk_arg_list = []

    if LTA:
        pk_print(f"pk_idx={pk_idx} %%%FOO%%%")
        for i, a in enumerate(pk_arg_list):
            pk_print(f"pk_arg_list[{i}]={a} %%%FOO%%%")

    pnx = get_available_pk_python_program_pnx(pk_idx)

    if LTA:
        pk_print(f"resolved file: {pnx} %%%FOO%%%")

    run_pk_python_program_by_path(pnx=pnx, pk_arg_list=pk_arg_list, LTA=LTA)
