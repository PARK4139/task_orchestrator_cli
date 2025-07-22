

from selenium.webdriver.common.action_chains import ActionChains
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.PkMessages2025 import PkMessages2025
from concurrent.futures import ThreadPoolExecutor

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def upzip_pnx(pnx):
    import os
    import traceback

    try:
        while 1:
            # 전처리
            pnx = pnx.replace("\n", "")
            pnx = pnx.replace("\"", "")

            if pnx.strip() == "":
                pk_print(working_str="백업할 대상이 입력되지 않았습니다")
                break

            pnx_dirname = os.path.dirname(pnx)
            pnx_basename = os.path.basename(pnx).split(".")[0]
            target_zip = rf'{pnx_dirname}\{pnx_basename}.zip'

            pk_chdir(pnx_dirname)

            if os.path.exists(target_zip):
                # cmd=f'bandizip.exe bx "{target_zip}"'
                cmd = f'bz.exe x -aoa "{target_zip}"'  # x 는 경로 보존, -aoa :Overwrite All existing files without prompt
                cmd_to_os_like_person_as_admin(cmd)
                if os.path.exists(pnx):
                    cmd = rf'echo y | del /f "{target_zip}"'
                    cmd_to_os_like_person_as_admin(cmd)
                else:
                    pk_print("압축해제 후 압축f을 삭제에 실패")
            else:
                pk_print("압축해제할 f이 없었습니다")
            pk_chdir(D_PROJECT)
            print_success("압축해제 성공")
            break
    except:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        pk_chdir(D_PROJECT)
