

import sys
import traceback

from colorama import init as pk_colorama_init

from pkg_py.functions_split.get_driver_selenium import get_driver_selenium

# from pkg_py.system_object.500_live_logic import ensure_magnets_collected_from_nyaa_si_p1, get_historical_list, ensure_pnx_made, get_driver_selenium
#, '[ TRY GUIDE ]', D_PROJECT, '[ UNIT TEST EXCEPTION DISCOVERED ]'
#, print_red

ensure_colorama_initialized_once()

if __name__ == "__main__":
    try:
        driver = get_driver_selenium(browser_debug_mode=False)
        # collect_magnet_set_from_nyaa_si(via_f_txt=True, driver=driver)

        import inspect

        func_n = inspect.currentframe().f_code.co_name
        ensure_pnx_made(pnx=rf'historical_{func_n}.txt', mode='f')
        historical_search_keyword_list = get_historical_list(f=rf'historical_{func_n}.txt')
        # option_values = ['', '1080 [Batch]'] + historical_search_keyword_list
        # search_keyword = get_value_completed(message='search_keyword=', option_values=option_values).strip()
        # nyaa_si_supplier = get_value_completed(message='nyaa_si_supplier=', option_values=['SubsPlease', '', 'Erai-raws'])
        search_keyword = ''  # pk_test
        nyaa_si_supplier = 'SubsPlease'  # pk_test
        ensure_magnets_collected_from_nyaa_si_p1(nyaa_si_supplier=nyaa_si_supplier, search_keyword=search_keyword, driver=driver)

    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
