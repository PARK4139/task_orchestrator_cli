from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.pk_print import pk_print


def rename_pnxs_from_pattern_once_to_pattern_new(src, pattern, mode, pattern_new, with_walking):
    import re

    pk_print(str_working=rf'''pattern={pattern}  pattern_new={pattern_new}  {'%%%FOO%%%' if LTA else ''}''')

    txt_to_exclude_list = [
        F_DB_YAML, F_SUCCESS_LOG, F_LOCAL_PKG_CACHE,
    ]

    if with_walking == True:
        d_list, f_list = get_sub_pnx_list(pnx=src, txt_to_exclude_list=txt_to_exclude_list)
    else:
        d_list, f_list = get_sub_pnx_list(pnx=src, txt_to_exclude_list=txt_to_exclude_list, without_walking=0)

    if mode == "f":
        pnxs = f_list
    elif mode == "d":
        pnxs = d_list
    else:
        pk_print(str_working=rf'''"return"  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return
    pk_print(f'''len(pnxs)={len(pnxs)}  {'%%%FOO%%%' if LTA else ''}''')
    # print_list_as_vertical(working_list=pnxs, working_list_n="pnxs  {'%%%FOO%%%' if LTA else ''}")

    # 한 번들어간 패턴
    pnxs_reg_checked = []
    item_p = None
    item_nx = None
    item_pnx = None
    item_nx_new = None
    for item in pnxs:
        item_p = get_p(item[0])
        item_nx = get_nx(item[0])
        item_pnx = get_pnx(item[0])
        if re.search(pattern, item_nx):
            # if re.match(pattern, item_nx):
            pnxs_reg_checked.append(item)
    pk_print(str_working=rf'''pnxs_reg_checked="{pnxs_reg_checked}"  {'%%%FOO%%%' if LTA else ''}''')
    # print_list_as_vertical(working_list=pnxs_reg_checked, working_list_n="pnxs_reg_checked")

    pnxs_and_pnxs_new = []
    for item in pnxs_reg_checked:
        item_p = get_p(item[0])
        item_nx = get_nx(item[0])
        item_nx_new = re.sub(pattern, pattern_new, item_nx)

        # logging
        pk_print(str_working=rf'''item_nx_new="{item_nx_new}"  {'%%%FOO%%%' if LTA else ''}''')

        item_pnx_new = rf"{item_p}\{item_nx_new}"
        pnxs_and_pnxs_new.append([item[0], item_pnx_new])

    # logging
    pk_print(
        str_working=rf'''item_p={item_p} item_nx={item_nx} item_nx_new={item_nx_new} {'%%%FOO%%%' if LTA else ''}''')

    # 확인
    # print_list_as_vertical(working_list=pnxs_and_pnxs_new, working_list_n="바꿀 대상")
    # pk_print(str_working=rf'''len(pnxs_and_pnxs_new)="{len(pnxs_and_pnxs_new)}"  {'%%%FOO%%%' if LTA else ''}''')

    # 적용
    rename_pnxs(pnx_list=pnxs_and_pnxs_new)
