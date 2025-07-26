from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical


def get_magnets_set_from_torrent_qq(search_keyword, driver=None):
    try:
        import traceback
        import random
        import re
        from bs4 import BeautifulSoup

        from colorama import init as pk_colorama_init
        colorama_init_once()

        magnet_link_set = set()
        ensure_printed(f'''search_keyword={search_keyword}  {'%%%FOO%%%' if LTA else ''}''')

        if search_keyword == "":
            ensure_printed(f"search_keyword is blank")
            return magnet_link_set

        if driver is None:
            # [OPTION]
            driver = get_driver_selenium_solved_cloudflare_sequrity(headless_mode=True)
            # driver = get_driver_selenium_solved_cloudflare_sequrity(headless_mode=False)

        mgt_url = None
        # solve cloudflare sequrity
        url = "https://torrentqq348.com"
        # open_url_with_reconnect(driver=driver, url = url, reconnect_time=10) # fail
        driver.uc_open_with_reconnect(url, reconnect_time=10)
        # driver_get_url_in_browser_and_wait_loaded(url=url, driver=driver) #fail
        driver_get_url_in_browser(url=url, driver=driver, seconds_s=1000, seconds_e=1500)
        body = get_bs4_element_ResultSet(driver=driver, tag_n="body")
        str_negative = '잠시만 기다려'
        if str_negative in body:
            ensure_printed(f'''cloudflare sequrity  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            return magnet_link_set

        # search "torrentqq347.com" in browser
        url = f'https://torrentqq356.com/search?q={search_keyword}'
        url_encoded = get_str_encoded_url(str_working=url)
        ensure_printed(f'''url={url:20}  url_encoded={url_encoded:20} {'%%%FOO%%%' if LTA else ''}''')
        # driver_get_url_in_browser_and_wait_loaded(url=url, driver=driver) #fail
        driver_get_url_in_browser(url=url, driver=driver)  # go to list page
        div_row_at_row = get_bs4_element_ResultSet(driver=driver, tag_n="div", class_n="row at-row")
        # ensure_printed(f'''div_row_at_row={div_row_at_row}  {'%%%FOO%%%' if LTA else ''}''')

        # move to detail page
        detail_page_link_list = []
        a_tag_list = get_bs4_element_ResultSet(driver=driver, tag_n="a")
        for a_tag_str in a_tag_list:
            title = a_tag_str.get('title')
            href = a_tag_str.get('href')
            if title and href:
                detail_page_link_list.append((title, href))
        keywords_required = search_keyword.split(" ")
        detail_page_link_matched_list = []
        for title, href in detail_page_link_list:
            ensure_printed(f'''title={title:80s}  href={href}''')
            detail_page_link_matched_list.append((title, href))
        # print_iterable_as_vertical(item_iterable=detail_page_link_list, item_iterable_n="detail_page_link_list")
        if len(detail_page_link_matched_list) == 0:
            ensure_printed(f'''detail page links not matched  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            return magnet_link_set
        print_iterable_as_vertical(item_iterable=detail_page_link_matched_list, item_iterable_n="link_matched_list")
        for title, href in detail_page_link_matched_list:
            # driver_get_url_as_browser_tab_via_js(driver, href)
            ensure_printed(
                f'''driver.title={driver.title} keywords_required={keywords_required} {'%%%FOO%%%' if LTA else ''}''')
            if not is_all_included_in_prompt(prompt=title, txt_list=keywords_required):
                continue
            driver_get_url_in_browser(url=href, driver=driver)  # go to detail page
            kill_tabs_except_current_tab_via_selenium(driver)
            body = get_bs4_element_ResultSet(driver=driver, tag_n="body")
            string_negative = '잠시만 기다리십시오…torrentqq'
            if string_negative in body:
                ensure_printed(f'''{string_negative} in bs4_element_ResultSet ''', print_color='red')
                continue
            href_list = []
            title_list = []
            detail_page_link_list = []
            onclick_list = []
            class_list = []
            txt_inner_list = []
            a_tag_list = get_bs4_element_ResultSet(driver=driver, tag_n="a")
            for a_tag_str in a_tag_list:
                title = a_tag_str.get('title')
                href = a_tag_str.get('href')
                onclick = a_tag_str.get('onclick')
                a_class = a_tag_str.get('class')
                txt_inner = a_tag_str.get_text(strip=True)
                title_list.append(title)
                href_list.append(href)
                onclick_list.append(onclick)
                class_list.append(a_class)
                txt_inner_list.append(txt_inner)
                if a_class is not None and "btn-magnet" in a_class and onclick:  # 둘 다 존재할 때만 리스트에 추가
                    detail_page_link_list.append((txt_inner, a_class, onclick))
            search_keyword_without_useless = search_keyword.strip()
            search_keyword_without_useless = search_keyword_without_useless.replace(" > 영화 토렌트", "")
            search_keyword_without_useless = search_keyword_without_useless.replace("영화 토렌트", "")
            search_keyword_without_useless = search_keyword_without_useless.replace("방송 토렌트", "")
            search_keyword_without_useless = search_keyword_without_useless.replace(" - 토렌트큐큐", "")
            # search_keyword_without_useless = search_keyword_without_useless.replace(" - TORRENTQQ","")
            for txt_inner, a_class, onclick in detail_page_link_list:
                mgt_url = driver.current_url
                base_url = get_base_url(mgt_url)
                onclick = onclick
                magnet_path = re.search(r"'(.+?)'", onclick)
                if magnet_path:
                    mgt_url = f"{base_url}{magnet_path.group(1)}"
                    ensure_printed(f'''mgt_url={mgt_url}  {'%%%FOO%%%' if LTA else ''}''')
                    # driver_get_url_in_browser(url=href, driver=driver)
                    # kill_tabs_except_current_tab_via_selenium(driver)  # 나머지 탭 닫기
                    script_tag_list = get_bs4_element_ResultSet(driver=driver, tag_n="script")
                    for script_tag in script_tag_list:
                        ensure_printed(f'''script_tag={script_tag}  {'%%%FOO%%%' if LTA else ''}''')
                        if script_tag and "magnet:?" in script_tag.text:
                            magnet_link = script_tag.text.split('"')[1]
                            magnet_url_customed = f"{magnet_link}&dn={search_keyword_without_useless}"
                            ensure_printed(f'''magnet_url_customed={magnet_url_customed:80s}  {'%%%FOO%%%' if LTA else ''}''')
                            magnet_link_set.add(magnet_url_customed)
                        else:
                            if mgt_url and "/magnet/" in mgt_url:
                                magnet_url_customed = f"{driver.title}&mgt_url={mgt_url}"
                                ensure_printed(f'''magnet_url_customed={magnet_url_customed}  {'%%%FOO%%%' if LTA else ''}''')
                                magnet_link_set.add(magnet_url_customed)
                            else:
                                ensure_printed(f'''magnet_link not found''', print_color='red')

                else:
                    ensure_printed(f'''magnet_link does not exist''', print_color='red')
                break
        print_iterable_as_vertical(item_iterable=magnet_link_set, item_iterable_n="magnet_link_set")

        # debug

        # sleep(hours=1)

        return magnet_link_set
    except:
        traceback.print_exc()
        import sys
        traceback.print_exc(file=sys.stdout)
