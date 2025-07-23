from pkg_py.pk_system_object.is_os_windows import is_os_windows

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.pk_print import pk_print


def ping_v1(ip):
    # pk : windows 10 pro 에서 정상동작 확인
    # pk : 다만 평균속도가 1초로 느린편

    if not ip:
        pk_print(f'''ping {ip} ''', print_color='red')
        return 0
    signiture = None
    if is_os_windows():
        cmd = rf"ping -n 1 -w 500 {ip}"  # 3600000ms 타임아웃
        signiture_list = ["(0% loss)", '(0% 손실)']
    else:
        cmd = rf"ping -c 1 -W 0.5 {ip}"  # 3600초 타임아웃
        signiture_list = [f'{PK_BLANK}0% packet loss']
    std_list = cmd_to_os(cmd=cmd, encoding=Encoding.UTF8)
    for line in std_list:
        if any(signiture in line for signiture in signiture_list):
            if LTA:
                pk_print(f'''ping {ip} ''', print_color='green')
            return 1
    pk_print(f'''ping {ip} ''', print_color='red')
    return 0
