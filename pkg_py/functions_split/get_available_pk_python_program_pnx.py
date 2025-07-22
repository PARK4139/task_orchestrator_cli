def get_available_pk_python_program_pnx(pk_idx):
    from pkg_py.functions_split.get_pk_system_process_pnx_and_idx_dict import get_pk_system_process_pnx_and_idx_dict
    pk_pnx_working_with_idx_dict = get_pk_system_process_pnx_and_idx_dict()
    pk_python_program_pnx_working = pk_pnx_working_with_idx_dict[pk_idx]
    return pk_python_program_pnx_working
