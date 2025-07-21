

import paramiko
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT


from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def compress_pnx_via_bz(pnx):
    import inspect
    import os
    import re
    import shutil
    import traceback

    from datetime import datetime
    func_n = inspect.currentframe().f_code.co_name
    try:
        while 1:
            ment = rf"백업 {pnx}"
            pk_print(f" {'%%%FOO%%%' if LTA else ''} {ment}", )

            # 전처리
            pnx = pnx.replace("\n", "")
            pnx = pnx.replace("\"", "")

            if pnx.strip() == "":
                pk_speak_v2(working_str="백업할 대상이 입력되지 않았습니다", comma_delay=0.98)
                break

            target_dirname = os.path.dirname(pnx)
            target_dirname_dirname = os.path.dirname(target_dirname)
            target_basename = os.path.basename(pnx).split(".")[0]
            target_zip = rf'{target_dirname}\$zip_{target_basename}.zip'
            target_yyyy_mm_dd_hh_mm_ss_zip_basename = rf'{target_basename} - {get_time_as_("%Y %m %d %H %M %S")}.zip'
            pk_print(f"pnx : {pnx}")
            pk_print(f"target_dirname : {target_dirname}")
            pk_print(f"target_dirname_dirname : {target_dirname_dirname}")
            pk_print(f"target_basename : {target_basename}")
            pk_print(f"target_zip : {target_zip}")
            pk_print(f"target_yyyy_mm_dd_HH_MM_SS_zip_basename : {target_yyyy_mm_dd_hh_mm_ss_zip_basename}")

            cmd = f'bz.exe c "{target_zip}" "{pnx}"'
            cmd_to_os(cmd=cmd)

            cmd = rf'ren "{target_zip}" "{target_yyyy_mm_dd_hh_mm_ss_zip_basename}"'
            cmd_to_os(cmd=cmd)

            # f이 위치한 드라이브로 이동
            drives = [
                "C",
                "D",
                "E",
                "F",
                "G",
            ]
            drive_where_target_is_located = pnx.split(":")[0].upper()
            for drive in drives:
                if (drive_where_target_is_located == drive):
                    os.system(rf"cd {drive}:")
            try:
                pk_chdir(target_dirname)
            except:
                pk_speak_v2(working_str="경로를 이해할 수 없습니다", comma_delay=0.98)
                pk_chdir(D_PROJECT)
                break
            lines = cmd_to_os_like_person_as_admin('dir /b /a-d *.zip')
            print_magenta(rf'''len(lines)={len(lines)}''')
            for line in lines:
                print_magenta(f'''line={line}''')
                if line != "":
                    if os.getcwd() != line:  # 여기 os.getcwd() 이게 들어가네... 나중에 수정하자
                        # 2023-12-04 월 12:14 SyntaxWarning: invalid escape sequence '\d'
                        # r 을 사용 Raw String(원시 문자열),  \를 모두 remove
                        # 정규식은 r 쓰면 안된다. \ 써야한다?.
                        # 2023-12-12 화 14:23 SyntaxWarning: invalid escape sequence '\d'
                        # 가상환경 재설치 후 또 문제가 나타남,
                        # pattern='d{4} d{2} d{2} d{2} d{2} d{2}'
                        # pattern=r'\d{4} \d{2} \d{2} \d{2} \d{2} \d{2}'
                        pattern = r'd{4} d{2} d{2} d{2} d{2} d{2}'
                        # pk_print(line)
                        if is_pattern_in_prompt(line, pattern):
                            pk_print(f"zip f 목록에 대하여 {pattern} 타임스탬프 정규식 테스트를 통과했습니다")
                            # pk_print(line)
                            # 2023-12-03 일 20:03 trouble shooting 성공
                            # 백업 시 타임스탬프에 언더바 넣도록 변경했는데 regex 는 변경 하지 않아서 난 실수 있었음.
                            time_to_backed_up = re.findall(pattern, line)
                            time_to_backed_up_ = time_to_backed_up[0][0:10].replace(" ", "-") + " " + time_to_backed_up[
                                                                                                          0][
                                                                                                      11:16].replace(
                                " ", ":") + ".00"
                            time_to_backed_up__ = datetime.strptime(str(time_to_backed_up_), '%Y-%m-%d %H:%M.%S')
                            time_current = datetime.now()
                            try:
                                target_dirname_old = rf'{target_dirname}\pkg_zip'
                                if not os.path.exists(target_dirname_old):
                                    os.makedirs(target_dirname_old)
                            except Exception:
                                pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''',
                                         print_color='red')
                                pk_chdir(D_PROJECT)
                                break
                            # 지금부터 7일 이전의 f만
                            # diff=time_to_backed_up__ - time_current
                            # if diff.days <-7:
                            # pk_print(f"line : {line}")

                            # pk_print(f"1분(60 seconds) 이전의 f자동정리 시도...")
                            pk_print(f"f자동정리 시도...")
                            change_min = time_current - datetime.timedelta(seconds=60)
                            diff = time_to_backed_up__ - change_min
                            if 60 < diff.seconds:
                                try:
                                    file_with_time_stamp_zip = os.path.abspath(line.strip())
                                    file_dirname_old_abspath = os.path.abspath(target_dirname_old)
                                    pk_print(rf'move "{file_with_time_stamp_zip}" "{file_dirname_old_abspath}"',
                                             print_color='blue')
                                    shutil.move(file_with_time_stamp_zip, file_dirname_old_abspath)
                                except Exception:
                                    pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''',
                                             print_color='red')
                                    pk_chdir(D_PROJECT)
                                    break
            pk_chdir(D_PROJECT)
            pk_print(f" {'%%%FOO%%%' if LTA else ''} green {ment}", print_color='blue')
            break
    except:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        pk_chdir(D_PROJECT)
