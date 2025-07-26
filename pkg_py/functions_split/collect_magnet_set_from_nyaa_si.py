from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.system_object.directories import D_PKG_TXT
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_historical_list import get_historical_list


def collect_magnet_set_from_nyaa_si(search_keyword=None, driver=None, via_f_txt=False, via_input=False):
    import inspect

    from urllib.parse import unquote, urlparse, parse_qs

    func_n = inspect.currentframe().f_code.co_name

    if not is_internet_connected():
        raise

    f = rf'{D_PKG_TXT}/pk_magnets.txt'
    ensure_pnx_made(pnx=f, mode="f")
    # answer = get_value_completed(message=f'can i open {get_nx(f)} (o/x)=', option_values=['o', 'x'])
    # if is_os_windows():
    #     if answer == 'o':
    #         cmd_to_os(cmd=rf'explorer "{get_pnx_windows_style(f)}"', mode="a")
    # else:
    #     ensure_printed(str_working=rf'''{get_pnx_unix_style(f)}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
    #     pass # todo

    f_func_n_txt = rf'{D_PROJECT}\pkg_txt\{func_n}.txt'
    ensure_pnx_made(pnx=f_func_n_txt, mode="f")
    # window_title_seg = get_nx(f_func_n_txt)

    # include_elements_all = ['1080']
    # include_elements_any = ['SubsPlease', 'Moozzi']
    # exclude_elements_all = ["[New-raws]", "[LoliHouse]", "[Erai-raws]", "[Koi-Raws]", '[EMBER]', '[Lilith-Raws]', '[Yameii]', '[ASW]', '[shincaps]', '[AsukaRaws]']
    magnets_set = set()
    search_keyword_list = []

    ensure_pnx_made(pnx=rf'historical_{func_n}.txt', mode='f')
    historical_search_keyword_list = get_historical_list(f=rf'historical_{func_n}.txt')
    option_values = ['', '1080 [Batch]'] + historical_search_keyword_list
    search_keyword = get_value_completed(key_hint='search_keyword=', values=option_values)
    search_keyword = search_keyword.strip()
    ensure_list_written_to_f(f=rf'historical_{func_n}.txt', working_list=[search_keyword] + historical_search_keyword_list,
                             mode="w")

    search_keyword = search_keyword.strip()
    search_keyword_list.append(search_keyword)

    # if via_f_txt:
    #     ensure_printed(f'''mode is via_f_txt mode''')
    #     ensure_printed(f'''via_f_txt={via_f_txt}  {'%%%FOO%%%' if LTA else ''}''')
    #     search_keyword_list = get_list_from_f(f=f_func_n_txt)
    #     search_keyword_list = get_list_removed_element_contain_prompt(working_list=search_keyword_list, prompt="#")
    #     search_keyword_list = get_list_replaced_element_from_str_to_str(working_list=search_keyword_list, from_str='pk_ani ', to_str='')
    #     search_keyword_list = get_list_replaced_element_from_str_to_str(working_list=search_keyword_list, from_str='pk_movie ', to_str='')
    #     search_keyword_list = get_list_replaced_element_from_str_to_str(working_list=search_keyword_list, from_str='pk_music ', to_str='')

    ensure_printed(f'''len(search_keyword_list)={len(search_keyword_list)}  {'%%%FOO%%%' if LTA else ''}''')
    # print_iterable_as_vertical(item_iterable=search_keyword_list, item_iterable_n="search_keyword_list")

    search_keyword_list = get_list_striped_element(working_list=search_keyword_list)
    search_keyword_list = get_list_deduplicated(working_list=search_keyword_list)

    if driver is None:
        driver = get_driver_selenium(browser_debug_mode=False)

    nyaa_si_supplier = get_value_completed(key_hint='nyaa_si_supplier=', values=['SubsPlease', '', 'Erai-raws'])
    magnets_set = magnets_set | get_magnets_set_from_nyaa_si(nyaa_si_supplier=nyaa_si_supplier,
                                                             search_keyword=search_keyword, driver=driver)

    magnets_set_filtered = set()

    positive_filter_keywords = get_value_completed(key_hint='positive_filter_keywords=', values=['1080'])
    for magnet in magnets_set:
        decoded_magnet = unquote(magnet)
        parsed = urlparse(decoded_magnet)
        qs = parse_qs(parsed.query)
        dn = qs.get('dn', [''])[0]
        if all(keyword in dn for keyword in positive_filter_keywords):
            magnets_set_filtered.add(magnet)
    magnets_set = magnets_set_filtered
    ensure_printed(f'''len(magnets_set)={len(magnets_set)}  {'%%%FOO%%%' if LTA else ''}''', print_color="green")

    magnets_set_filtered = set()
    negative_filter_keywords = [
        "Yami Shibai 8",
        "Yami Shibai 9",
        "360p",
        "720p",
        "480p",
    ]
    print_iterable_as_vertical(item_iterable=negative_filter_keywords, item_iterable_n="negative_filter_keywords")
    for magnet in magnets_set:
        decoded_magnet = unquote(magnet)
        parsed = urlparse(decoded_magnet)
        qs = parse_qs(parsed.query)
        dn = qs.get('dn', [''])[0]
        if not any(keyword in dn for keyword in negative_filter_keywords):
            magnets_set_filtered.add(magnet)
    magnets_set = magnets_set_filtered

    f = rf'{D_PKG_TXT}/pk_magnets.txt'
    magnets_list = get_list_url_decoded_element(magnets_set)
    magnets_list = [magnet for magnet in
                    sorted(magnets_list, key=lambda magnet: magnet.split("&dn=")[1] if "&dn=" in magnet else "")]
    ensure_list_written_to_f(f=f, working_list=magnets_list, mode="a")

    # magnets 중복remove
    magnets_list = get_list_from_f(f=f)
    magnets_list = get_list_striped_element(working_list=magnets_list)
    magnets_list = get_list_removed_empty(working_list=magnets_list)
    magnets_list = get_list_deduplicated(working_list=magnets_list)
    ensure_list_written_to_f(f=f, working_list=magnets_list, mode="w")

    # search_keyword_list 목록추가, search_keyword_list 중복remove
    search_keyword_list = get_list_from_f(f=f_func_n_txt) + search_keyword_list
    search_keyword_list = get_list_striped_element(working_list=search_keyword_list)
    search_keyword_list = get_list_removed_empty(working_list=search_keyword_list)
    search_keyword_list = get_list_deduplicated(working_list=search_keyword_list)
    ensure_list_written_to_f(f=f_func_n_txt, working_list=search_keyword_list, mode="w")
