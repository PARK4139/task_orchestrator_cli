import math
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.functions.get_nx import get_nx
from sources.functions.is_f import is_f


def open_url_with_reconnect(driver, url, reconnect_time=10, max_retries=3):
    import time
    from selenium.common.exceptions import WebDriverException
    attempt = 0
    while attempt < max_retries:
        try:
            driver.get(url)
            print(f"성공적으로 연결되었습니다: {url}")
            return 1
        except WebDriverException as e:
            attempt += 1
            print(f"연결 실패. 재시도 {attempt}/{max_retries}회, {reconnect_time}초 대기: {e}")
            time.sleep(reconnect_time)
    print(f"최대 재시도 횟수({max_retries}) 초과. 연결 실패.")
    return 0
