from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.pk_print import pk_print


def set_wake_up_via_schtasks(seconds):
    from datetime import datetime, timedelta

    # 현재 시간을 기준으로 깨울 시간을 계산
    current_time_str = datetime.now().strftime("%H:%M:%S")
    wake_time = datetime.now() + timedelta(seconds=seconds)
    wake_time_str = wake_time.strftime("%H:%M:%S")
    pk_print(
        f"현재 시간: {current_time_str}, {wake_time_str} 후에 컴퓨터를 깨웁니다 {'%%%FOO%%%' if LTA else ''}",
        print_color="blue"
    )

    # 작업 예약 명령어 생성
    task_name = "WakeComputer"
    cmd = f'schtasks /create /tn "{task_name}" /tr "cmd.exe /c exit" /sc once /st {wake_time.strftime("%H:%M")} /f /it'
    pk_print(f''' {cmd}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    std_list = cmd_to_os(cmd=cmd)
    std_list = get_list_converted_from_byte_list_to_str_list(std_list)
    for std_str in std_list:
        pk_print(f'''[STD_OUT] {std_str}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    pk_print(f'''태스크 스케줄러에 깨우기 작업이 설정되었습니다.  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
