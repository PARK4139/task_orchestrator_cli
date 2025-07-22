def get_pnxs_from_d_working(d_working, with_walking=1):
    from pkg_py.functions_split.is_d import is_d
    import os
    if not os.path.exists(d_working):
        print(f"The pnx '{d_working}' does not exist.")
    if not is_d(d_working):
        print(f"The pnx '{d_working}' is not d")
    pnx_list = []
    if with_walking == 1:
        for root, d_nx_list, f_nx_list in os.walk(d_working):
            for d_nx in d_nx_list:
                pnx_list.append(os.path.join(root, d_nx))
            for f_nx in f_nx_list:
                pnx_list.append(os.path.join(root, f_nx))
        return pnx_list
    if with_walking == 0:
        if os.path.exists(d_working) and is_d(d_working):
            pnx_list = [os.path.join(d_working, item) for item in os.listdir(d_working)]
        return pnx_list
