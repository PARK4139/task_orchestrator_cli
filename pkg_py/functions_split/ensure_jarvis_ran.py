

def ensure_jarvis_ran():
    """
    대화형 Jarvis 루프
    기존 내용은 주석처리하고 대화형 루프로 변경
    """
    from datetime import datetime, time
    from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.functions_split.ensure_spoken import ensure_spoken
    from pkg_py.functions_split.ensure_spoken_v3 import ensure_spoken_v3

    # ===== 기존 내용 주석처리 =====
    # jarvis 모드설정
    # ensure_spoken("good evening, sir")
    # return

    # if not ensure_pk_wsl_distro_enabled():
    #     raise RuntimeError("WSL 배포판 설치/이름 변경에 실패했습니다.")

    # if is_os_linux():
    #     # ensure_command_excuted_to_os('exit')
    #     # available_pk_system_process_pnx = get_pnx_from_fzf(D_PKG_PY)
    #     available_pk_system_process_pnx = None
    #     pnx_list = get_pnxs(d_working=D_PKG_PY, mode="f", with_walking=0)
    #     for pnx in pnx_list:
    #         if __file__ not in pnx:
    #             continue
    #         available_pk_system_process_pnx = pnx
    #     tmux_session = get_nx(available_pk_system_process_pnx).replace(".", "_")
    #     ensure_tmux_pk_session_removed(tmux_session)

    # def parse_time_ranges(text_list):
    #     """sample: ["12:00-13:00", "15:00-15:10"] -> [(time(12,0), time(13,0)), (time(15,0), time(15,10))]"""
    #     ranges = []
    #     for txt in text_list:
    #         try:
    #                 start_str, end_str = txt.split("-")
    #                 h1, m1 = map(int, start_str.strip().split(":"))
    #                 h2, m2 = map(int, end_str.strip().split(":"))
    #                 ranges.append((time(h1, m1), time(h2, m2)))
    #             except:
    #                 continue
    #         return ranges

    # def is_now_in_time_range(now_time, time_range):
    #     start, end = time_range
    #     return start <= now_time <= end

    # def alert(now_time):
    #     """알림 함수: 현재 시간을 출력하고, OS에 따라 알림 표시"""
    #     ensure_spoken(f"현재 시간은 {now_time.hour}시 {now_time.minute}분입니다.")
    #     ensure_printed(f"현재 시간은 {now_time.hour}시 {now_time.minute}분입니다.", print_color='yellow')

    # ensure_spoken_v3("샘플 설정 시간을 입력해주세요")
    # sleep_time_ranges_text = ["00:12-05:30"]
    # lunch_time_ranges_text = ["12:00-13:00"]
    # break_time_ranges_text = ["15:00-15:15"]
    # exercise_time_ranges_text = ["18:30-18:50"]

    # # 파싱
    # all_time_blocks = (
    #         parse_time_ranges(sleep_time_ranges_text)
    #         + parse_time_ranges(lunch_time_ranges_text)
    #         + parse_time_ranges(break_time_ranges_text)
    #         + parse_time_ranges(exercise_time_ranges_text)
    # )

    # alerted_blocks = set()  # 이미 알림을 한 시간 구간 저장
    # last_cleared_hour = -1  # 아직 클리어된 적 없음을 의미

    # while True:
    #     now = datetime.now()
    #     now_time = now.time()

    #     # 1시간마다 콘솔 클리어
    #     if now.hour != last_cleared_hour:
    #         ensure_console_cleared()
    #         last_cleared_hour = now.hour
    #         alerted_blocks.clear()  # 새로운 시간 진입 시, 알림 상태 초기화
    #         ensure_printed(f"alerted_blocks=({alerted_blocks})", print_color='yellow')

    #     for idx, block in enumerate(all_time_blocks):
    #         if is_now_in_time_range(now_time, block):
    #             if idx not in alerted_blocks:
    #                 alert(now_time)
    #                     alerted_blocks.add(idx)
    #                 break  # 현재 속한 구간 하나만 처리

    #     ensure_slept(milliseconds=10000)
    # ===== 기존 내용 주석처리 완료 =====

    # ===== 새로운 대화형 루프 =====
    def get_user_input():
        """사용자 입력 받기"""
        try:
            return input("🎤 Jarvis: ").strip()
        except KeyboardInterrupt:
            return "quit"
        except EOFError:
            return "quit"

    def process_command(command):
        """명령어 처리"""
        command = command.lower()
        
        if command in ["quit", "exit", "종료", "나가기"]:
            ensure_spoken("Jarvis를 종료합니다. 안녕히 가세요.")
            ensure_printed("🔄 Jarvis 종료 중...", print_color='yellow')
            return False
        
        elif command in ["hello", "안녕", "안녕하세요"]:
            ensure_spoken("안녕하세요! 무엇을 도와드릴까요?")
            ensure_printed("👋 안녕하세요!", print_color='green')
        
        elif command in ["time", "시간", "몇시"]:
            now = datetime.now()
            time_str = f"현재 시간은 {now.hour}시 {now.minute}분입니다."
            ensure_spoken(time_str)
            ensure_printed(f"⏰ {time_str}", print_color='blue')
        
        elif command in ["date", "날짜", "오늘"]:
            now = datetime.now()
            date_str = f"오늘은 {now.year}년 {now.month}월 {now.day}일입니다."
            ensure_spoken(date_str)
            ensure_printed(f"📅 {date_str}", print_color='blue')
        
        elif command in ["help", "도움말", "명령어"]:
            help_text = """
🎤 Jarvis 명령어:
- hello/안녕: 인사
- time/시간: 현재 시간
- date/날짜: 현재 날짜
- clear/클리어: 화면 정리
- quit/종료: Jarvis 종료
- help/도움말: 이 도움말 표시
            """
            ensure_printed(help_text, print_color='cyan')
        
        elif command in ["clear", "클리어", "정리"]:
            ensure_console_cleared()
            ensure_printed("🧹 화면을 정리했습니다.", print_color='green')
        
        elif command == "":
            ensure_printed("🤔 무엇을 도와드릴까요? (help 입력시 명령어 확인)", print_color='yellow')
        
        else:
            response = f"'{command}' 명령어를 이해하지 못했습니다. 'help'를 입력하여 사용 가능한 명령어를 확인하세요."
            ensure_spoken(response)
            ensure_printed(f"❓ {response}", print_color='red')
        
        return True

    # Jarvis 시작
    ensure_console_cleared()
    ensure_spoken("안녕하세요! Jarvis가 시작되었습니다.")
    ensure_printed("🤖 Jarvis 대화형 루프 시작!", print_color='green')
    ensure_printed("💡 'help'를 입력하여 사용 가능한 명령어를 확인하세요.", print_color='cyan')
    ensure_printed("=" * 50, print_color='white')

    # 대화형 루프
    while True:
        try:
            user_input = get_user_input()
            if not process_command(user_input):
                break
            ensure_printed("-" * 30, print_color='white')
        except Exception as e:
            ensure_printed(f"❌ 오류 발생: {e}", print_color='red')
            ensure_spoken("오류가 발생했습니다.")
