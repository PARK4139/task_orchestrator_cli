def get_available_pk_system_process_pnx(pk_idx):
    from pkg_py.functions_split.get_pk_system_processes_and_idx import get_pk_system_processes_and_idx
    pk_system_process_pnxs_and_idx = get_pk_system_processes_and_idx()
    return pk_system_process_pnxs_and_idx[pk_idx]
