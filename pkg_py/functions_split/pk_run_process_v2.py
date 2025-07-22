from pkg_py.functions_split.run_pk_python_program_by_path import run_pk_python_program_by_path


def pk_run_process_v2(pk_program_n_seg=None, pk_arg_list=None):
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_pk_system_process_pnx_list import get_pk_system_process_pnx_list
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.functions_split.run_pk_system_process_by_idx import run_pk_system_process_by_idx
    from pkg_py.pk_system_object.Local_test_activate import LTA

    if not pk_program_n_seg:
        pk_print("[SKIP] No segment provided.", print_color="yellow")
        return

    pk_list = get_pk_system_process_pnx_list()
    nx_map = [(i, get_nx(p)) for i, p in enumerate(pk_list)]

    for pk_idx, program_nx in nx_map:
        if pk_program_n_seg in program_nx:
            # run_pk_system_process_by_idx(pk_idx, pk_arg_list)
            if LTA:
                pk_print(f"pk_idx={pk_idx} get_nx={program_nx} pk_program_n_seg={pk_program_n_seg} {'%%%FOO%%%' if LTA else ''}", print_color="green")
            break
        else:
            if LTA:
                pk_print(f"pk_idx={pk_idx} get_nx={program_nx} pk_program_n_seg={pk_program_n_seg} {'%%%FOO%%%' if LTA else ''}")
