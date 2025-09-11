from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical


def print_sub_pnx_list(src):
    txt_to_exclude_list = [
        F_DB_YAML,
        F_SUCCESS_LOG,
        F_LOCAL_PKG_CACHE_PRIVATE,
    ]

    # dir_pnxs, file_pnxs = get_sub_pnxs_without_walking(pnx=item_pnx, txt_to_exclude_list=txt_to_exclude_list)
    d_list, f_list = get_sub_pnx_list(pnx=src, txt_to_exclude_list=txt_to_exclude_list)

    pnx_list = d_list + f_list

    # 확인
    ensure_iterable_log_as_vertical(item_iterable=pnx_list, item_iterable_n="바꿀 대상")
    logging.debug(rf'''len(pnxs)="{len(pnx_list)}"  {'%%%FOO%%%' if LTA else ''}''')
