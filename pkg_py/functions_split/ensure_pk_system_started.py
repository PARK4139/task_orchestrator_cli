from pkg_py.functions_split.measure_seconds import measure_seconds


@measure_seconds
def ensure_pk_system_started():
    from pkg_py.functions_split.ensure_pk_system_started_v5 import ensure_pk_system_started_v5
    # ensure_pk_system_started_v2(index_map)
    # ensure_pk_system_started_v3(get_sorted_pk_file_list()) # not used fzf
    # ensure_pk_system_started_v4()
    ensure_pk_system_started_v5()
