

from pkg_py.functions_split.ensure_printed import ensure_printed


def collect_magnet_set_from_nyaa_si_p1(nyaa_si_supplier, search_keyword, driver=None):
    init_db_container()  # DB 컨테이너 & 테이블 자동 ensure
    import random, math
    from bs4 import BeautifulSoup
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait

    from urllib.parse import urlparse, parse_qs, unquote

    def get_db_conn():
        import mysql.connector
        host = get_pk_config("db_host", "127.0.0.1")
        user = get_pk_config("db_user", "root")
        pwd = get_pk_config("db_password", "example")
        db = get_pk_config("db_name", "nyaa_db")
        port = int(get_pk_config("db_port", "3306"))
        return mysql.connector.connect(
            host=host, user=user, password=pwd, database=db, port=port
        )

    # batch insert 함수
    def save_magnets_batch(magnets):

        #
        ensure_printed(f"Saving {len(magnets)} magnets to MariaDB")
        conn = get_db_conn()
        cur = conn.cursor()
        # magnet 링크에서 title 파싱
        data = [(m, parse_qs(urlparse(unquote(m)).query).get("dn", [""])[0]) for m in magnets]
        cur.executemany(
            "INSERT IGNORE INTO nyaa_magnets(magnet,title) VALUES(%s,%s)", data
        )
        conn.commit()
        cur.close()
        conn.close()
        ensure_printed("Batch saved")

    ensure_printed("Starting crawl")
    driver = driver or get_driver_selenium(browser_debug_mode=False)
    base = f"https://nyaa.si/user/{nyaa_si_supplier}?f=0&c=0_0&q={get_str_encoded_url(search_keyword)}"
    driver.get(base)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    total = get_total_cnt_of_f_torrent_list(soup.find("h3").text.strip())
    pages = math.ceil(total / 75) if total else get_page_number_last_of_nyaa_si_page(base, driver)
    start = 1
    end = 2
    batch = []
    for p in range(start, end + 1):
        try:
            driver.get(f"{base}&p={p}")
            WebDriverWait(driver, 10).until(lambda d: d.find_element(By.TAG_NAME, "body"))
            found = {a["href"] for a in BeautifulSoup(driver.page_source, "html.parser").find_all("a", href=True) if
                     a["href"].startswith("magnet:")}
            ensure_printed(f"Page {p}: {len(found)} magnets")
            batch.extend(found)
            if len(batch) >= 2000:
                save_magnets_batch(batch)
                batch.clear()
            ensure_slept(milliseconds=random.randint(200, 333))
        except Exception as e:
            ensure_printed(f"Error page {p}: {e}", print_color="red")
    if batch:
        save_magnets_batch(batch)
    ensure_printed("Done collecting", print_color="green")
    return None
