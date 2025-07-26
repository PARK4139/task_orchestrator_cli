from webdriver_manager.chrome import ChromeDriverManager
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.functions_split.ensure_printed import ensure_printed


def get_nth_row(df, n):
    # n번째 줄만 가져오기
    if n >= 0 and n <= len(df):
        return df.iloc[n]  # n번째 행
    else:
        ensure_printed(str_working="유효하지 않은 행 번호입니다.")
        return None
