from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical


def print_sub_pnx_list(src):
    txt_to_exclude_list = [
        F_DB_YAML,
        F_SUCCESS_LOG,
        F_LOCAL_PKG_CACHE,
    ]

    # dir_pnxs, file_pnxs = get_sub_pnxs_without_walking(pnx=item_pnx, txt_to_exclude_list=txt_to_exclude_list)
    d_list, f_list = get_sub_pnx_list(pnx=src, txt_to_exclude_list=txt_to_exclude_list)

    pnx_list = d_list + f_list

    # 확인
    print_iterable_as_vertical(item_iterable=pnx_list, item_iterable_n="바꿀 대상")
    pk_print(working_str=rf'''len(pnxs)="{len(pnx_list)}"  {'%%%FOO%%%' if LTA else ''}''')
