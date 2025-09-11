from sources.objects.pk_local_test_activate import LTA

import logging


def driver_get_url_in_browser(url, driver, seconds_s=2222, seconds_e=4333):
    import random

    # driver.get(url_decoded)
    url_decoded = get_str_url_decoded(url)
    if url_decoded.startswith(("http://", "https://")):
        logging.debug(f'''url_decoded={url_decoded}  {'%%%FOO%%%' if LTA else ''}''')
        driver.get(url_decoded)
    else:
        logging.debug(f"WEIRED URL url_decoded={url_decoded}")
    ensure_slept(milliseconds=random.randint(a=seconds_s, b=seconds_e))  # 정적웹소스 다운로드 대기
    # focus 를 새탭으로 이동
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])
