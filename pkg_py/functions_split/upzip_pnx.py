

from selenium.webdriver.common.action_chains import ActionChains
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.map_massages import PkMessages2025
from concurrent.futures import ThreadPoolExecutor

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def upzip_pnx(pnx):
    import os
    import traceback

    try:
        while 1:
            # 전처리
            pnx = pnx.replace("\n", "")
            pnx = pnx.replace("\"", "")

            if pnx.strip() == "":
                ensure_printed(str_working="백업할 대상이 입력되지 않았습니다")
                break

            pnx_dirname = os.path.dirname(pnx)
            pnx_basename = os.path.basename(pnx).split(".")[0]
            target_zip = rf'{pnx_dirname}\{pnx_basename}.zip'

            os.chdir(pnx_dirname)

            if os.path.exists(target_zip):
                # cmd=f'bandizip.exe bx "{target_zip}"'
                cmd = f'bz.exe x -aoa "{target_zip}"'  # x 는 경로 보존, -aoa :Overwrite All existing files without prompt
                ensure_command_excuted_to_os_like_person_as_admin(cmd)
                if os.path.exists(pnx):
                    cmd = rf'echo y | del /f "{target_zip}"'
                    ensure_command_excuted_to_os_like_person_as_admin(cmd)
                else:
                    ensure_printed("압축해제 후 압축f을 삭제에 실패")
            else:
                ensure_printed("압축해제할 f이 없었습니다")
            os.chdir(D_PROJECT)
            print_success("압축해제 성공")
            break
    except:
        ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        os.chdir(D_PROJECT)
