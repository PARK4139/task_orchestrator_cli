from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist


def get_df_from_issues_list_csv(issues_list_csv):
    import pandas as pd

    alternative_csv_pnx = get_pnx_os_style(rf"{D_DOWNLOADS}/deprecated/Issues_list.csv")
    issues_list_csv = get_pnx_os_style(issues_list_csv)
    # CSV f 로드
    for pnx in [issues_list_csv, alternative_csv_pnx]:
        pnx_unix = get_pnx_unix_style(pnx)
        if does_pnx_exist(pnx_unix):
            df = pd.read_csv(filepath_or_buffer=pnx_unix)
            if does_pnx_exist(pnx_unix):
                move_pnx(pnx=pnx_unix, d_dst=alternative_csv_pnx, with_overwrite=1)
            return df
    return None
