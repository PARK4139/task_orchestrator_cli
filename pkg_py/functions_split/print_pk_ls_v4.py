

from pkg_py.system_object.stamps import STAMP_PK_ENVIRONMENT_WITH_UNDERBAR
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def print_pk_ls_v4(file_list: list[str], limit: int = None):
    import os
    ensure_printed("실행 가능한 pk_ 프로그램 목록:")

    for idx, filepath in enumerate(file_list):

        if limit is not None and idx >= limit:
            ensure_printed(f"... (이하 {len(file_list) - limit}개 생략됨)")
            break
        ensure_printed(f"[ pk {idx} ] {os.path.basename(filepath).replace(STAMP_PK_ENVIRONMENT_WITH_UNDERBAR, "")}")
