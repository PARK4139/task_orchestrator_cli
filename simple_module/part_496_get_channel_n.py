from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style


def get_channel_n(channel_url, driver=None):
    from selenium.webdriver.common.by import By
    if driver is None:
        driver = get_driver_selenium(browser_debug_mode=True)

    driver.get(channel_url)
    pk_sleep(seconds=2)  # 페이지 로드 대기

    channel_name = driver.find_element(By.CSS_SELECTOR, "meta[itemprop='name']").get_attribute("content")
    channel_name = get_pnx_unix_style(channel_name)
    return channel_name
