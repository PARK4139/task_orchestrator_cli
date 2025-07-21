

import win32con
import platform
import math
from selenium.webdriver.common.action_chains import ActionChains
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_100_performance_logic import pk_measure_seconds

from dirsync import sync
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def assist_to_find_pnx_list_like_everything():
    # 기존의 파일과 디렉토리 목록에 없는 부분만 추가적으로 DB 에 저장
    # DB 에 저장 모든 파일과 디렉토리 목록을 idx 와 함꼐 출력
    #
    # pk {idx} 를 입력 하면 idx 에 해당하는 파일 또는 디렉토리를 open
    # open 시 디렉토리라면 explorer.exe 를 통해서 열고
    # open 시 파일이라면 확장자에 따라서 지정된 파일로 연다. 지정되지 않은 확장자라면 code.exe 로 연다.
    def get_pnx_list_from_pk_everything_db():
        # input()
        # '''select * from %{}%'''
        pass

    def open_pnx(idx):
        pnx = get_pnx_from_pk_everything_db(idx=idx)
        if is_d(pnx):
            cmd_to_os(f'explorer.exe {pnx}')
        else:
            x = get_x(pnx)
            if x == '.py':
                cmd_to_os(f'code {pnx}')
            else:
                pk_print(f'''아직 행위가 정의되지 않은 확장자입니다. {x} {'%%%FOO%%%' if LTA else ''}''')

    def get_pnx_from_pk_everything_db(idx):
        # input()
        # '''select * from %{}%'''
        pass

    @pk_measure_seconds
    def update_pk_everything_db():
        pass

    update_pk_everything_db()  # monitoring 을 통해서 업데이트를 수행하면 어떨까?

    while 1:
        d_working = input('탐색할 디렉토리를 입력하세요')
        pass

    # pnx_interested_list = [
    #     # rf'{USERPROFILE}\AppData\Roaming\bittorrent',
    # ]
    # string_exclude = [
    #     rf'.dat',
    #     rf'.dll',
    #     rf'.exe',
    #     rf'.dmp',
    #     rf'.lng',
    # ]
    # pnx_list = get_pnx_list_interested_from_file_system(pnx_interested_list=pnx_interested_list, string_exclude=string_exclude)
    # pnx_list = get_list_interested_from_list(working_list=pnx_list,  extension_list_include=[".torrent"])
    # print_list_as_vertical(working_list=pnx_list, working_list_n="pnx_list")
    # string_list_include_any = [
    #     'ONE PIECE - 1123',
    #     'Boku no Hero Academia - 160',
    #     'Re Zero kara Hajimeru Isekai Seikatsu - 59',
    #     'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka S5 - 09',
    #     'Dragon Ball Daima - 08',
    #     'Sword Art Online Alternative - Gun Gale Online S2 - 09',
    #     'Ao no Exorcist - Yuki no Hate-hen - 09',
    #     'Dandadan - 11',
    #     'Amagami-san Chi no Enmusubi - 10',
    #     'Seirei Gensouki 2 - 01',
    # ]
    # pnx_list = get_list_interested_from_list(working_list=pnx_list,  string_list_include_any=string_list_include_any)
    # print_list_as_vertical(working_list=pnx_list, working_list_n="pnx_list")

    # 탐색기 # 전체영역검색
    # get_pnx_list_found_from_file_system()
    # find_pnx_interested_list_from_text_file(including_texts=["심야 괴담회", "심야괴담회"], exclude_texts=[], including_extensions=[".torrent"], except_extensions=[])
    # pnxs_required = get_found_pnx_interested_list_from_text_file(including_texts=["심야 괴담회", "심야괴담회"], exclude_texts=[], including_extensions=[".torrent"], except_extensions=[])
    # pnxs_required = get_list_replaced_element_from_str_to_str(items=pnxs_required, from_str="심야 괴담회", to_str="심야괴담회")
    # pnxs_required = get_list_replaced_element_from_str_to_str(items=pnxs_required, from_str=rf"%USERPROFILE%\AppData\Roaming\bittorrent", to_str="")
    # pnxs_required = get_list_replaced_element_from_str_to_str(items=pnxs_required, from_str="시즌4", to_str="4")
    # pnxs_required = get_list_replaced_element_from_str_to_str(items=pnxs_required, from_str="심야괴담회 4", to_str="심야괴담회4")
    # pnxs_required = get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.720p-NEXT")
    # pnxs_required = get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.1080p-NEXT")
    # pnxs_required = get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.1080p\.WANNA")
    # pnxs_required = get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.1080p\.H264-F1RST")
    # pnxs_required = get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=rf"^\\") # \로 시작하는 부분 삭제
    # pnxs_required = get_list_removed_element_duplicated(items=pnxs_required)
    # pnxs_required = get_list_sorted_element(items=pnxs_required, mode="asc")
    # print_list_as_vertical(working_list=pnxs_required, items_name="pnxs_required")
    # pnxs_required = get_found_pnx_interested_list_from_text_file(including_texts=["ONE PIECE", "ONEPIECE", "one piece", "onepiece", "One Piece", "Onepiece"], exclude_texts=[], including_extensions=[], except_extensions=[".torrent",".jpg",".jpeg",".png",".PNG"])
    # pnxs_required = get_list_replaced_element_from_str_to_str(items=pnxs_required, from_str="ONE PIECE", to_str="ONEPIECE")
    # pnxs_required = get_list_replaced_element_from_str_to_str(items=pnxs_required, from_str="ONEPIECE 4", to_str="ONEPIECE4")
    # pnxs_required = get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.720p-NEXT")
    # pnxs_required = get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.1080p-NEXT")
    # pnxs_required = get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.1080p\.WANNA")
    # pnxs_required = get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.1080p\.H264-F1RST")
    # pnxs_required = get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=rf"^\\") # \로 시작하는 부분 삭제
    # pnxs_required = get_list_removed_element_duplicated(items=pnxs_required)
    # pnxs_required = get_list_sorted_element(items=pnxs_required, mode="asc")
    # print_list_as_vertical(working_list=pnxs_required, items_name="pnxs_required")
    # pk_print(string = rf'''len(pnxs_required)="{len(pnxs_required)}"  {'%%%FOO%%%' if LTA else ''}''')
    pass
