import logging

from functions.ensure_drag_changed_printed import get_list_striped_element
from functions.get_list_contained_with_stamp_from_f import get_list_contained_with_stamp_from_f
from functions.get_list_deduplicated import get_list_deduplicated
from functions.get_list_from_f import get_list_from_f
from functions.get_list_removed_element_contain_prompt import get_list_removed_element_contain_prompt
from functions.get_list_removed_element_empty import get_list_removed_empty
from functions.get_list_url_decoded_element import get_list_url_decoded_element
from functions.get_magnets_set_from_torrent_qq import get_magnets_set_from_torrent_qq
from functions.is_internet_connected import is_internet_connected
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.objects.pk_local_test_activate import LTA
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE


def collect_magnets_from_torrentqq(search_keyword=None, driver=None, via_f_txt=True):
    import sys

    import traceback

    try:
        if not is_internet_connected():
            raise

        collect_magnets_from_nyaa_si_txt = rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/collect_magnets_from_nyaa_si.txt'
        magnets_set = set()

        # [OPTION]
        # window_title_seg = get_nx(collect_magnets_from_nyaa_si_txt)
        # if not is_window_opened(window_title_seg=window_title_seg):
        # ensure_pnx_opened_by_ext(pnx=f_func_n_txt)
        # move_window_to_front(window_title_seg=window_title_seg)
        # ensure_command_executed(cmd=rf'explorer "{f_func_n_txt}" ', debug_mode=True, mode="a")

        # [OPTION]
        # search_keyword = search_keyword
        # search_keyword ="________________"
        # search_keyword = input_validated("serch_keyword")

        # [OPTION]
        # filtered_list.append(search_keyword)
        filtered_list = get_list_contained_with_stamp_from_f(f=collect_magnets_from_nyaa_si_txt, STAMP='[ TORRENTQQ ]')

        # 전처리
        logging.debug(f'''search_keyword_list={filtered_list}  {'%%%FOO%%%' if LTA else ''}''')
        filtered_list = get_list_removed_element_contain_prompt(working_list=filtered_list,
                                                                prompt="#")  # 시작 문자가 '#'인 요소를 remove
        logging.debug(f'''search_keyword_list={filtered_list}  {'%%%FOO%%%' if LTA else ''}''')
        filtered_list = get_list_striped_element(working_list=filtered_list)
        logging.debug(f'''search_keyword_list={filtered_list}  {'%%%FOO%%%' if LTA else ''}''')
        filtered_list = get_list_removed_empty(working_list=filtered_list)
        logging.debug(f'''search_keyword_list={filtered_list}  {'%%%FOO%%%' if LTA else ''}''')
        filtered_list = get_list_deduplicated(working_list=filtered_list)
        logging.debug(f'''search_keyword_list={filtered_list}  {'%%%FOO%%%' if LTA else ''}''')
        ensure_iterable_log_as_vertical(item_iterable=filtered_list, item_iterable_n='search_keyword_list')
        logging.debug(rf'''len(search_keyword_list)="{len(filtered_list)}"  {'%%%FOO%%%' if LTA else ''}''')

        # if driver is None:
        #     driver = get_driver_selenium_solved_cloudflare_sequrity()
        # get_driver_selenium_solved_cloudflare_sequrity() 재사용하면 magnet_link not found

        for search_keyword in filtered_list:
            # magnets_set = magnets_set | get_magnets_set_from_torrent_qq(search_keyword=search_keyword, driver=driver)# fail
            magnets_set = magnets_set | get_magnets_set_from_torrent_qq(search_keyword=search_keyword)

            # save magnets collected
            magnets_txt = rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/pk_magnets.txt'
            magnets_list = get_list_url_decoded_element(magnets_set)
            magnets_list = [magnet for magnet in sorted(magnets_list, key=lambda magnet: magnet.split("&dn=")[
                1] if "&dn=" in magnet else "")]
            magnets_list = [magnet for magnet in sorted(magnets_list, key=lambda magnet: magnet.split("&mgt_url=")[
                1] if "&mgt_url=" in magnet else "")]
            ensure_list_written_to_f(f=magnets_txt, working_list=magnets_list, mode="a")

            # magnets 중복remove
            magnets_list = get_list_from_f(f=magnets_txt)
            magnets_list = get_list_striped_element(working_list=magnets_list)
            magnets_list = get_list_removed_empty(working_list=magnets_list)
            magnets_list = get_list_deduplicated(working_list=magnets_list)
            ensure_list_written_to_f(f=magnets_txt, working_list=magnets_list, mode="w")

        # search_keyword_list 목록추가, search_keyword_list 중복remove
        filtered_list = get_list_from_f(f=collect_magnets_from_nyaa_si_txt) + filtered_list
        filtered_list = get_list_striped_element(working_list=filtered_list)
        filtered_list = get_list_removed_empty(working_list=filtered_list)
        filtered_list = get_list_deduplicated(working_list=filtered_list)
        ensure_list_written_to_f(f=collect_magnets_from_nyaa_si_txt, working_list=filtered_list, mode="w")

    except:
        traceback.print_exc(file=sys.stdout)
