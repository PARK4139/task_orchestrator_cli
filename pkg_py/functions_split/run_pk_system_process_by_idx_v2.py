def run_pk_system_process_by_idx_v2(pk_idx, pk_arg_list):
    from pkg_py.functions_split.get_available_pk_python_program_pnx import get_available_pk_python_program_pnx
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.functions_split.run_pk_python_program_by_path import run_pk_python_program_by_path
    from pkg_py.pk_system_object.Local_test_activate import LTA
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
