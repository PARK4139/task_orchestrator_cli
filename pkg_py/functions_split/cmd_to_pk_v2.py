

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def pk_ensure_pk_system_started_v2(index_map):
    #
    # , guide_pk_error_mssage
    try:
        import sys
        import os

        import glob

        if LTA:
            pk_print(f"len(sys.argv)={len(sys.argv)} {'%%%FOO%%%' if LTA else ''}")

        if len(sys.argv) == 1:
            if LTA:
                pk_print(f'인자가 {len(sys.argv)}개 입력되었습니다 {"%%%FOO%%%" if LTA else ""}')
            print_pk_ls(index_map=index_map)  # 업데이트 필요
            return

        if len(sys.argv) >= 2:
            arg1 = sys.argv[1]

            if arg1 in ['--version', '-v', 'ver']:
                print_pk_ver()
                return
            elif arg1 in ['--list', '-l', 'ls']:
                print_pk_ls(index_map=index_map)
                return

            # STEP 2: index로 pk 프로그램 실행
            if arg1 in index_map:
                pk_file_to_run = index_map[arg1]
                if LTA:
                    pk_print(f"[INFO] 실행할 파일: {pk_file_to_run}")
                run_pk_python_program_by_path(pk_file_to_run, sys.argv[2:])
                return
            else:
                if not arg1.isdigit():

                    # 문자열 기반 추측 지원
                    guide_to_use_pk_system_process(get_pk_system_process_pnx_list(), nx_by_user_input=arg1)
                else:
                    guide_pk_error_mssage()
                return

    except Exception:
        import traceback
        traceback.print_exc()
