from pathlib import Path
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from pathlib import Path
from sources.functions.does_pnx_exist import is_pnx_existing


def get_df_from_issues_list_csv(issues_list_csv):
    import pandas as pd

    alternative_csv_pnx = Path(rf"{D_DOWNLOADS}/deprecated/Issues_list.csv")
    issues_list_csv = Path(issues_list_csv)
    # CSV f 로드
    for pnx in [issues_list_csv, alternative_csv_pnx]:
        pnx_unix = get_pnx_unix_style(pnx)
        if is_pnx_existing(pnx_unix):
            df = pd.read_csv(filepath_or_buffer=pnx_unix)
            if is_pnx_existing(pnx_unix):
                ensure_pnx_moved(pnx=pnx_unix, d_dst=alternative_csv_pnx, with_overwrite=1)
            return df
    return None
