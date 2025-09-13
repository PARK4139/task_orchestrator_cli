def get_magnets_set_from_nyaa_si_v1(nyaa_si_supplier, search_keyword, driver):  # v1 : txt 파일에 데이터를 수집하는 방식
    import logging

    from sources.functions import ensure_slept
    from sources.functions.ensure_value_completed import ensure_value_completed
    from sources.functions.get_driver_selenium import get_driver_selenium
    from sources.functions.get_list_from_int_a_to_int_b import get_list_from_int_a_to_int_b
    from sources.functions.get_page_number_last_of_nyaa_si_page import get_page_number_last_of_nyaa_si_page
    from sources.functions.get_str_encoded_url import get_str_encoded_url
    from sources.functions.get_str_url_decoded import get_str_url_decoded
    from sources.functions.get_total_cnt_of_f_torrent_list import get_total_cnt_of_f_torrent_list
    from sources.objects.pk_local_test_activate import LTA

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from bs4 import BeautifulSoup
    import math
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    import random

    if driver is None:
        driver = get_driver_selenium(browser_debug_mode=False)

    url = f'https://nyaa.si/user/{nyaa_si_supplier}?f=0&c=0_0&q={get_str_encoded_url(search_keyword)}'
    logging.debug(f'''url={url}  {'%%%FOO%%%' if LTA else ''}''')

    driver.get(url)
    page_src = driver.page_source
    soup = BeautifulSoup(page_src, "html.parser")

    page_number_last = None
    files_per_page = 75
    total_cnt_of_f_torrent_list = get_total_cnt_of_f_torrent_list(h3_text=soup.find("h3").text.strip())
    if total_cnt_of_f_torrent_list:
        page_number_last = math.ceil(total_cnt_of_f_torrent_list / files_per_page)
        logging.debug(f'''files_per_page={files_per_page}  {'%%%FOO%%%' if LTA else ''}''')
        logging.debug(f'''displayable_magnets_cnt_per_page={files_per_page}  {'%%%FOO%%%' if LTA else ''}''')
        logging.debug(f'''page_number_last={page_number_last}  {'%%%FOO%%%' if LTA else ''}''')
    else:
        page_number_last = get_page_number_last_of_nyaa_si_page(url=url, driver=driver)

    page_number_str_list = [str(i) for i in get_list_from_int_a_to_int_b(int_a=1, int_b=page_number_last)]
    page_number_start_to_download = int(
        ensure_value_completed(key_hint='page_number_start_to_download', options=page_number_str_list))
    page_number_end_to_download = int(
        ensure_value_completed(key_hint='page_number_end_to_download', options=page_number_str_list))

    magnets_set = set()
    logging.debug(f'''page_number_end_to_download={page_number_end_to_download}  {'%%%FOO%%%' if LTA else ''}''')
    for page_number in range(page_number_start_to_download, page_number_end_to_download + 1):
        url_page = f'{url}&p={page_number}'
        url_decoded = get_str_url_decoded(str_working=url_page)
        logging.debug(rf'''url_page={url_page:60s}  url_decoded={url_decoded}  {'%%%FOO%%%' if LTA else ''}''')
        driver.get(url_page)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        ensure_slept(milliseconds=random.randint(200, 333))
        page_src = driver.page_source
        soup = BeautifulSoup(page_src, "html.parser")
        # logging.debug(f'''soup={soup}  {'%%%FOO%%%' if LTA else ''}''')
        magnet_links = {a["href"] for a in soup.find_all("a", href=True) if a["href"].startswith("magnet:")}
        logging.debug(f'''Found {len(magnet_links)} magnet links on page {page_number}''')
        magnets_set |= magnet_links
    logging.debug(f'''len(magnets_set)={len(magnets_set)}  {'%%%FOO%%%' if LTA else ''}''')
    return magnets_set
