from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def download_issue_data(data_required, original_log=False):
    import inspect
    import re

    func_n = inspect.currentframe().f_code.co_name

    # 전처리
    issue_file_name = data_required["f 위치"].split('/')[-1]

    def get_origin_log_file_name(issue_file_name):
        # 정규식 패턴 정의: "_숫자(최대 2자리)_VIDEO"
        pattern = r"_\d{1,2}_VIDEO"
        original_filename = re.sub(pattern, "", issue_file_name)
        return original_filename

    origin_log_file_name = get_origin_log_file_name(issue_file_name)
    data_required["주행일자"] = data_required["f 위치"].split('/')[0]
    data_required["f 위치"] = data_required["f 위치"].replace("/", f"\\")

    # 정의
    if original_log == False:
        src = rf"\\192.168.1.33\01_Issue\{data_required["f 위치"]}"
    else:
        src = rf"\\192.168.1.33\02_Orignal\{data_required["차량"]}\{data_required["지역"]}\{data_required["주행일자"]}\{data_required["코스"]}\{origin_log_file_name}"
        ensure_printed(str_working=rf'''src="{src}"  {'%%%FOO%%%' if LTA else ''}''')

    dst = rf"C:\log"
    cmd = rf"copy {src} {dst}"
    src_nx = get_nx(pnx=src)
    src_new = rf"{dst}\{src_nx}"

    while 1:
        if does_pnx_exist(pnx=src_new):
            ensure_printed(str_working=rf'''{src_new} 가 이미 있습니다."  {'%%%FOO%%%' if LTA else ''}''')
            break
        else:
            if not does_pnx_exist(pnx=src_new):
                cmd_to_os(cmd=cmd, mode="a")
                ensure_printed(str_working=rf'''이슈데이터 다운로드 완료 "{src_new}"  {'%%%FOO%%%' if LTA else ''}''',
                         print_color='blue')
                return
