from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_pnxs_renamed_from_pattern_twice_to_pattern_new(pnx, pattern, mode, with_walking, pattern_new="_"):
    import re

    ensure_printed(str_working=rf'''pattern={pattern} pattern_new={pattern_new}  {'%%%FOO%%%' if LTA else ''}''')

    txt_to_exclude_list = [
        F_DB_YAML, F_SUCCESS_LOG, F_LOCAL_PKG_CACHE,
    ]

    if with_walking == True:
        d_list, f_list = get_sub_pnx_list(pnx=pnx, txt_to_exclude_list=txt_to_exclude_list)
    else:
        d_list, f_list = get_sub_pnx_list(pnx=pnx, txt_to_exclude_list=txt_to_exclude_list, without_walking=0)

    if mode == "f":
        pnxs = f_list
    elif mode == "d":
        pnxs = d_list
    else:
        ensure_printed(str_working=rf'''"return"  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return

    # 두 번들어간 패턴
    pnxs_reg_checked = []
    item_new = None
    for item in pnxs:
        item_p = get_p(item[0])
        item_nx = get_nx(item[0])
        item_pnx = get_pnx(item[0])
        if len(re.findall(pattern, item[0])) >= 2:
            # if re.match(pattern, item_nx):
            pnxs_reg_checked.append(item)
    ensure_printed(f'''len(pnxs_reg_checked)={len(pnxs_reg_checked)}  {'%%%FOO%%%' if LTA else ''}''')

    pnxs_and_pnxs_new = []
    for item in pnxs_reg_checked:
        item_p = get_p(item[0])
        item_nx = get_nx(item[0])
        item_nx_new = re.sub(pattern, pattern_new, item_nx)
        if is_f(item[0]):
            item_pnx_new = rf"{item_p}\{item_nx_new}"
        else:
            item_pnx_new = rf"{item_p}\{item_nx_new}"
        pnxs_and_pnxs_new.append([item[0], item_pnx_new])

    # 확인
    ensure_printed(str_working=rf'''len(pnxs_and_pnxs_new)="{len(pnxs_and_pnxs_new)}" 바꿀 대상  {'%%%FOO%%%' if LTA else ''}''')

    # 적용
    rename_pnxs(pnx_list=pnxs_and_pnxs_new)
