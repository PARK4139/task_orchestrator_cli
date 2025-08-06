from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


# @ensure_seconds_measured
# def get_pnxs_from_d_working(d_working, with_walking=True):
#     from pkg_py.functions_split.is_d import is_d
#     import os
#     if not os.path.exists(d_working):
#         print(f"The pnx '{d_working}' does not exist.")
#     if not is_d(d_working):
#         print(f"The pnx '{d_working}' is not d")
#     pnx_list = []
#     if with_walking == 1:
#         for root, d_nx_list, f_nx_list in os.walk(d_working):
#             for d_nx in d_nx_list:
#                 pnx_list.append(os.path.join(root, d_nx))
#             for f_nx in f_nx_list:
#                 pnx_list.append(os.path.join(root, f_nx))
#         return pnx_list
#     if with_walking == 0:
#         if os.path.exists(d_working) and is_d(d_working):
#             pnx_list = [os.path.join(d_working, item) for item in os.listdir(d_working)]
#         return pnx_list


@ensure_seconds_measured
def get_pnxs_from_d_working(
        d_working,
        with_walking=False,
        only_files=False,  # 속도가 개선됨
        only_dirs=False,  # 속도가 개선됨
        exclude_keywords=None,
):
    import os
    from pkg_py.functions_split.is_d import is_d

    if not os.path.exists(d_working):
        print(f"The pnx '{d_working}' does not exist.")
        return []

    if not is_d(d_working):
        print(f"The pnx '{d_working}' is not d")
        return []

    if exclude_keywords is None:
        exclude_keywords = [".venv", "__PYCACHE__", "__pycache__"]

    pnx_list = []

    def should_exclude(pnx):
        return any(keyword.lower() in pnx.lower() for keyword in exclude_keywords)

    def append_filtered(full_path, is_file_check):
        if should_exclude(full_path):
            return
        if only_files and not os.path.isfile(full_path):
            return
        if only_dirs and not os.path.isdir(full_path):
            return
        pnx_list.append(full_path)

    if with_walking:
        for root, d_nx_list, f_nx_list in os.walk(d_working):
            for d_nx in d_nx_list:
                append_filtered(os.path.join(root, d_nx), is_file_check=False)
            for f_nx in f_nx_list:
                append_filtered(os.path.join(root, f_nx), is_file_check=True)
    else:
        for item in os.listdir(d_working):
            full_path = os.path.join(d_working, item)
            append_filtered(full_path, is_file_check=os.path.isfile(full_path))

    return pnx_list
