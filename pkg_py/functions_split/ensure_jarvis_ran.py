from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_slept import ensure_slept
from pkg_py.functions_split.ensure_spoken import ensure_spoken

def ensure_jarvis_ran():
    from datetime import datetime, time

    # jarvis 모드설정
    ensure_spoken("good evening, sir")

    def parse_time_ranges(text_list):
        """sample: ["12:00-13:00", "15:00-15:10"] -> [(time(12,0), time(13,0)), (time(15,0), time(15,10))]"""
        ranges = []
        for txt in text_list:
            try:
                start_str, end_str = txt.split("-")
                h1, m1 = map(int, start_str.strip().split(":"))
                h2, m2 = map(int, end_str.strip().split(":"))
                ranges.append((time(h1, m1), time(h2, m2)))
            except:
                continue
        return ranges

    def is_now_in_time_range(now_time, time_range):
        start, end = time_range
        return start <= now_time <= end

    def alert(now_time):
        """알림 함수: 현재 시간을 출력하고, OS에 따라 알림 표시"""

        ensure_spoken(f"현재 시간은 {now_time.hour}시 {now_time.minute}분입니다.")
        ensure_printed(f"현재 시간은 {now_time.hour}시 {now_time.minute}분입니다.", print_color='yellow')

    ensure_spoken_v3("샘플 설정 시간을 입력해주세요")
    sleep_time_ranges_text = ["00:12-05:30"]
    lunch_time_ranges_text = ["12:00-13:00"]
    break_time_ranges_text = ["15:00-15:15"]
    exercise_time_ranges_text = ["18:30-18:50"]

    # 파싱
    all_time_blocks = (
            parse_time_ranges(sleep_time_ranges_text)
            + parse_time_ranges(lunch_time_ranges_text)
            + parse_time_ranges(break_time_ranges_text)
            + parse_time_ranges(exercise_time_ranges_text)
    )

    alerted_blocks = set()  # 이미 알림을 한 시간 구간 저장
    last_cleared_hour = -1  # 아직 클리어된 적 없음을 의미

    while True:
        now = datetime.now()
        now_time = now.time()

        # 1시간마다 콘솔 클리어
        if now.hour != last_cleared_hour:
            ensure_console_cleared()
            last_cleared_hour = now.hour
            alerted_blocks.clear()  # 새로운 시간 진입 시, 알림 상태 초기화
            ensure_printed(f"alerted_blocks=({alerted_blocks})", print_color='yellow')

        for idx, block in enumerate(all_time_blocks):
            if is_now_in_time_range(now_time, block):
                if idx not in alerted_blocks:
                    alert(now_time)
                    alerted_blocks.add(idx)
                break  # 현재 속한 구간 하나만 처리

        ensure_slept(milliseconds=10000)
