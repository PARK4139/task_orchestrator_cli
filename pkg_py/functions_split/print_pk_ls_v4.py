

from pkg_py.pk_system_object.stamps import STAMP_PK_ENVIRONMENT_WITH_UNDERBAR
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.pk_measure_seconds import pk_measure_seconds


@pk_measure_seconds
def print_pk_ls_v4(file_list: list[str], limit: int = None):
    import os
    pk_print("실행 가능한 pk_ 프로그램 목록:")

    for idx, filepath in enumerate(file_list):

        if limit is not None and idx >= limit:
            pk_print(f"... (이하 {len(file_list) - limit}개 생략됨)")
            break
        pk_print(f"[ pk {idx} ] {os.path.basename(filepath).replace(STAMP_PK_ENVIRONMENT_WITH_UNDERBAR, "")}")
