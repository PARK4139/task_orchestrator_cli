from sources.functions.get_historical_list import get_historical_list


def collect_magnet_set():
    driver = get_driver_selenium(browser_debug_mode=False)
    # collect_magnet_set_from_nyaa_si(via_f_txt=True, driver=driver)

    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    ensure_pnx_made(pnx=rf'historical_{func_n}.txt', mode='f')
    historical_search_keyword_list = get_historical_list(f=rf'historical_{func_n}.txt')
    # option_values = ['', '1080 [Batch]'] + historical_search_keyword_list
    # search_keyword = ensure_value_completed(message='search_keyword=', option_values=option_values).strip()
    # nyaa_si_supplier = ensure_value_completed(message='nyaa_si_supplier=', option_values=['SubsPlease', '', 'Erai-raws'])
    search_keyword = ''  # pk_test
    nyaa_si_supplier = 'SubsPlease'  # pk_test
    ensure_magnets_collected_from_nyaa_si_p1(nyaa_si_supplier=nyaa_si_supplier, search_keyword=search_keyword, driver=driver)

    # collect_magnets_from_torrentqq(via_f_txt=True, driver=driver)
