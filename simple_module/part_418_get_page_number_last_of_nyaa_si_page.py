from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_014_pk_print import pk_print


def get_page_number_last_of_nyaa_si_page(url, driver):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from bs4 import BeautifulSoup
    import re
    page_number_max_in_pagenation = 1
    while 1:
        url_page = f'{url}&p={page_number_max_in_pagenation}'
        driver.get(url_page)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        pk_sleep(milliseconds=200)
        page_src = driver.page_source
        soup = BeautifulSoup(page_src, "html.parser")
        # pk_print(f'''soup={soup}  {'%%%FOO%%%' if LTA else ''}''')
        ul_pagination = soup.find("ul", class_="pagination")
        page_number_in_pagenation_list = []
        if ul_pagination:
            # print(ul_pagination.prettify())
            for a_tag in ul_pagination.find_all("a"):
                text = a_tag.get_text(strip=True)
                # 숫자인 경우에만 리스트에 추가
                if text.isdigit():
                    page_number_in_pagenation_list.append(int(text))
        if page_number_in_pagenation_list:
            page_number_max_in_pagenation = max(page_number_in_pagenation_list)
        div_pagination_info = soup.find("div", class_="pagination-page-info")
        if div_pagination_info:
            div_pagination_info_text = div_pagination_info.get_text(strip=True)
            # pk_print(f'''div_pagination_info_text={div_pagination_info_text}  {'%%%FOO%%%' if LTA else ''}''')
            pattern = r"results (\d+-\d+) out of (\d+) results"
            match = re.search(pattern, div_pagination_info_text)
            if match:
                cnt_part_of_results = match.group(1)  # "976-1000"
                cnt_total_of_results = match.group(2)  # "1000"
                pk_print(
                    f'''max_page_number_in_pagenation={page_number_max_in_pagenation} cnt_part_of_results={cnt_part_of_results}  cnt_total_of_results={cnt_total_of_results}  {'%%%FOO%%%' if LTA else ''}''')
                if cnt_part_of_results.split('-')[1] == cnt_total_of_results:
                    page_number_last = page_number_max_in_pagenation
                    return page_number_last
                else:
                    page_number_max_in_pagenation = page_number_max_in_pagenation + 1
