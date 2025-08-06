# editable = True  # pk_option
from pkg_py.functions_split import ensure_console_cleared, ensure_spoken

editable = False  # pk_option


def parse_time_input(time_str):
    import re

    from pkg_py.functions_split.ensure_printed import ensure_printed

    """시간 문자열을 파싱하여 초 단위로 변환"""
    try:
        # 정규식으로 숫자와 단위 추출
        pattern = r'^(\d+)\s*(초|분|시간|시)$'
        match = re.match(pattern, time_str.strip())

        if not match:
            return None, None

        value = int(match.group(1))
        unit = match.group(2)

        # 단위별 초 계산
        if unit == "초":
            seconds = value
            unit_display = "초"
        elif unit == "분":
            seconds = value * 60
            unit_display = "분"
        elif unit in ["시간", "시"]:
            seconds = value * 3600
            unit_display = "시간"
        else:
            return None, None

        return seconds, unit_display

    except Exception as e:
        ensure_printed(f"시간 파싱 오류: {e}", print_color='red')
        return None, None

def get_time_input():
    import inspect

    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
    try:
        func_n = inspect.currentframe().f_code.co_name

        # 알람 내용 입력 (히스토리 + 자동완성 지원)
        key_name = "alarm_content"
        alarm_content = get_values_from_historical_file_routine(
            file_id=get_file_id(key_name, func_n),
            key_hint=f'{key_name}=',
            options_default=[],
            editable=editable
        )

        key_name = "time_input"
        default_time_options = [
            "1초","2초","3초","5초", "10초", "30초", "1분", "5분", "10분", "15분", "30분",
            "1시간", "2시간", "3시간", "5시간", "10시간"
        ]
        time_input = get_values_from_historical_file_routine(
            file_id=get_file_id(key_name, func_n),
            key_hint=f'{key_name}=',
            options_default=default_time_options,
            editable=editable
        )
        if not time_input or not time_input.strip():
            ensure_printed("시간을 입력하지 않았습니다.", print_color='red')
            ensure_spoken("시간을 입력하지 않았습니다.")
            return None, None, None

        # 시간 파싱
        seconds, unit = parse_time_input(time_input)

        if seconds is None:
            ensure_printed("올바른 시간 형식을 입력하세요. (예: 10초, 5분, 1시간)", print_color='red')
            return None, None, None

        if not alarm_content or not alarm_content.strip():
            alarm_content = f"{time_input} 시간경과 알람입니다!"

        return alarm_content, seconds, unit

    except Exception as e:
        ensure_printed(f"입력 중 오류 발생: {e}", print_color='red')
        return None, None, None

def play_alarm_sound():
    """알람 사운드 재생"""
    import winsound
    import time

    from pkg_py.functions_split.ensure_printed import ensure_printed

    for i in range(2):
        ensure_printed(f"[{PkMessages2025.ALARM_BACKGROUND_RUNNING}] {PK_ANSI_COLOR_MAP['RED']}사운드={i + 1}/{len(range(2))} {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)  # 경고음
        time.sleep(0.6)




def alarm_thread(alarm_content, seconds, unit):
    import time
    from datetime import datetime, timedelta

    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_spoken import ensure_spoken
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front

    """알람 스레드 - 지정된 시간 후 알람 울리기"""
    try:
        # 현재 시간과 알람 시간 계산
        now = datetime.now()
        alarm_time = now + timedelta(seconds=seconds)

        ensure_window_title_replaced(alarm_content)

        ensure_console_cleared()
        ensure_printed(f" 알람 설정 완료!", print_color='green')
        ensure_printed(f"현재 시간: {now.strftime('%H:%M:%S')}", print_color='cyan')
        ensure_printed(f"알람 시간: {alarm_time.strftime('%H:%M:%S')}", print_color='cyan')
        ensure_printed(f"대기 시간: {seconds}초", print_color='cyan')
        ensure_printed(f"알람 내용: {alarm_content}", print_color='cyan')

        # 카운트다운 표시
        remaining_seconds = seconds
        while remaining_seconds > 0:
            if remaining_seconds % 60 == 0:  # 1분마다 표시
                minutes_left = remaining_seconds // 60
                ensure_printed(f" 남은 시간: {minutes_left}분", print_color='yellow')
            elif remaining_seconds <= 10:  # 10초 이하일 때는 초 단위로 표시
                ensure_printed(f" 남은 시간: {remaining_seconds}초", print_color='red')

            time.sleep(1)
            remaining_seconds -= 1

        # 알람 시간 도달 - 루프 시작
        while True:
            ensure_console_cleared()
            ensure_window_to_front(window_title_seg=alarm_content)
            play_alarm_sound()
            try:
                ensure_printed(f" 알람 내용 읽는 중...", print_color='red')
                ensure_spoken(alarm_content)
            except Exception as e:
                ensure_printed(f"알람 내용 읽기 오류: {e}", print_color='red')
            
            time.sleep(2)

    except Exception as e:
        ensure_printed(f"알람 스레드 오류: {e}", print_color='red')


def ensure_alert_after_time_profimsed(alarm_content=None, seconds=None, unit=None):
    import threading

    from pkg_py.functions_split.ensure_printed import ensure_printed

    """약속된 시간 후 알람 울리기 (자동완성 + 히스토리 지원)
    
    Args:
        alarm_content (str, optional): 알람 내용. None이면 사용자 입력 받음
        seconds (int, optional): 대기 시간(초). None이면 사용자 입력 받음
        unit (str, optional): 시간 단위. None이면 사용자 입력 받음
    """
    # 인자가 제공되지 않은 경우 사용자 입력 받기
    if alarm_content is None or seconds is None or unit is None:
        input_alarm_content, input_seconds, input_unit = get_time_input()

        if input_alarm_content is None:
            ensure_printed("알람 설정을 취소합니다.", print_color='red')
            return

        # 인자가 None인 경우에만 사용자 입력값 사용
        alarm_content = alarm_content or input_alarm_content
        seconds = seconds or input_seconds
        unit = unit or input_unit

    # 알람 스레드 시작
    thread = threading.Thread(
        target=alarm_thread,
        args=(alarm_content, seconds, unit),
        daemon=False  # 데몬=False로 변경하여 메인 프로그램 종료와 독립적으로 실행
    )
    thread.start()

            ensure_printed(f"[{PkMessages2025.ALARM_BACKGROUND_RUNNING}] {PK_ANSI_COLOR_MAP['GREEN']}상태=백그라운드실행 {PK_ANSI_COLOR_MAP['RESET']}", print_color='green')
    ensure_printed(" 프로그램을 종료해도 알람은 계속 작동합니다.", print_color='cyan')
    ensure_printed(" 입력값이 히스토리에 저장되어 다음에 자동완성됩니다.", print_color='cyan')

    # 알람 스레드가 완료될 때까지 대기 (선택사항)
    # thread.join()
