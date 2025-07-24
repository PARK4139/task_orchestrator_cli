import undetected_chromedriver as uc
import pythoncom
import psutil
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from collections import Counter
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.is_d import is_d
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def get_random_date():
    import random
    from datetime import timedelta
    from datetime import datetime

    # 현재 날짜 가져오기
    current_date = datetime.now()
    # 시작 날짜 설정 (sample: 1970년 1월 1일)
    start_date = datetime(1970, 1, 1)
    # 현재 날짜와 시작 날짜 사이의 일수 계산
    days_diff = (current_date - start_date).days
    # 랜덤하게 선택된 일수 더하기
    random_date = start_date + timedelta(days=random.randint(0, days_diff))
    # "yyyy-yy-yy" 형식으로 포맷팅
    formatted_date = random_date.strftime("%Y-%y-%y")
    return formatted_date
