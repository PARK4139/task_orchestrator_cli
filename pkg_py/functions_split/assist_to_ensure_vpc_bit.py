from pkg_py.pk_system_object.Local_test_activate import LTA

from pkg_py.functions_split.pk_print import pk_print


def assist_to_ensure_vpc_bit(bit_mode):
    # 개요 : vpc 트래킹 시스템, 이슈발생 vpc 이슈트래킹시스템 필요.
    # BIT # Built in Test
    # P BIT # non-continuous : pilot or maintenance
    # C BIT # continuous     : os
    # 프로그램 대기능 정의 : vpc 테스트/이슈레포팅/해결 자동시스템
    # 프로그램명 : oo.py
    # 프로그램 설치위치 : vpc/도커/oo.py or IT/도커/oo.py
    # 개발순서 : P BIT > C BIT

    if not LTA:
        if not is_internet_connected():
            pk_print(f'''인터넷이 연결되어야 vpc bit 가 진행이 가능합니다. {'%%%FOO%%%' if LTA else ''}''', print_color='red')

    # ensure ping to acu_it # [acu_it] from toml

    # ensure ping to vpc side a # [vpc side a] from toml

    # ensure ping to vpc side b # [vpc side b] from toml

    state_c_bit_activated = 1
    if bit_mode == "p":
        state_c_bit_activated = 0
    if bit_mode == "c":
        state_c_bit_activated = 1
    while 1:
        pk_print(f'''bit_mode={bit_mode} {'%%%FOO%%%' if LTA else ''}''')
        if ensure_vpc_issue_clear():
            pass
        if state_c_bit_activated == 0:
            break
        pk_sleep(milliseconds=1000)
