

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.get_pk_system_process_available_idx_list import get_pk_system_process_available_idx_list
from pkg_py.functions_split.run_pk_system_process_by_idx import run_pk_system_process_by_idx
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.print_pk_ls import print_pk_ls
from pkg_py.functions_split.get_pk_system_process_pnxs import get_pk_system_process_pnxs
from pkg_py.functions_split.guide_pk_error_mssage import guide_pk_error_mssage
from pkg_py.functions_split.guide_to_use_pk_system_process import guide_to_use_pk_system_process
from pkg_py.functions_split.print_pk_ver import print_pk_ver


def ensure_pk_system_started_v1(index_map):
    try:
        import sys

        import sys
        import os

        import glob

        pk_system_process_available_idx_list = get_pk_system_process_available_idx_list()
        if LTA:
            ensure_printed(f'''len(sys.argv)={len(sys.argv)} {'%%%FOO%%%' if LTA else ''}''')
        if len(sys.argv) == 1:
            if LTA:
                ensure_printed(f'인자가 {len(sys.argv)}개 입력되었습니다 {'%%%FOO%%%' if LTA else ''}')
            print_pk_ls(index_map=index_map)
        elif len(sys.argv) == 2:
            if LTA:
                ensure_printed(f'인자가 {len(sys.argv)}개 입력되었습니다 {'%%%FOO%%%' if LTA else ''}')
            if sys.argv[1] in ['--version', '-v', 'ver']:
                print_pk_ver()
            elif sys.argv[1] in ['--list', '-l', 'ls']:
                print_pk_ls(index_map=index_map)
            elif sys.argv[1] in pk_system_process_available_idx_list:
                run_pk_system_process_by_idx(pk_idx=int(sys.argv[1]), pk_arg_list=sys.argv)
            else:
                if not str.isdigit(sys.argv[1]):

                    guide_to_use_pk_system_process(pk_system_process_pnx_list=get_pk_system_process_pnxs(), nx_by_user_input=sys.argv[1])
                else:
                    guide_pk_error_mssage()

        elif len(sys.argv) == 3:
            # todo : pk ass sche 인자 2개로 검색 후 출력
            if LTA:
                ensure_printed(f'인자가 {len(sys.argv)}개 입력되었습니다 {'%%%FOO%%%' if LTA else ''}')
            if sys.argv[1] in pk_system_process_available_idx_list:
                run_pk_system_process_by_idx(pk_idx=int(sys.argv[1]), pk_arg_list=sys.argv)
    except:
        import traceback
        traceback.print_exc()
        import sys
        traceback.print_exc(file=sys.stdout)
