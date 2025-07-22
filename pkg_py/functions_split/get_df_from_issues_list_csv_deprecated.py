from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def get_df_from_issues_list_csv_deprecated():
    # 경로
    Downloads = rf"{D_HOME}/Downloads"
    issues_list_csv = rf"{D_HOME}/Downloads/Issues_list.csv"
    issues_list_csv_alternative = rf"{D_HOME}/Downloads/deprecated/Issues_list.csv"

    import pandas as pd
    df = None
    pnx = issues_list_csv
    if does_pnx_exist(pnx):
        df = pd.read_csv(filepath_or_buffer=pnx)
    else:
        pnx = issues_list_csv_alternative
        if does_pnx_exist(pnx):
            df = pd.read_csv(filepath_or_buffer=pnx)
    move_pnx(pnx=pnx, d_dst=Downloads, with_overwrite=1)
    return df
