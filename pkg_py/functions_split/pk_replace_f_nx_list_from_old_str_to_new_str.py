


def pk_replace_f_nx_list_from_old_str_to_new_str(d_working, old_str, new_str):
    from pkg_py.functions_split.pk_print import pk_print
    import os

    for f_nx in os.listdir(d_working):
        pnx_old = os.path.join(d_working, f_nx)
        if os.path.isfile(pnx_old) and old_str in f_nx:
            f_nx_new = f_nx.replace(old_str, new_str)
            f_nx_new = f_nx_new.strip()
            f_new = os.path.join(d_working, f_nx_new)
            os.rename(pnx_old, f_new)
            if f_nx_new:
                pk_print(f"Renamed: {f_nx} -> {f_nx_new}", print_color='green')
            else:
                pk_print(f"Renamed: {f_nx} -> {f_nx_new}", print_color='red')
