def run_pk_system_process_by_idx_v2(pk_idx, pk_arg_list):
    from pkg_py.functions_split.get_available_pk_system_process_pnx import get_available_pk_system_process_pnx
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.run_pk_system_process_by_path import run_pk_system_process_by_path
    from pkg_py.system_object.local_test_activate import LTA
    if pk_arg_list is None:
        pk_arg_list = []

    if LTA:
        ensure_printed(f"pk_idx={pk_idx} %%%FOO%%%")
        for i, a in enumerate(pk_arg_list):
            ensure_printed(f"pk_arg_list[{i}]={a} %%%FOO%%%")

    pnx = get_available_pk_system_process_pnx(pk_idx)

    if LTA:
        ensure_printed(f"resolved file: {pnx} %%%FOO%%%")

    run_pk_system_process_by_path(pnx=pnx, pk_arg_list=pk_arg_list, LTA=LTA)
