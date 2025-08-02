import datetime
from datetime import datetime, time
from enum import Enum
from sys import prefix
from typing import Optional, Callable

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.functions_split.ensure_pk_wsl_distro_enabled import ensure_pk_wsl_distro_enabled
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_py_system_process_ran_by_pnx import ensure_py_system_process_ran_by_pnx
from pkg_py.functions_split.ensure_spoken import ensure_spoken
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_sorted_pk_file_list import get_excutable_pk_system_processes
from pkg_py.system_object.etc import pk_
from pkg_py.system_object.files import F_PK_SQLITE
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.functions_split.is_mic_device_connected import is_mic_device_connected


class JarvisMode(Enum):
    """Jarvis 동작 모드 정의"""
    CLI_COMMAND = "cli_command"      # CLI 명령어 모드
    VOICE_COMMAND = "voice_command"  # 음성 명령어 모드
    HYBRID = "hybrid"                # 하이브리드 모드 (CLI + 음성)
    SILENT = "silent"                # 무음 모드 (음성 출력 없음)
    DEBUG = "debug"                  # 디버그 모드


def check_microphone_available():
    """마이크 사용 가능 여부 확인 - 기존 함수 활용"""
    try:
        # 기존 마이크 감지 함수 사용
        mic_connected = is_mic_device_connected()
        
        if mic_connected:
            ensure_printed("🎤 마이크가 감지되었습니다.", print_color='green')
            return True
        else:
            ensure_printed("🎤 마이크가 감지되지 않습니다.", print_color='yellow')
            return False
            
    except Exception as e:
        ensure_printed(f" 마이크 확인 중 오류: {e}", print_color='yellow')
        return False


class JarvisState:
    """Jarvis 상태 관리 클래스"""
    def __init__(self):
        # 마이크 사용 가능 여부에 따라 초기 모드 결정
        if check_microphone_available():
            self.current_mode = JarvisMode.VOICE_COMMAND
            ensure_printed("🎤 마이크가 감지되어 음성 모드로 시작합니다.", print_color='green')
        else:
            self.current_mode = JarvisMode.CLI_COMMAND
            ensure_printed("⌨️ CLI 모드로 시작합니다.", print_color='cyan')
            
        self.is_running = False
        self.last_command_time = None
        self.command_history = []
        self.alerted_blocks = set()
        self.last_cleared_hour = -1
        # 새로운 필드들 추가
        self.command_cache = {}  # 명령어 실행 결과 캐시
        self.process_cache = {}  # 프로세스 목록 캐시
        self.cache_timestamp = None
        self.cache_duration = 300  # 5분 캐시
        self.microphone_available = check_microphone_available()  # 마이크 상태 저장
        
    def switch_mode(self, new_mode: JarvisMode):
        """모드 전환 - 마이크 상태 확인"""
        old_mode = self.current_mode
        
        # 음성 모드로 전환하려면 마이크가 필요
        if new_mode in [JarvisMode.VOICE_COMMAND, JarvisMode.HYBRID]:
            if not self.microphone_available:
                ensure_printed(" 마이크가 연결되지 않아 음성 모드로 전환할 수 없습니다.", print_color='red')
                return old_mode
        
        self.current_mode = new_mode
        ensure_printed(f" Jarvis 모드 변경: {old_mode.value} → {new_mode.value}", print_color='cyan')
        return old_mode
    
    def add_command_to_history(self, command: str):
        """명령어 히스토리에 추가"""
        self.command_history.append({
            'command': command,
            'timestamp': datetime.now(),
            'mode': self.current_mode.value
        })
        # 최근 100개만 유지
        if len(self.command_history) > 100:
            self.command_history.pop(0)

    def get_cached_processes(self):
        """캐시된 프로세스 목록 반환"""
        now = datetime.now()
        if (self.cache_timestamp is None or 
            (now - self.cache_timestamp).seconds > self.cache_duration):
            try:
                self.process_cache = get_excutable_pk_system_processes()
                self.cache_timestamp = now
            except Exception as e:
                ensure_printed(f"⚠️ 프로세스 목록 캐시 오류: {e}", print_color='yellow')
        return self.process_cache

    def check_microphone_status(self):
        """마이크 상태 재확인 - 기존 함수 활용"""
        self.microphone_available = bool(is_mic_device_connected())
        return self.microphone_available


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


def get_user_command_via_mode(mode: JarvisMode) -> str:
    try:
        if mode == JarvisMode.VOICE_COMMAND:
            return get_voice_command()
        elif mode == JarvisMode.HYBRID:
            # 하이브리드 모드에서는 음성 우선, 실패시 CLI
            try:
                return get_voice_command()
            except:
                return get_cli_command()
        else:  # CLI_COMMAND, SILENT, DEBUG
            return get_cli_command()
    except KeyboardInterrupt:
        return "quit"
    except EOFError:
        return "quit"


def get_cli_command() -> str:
    """CLI 명령어 입력 받기 - 개선된 자동완성"""
    try:
        # 캐시된 프로세스 목록 사용
        pk_processes = state.get_cached_processes() if 'state' in locals() else get_excutable_pk_system_processes()
        
        # 파일명만 추출 (경로 제거)
        import os
        process_names = [os.path.basename(f).replace('.py', '') for f in pk_processes]
        
        # 카테고리별 명령어 그룹화
        command_categories = {
            "기본 명령어": [
                "hello", "안녕", "안녕하세요",
                "time", "시간", "몇시",
                "date", "날짜", "오늘",
                "help", "도움말", "명령어",
                "clear", "클리어", "정리",
                "quit", "exit", "종료", "나가기",
            ],
            "모드 전환": [
                "mode cli", "cli mode", "텍스트 모드",
                "mode voice", "voice mode", "음성 모드",
                "mode hybrid", "hybrid mode", "하이브리드 모드",
                "mode silent", "silent mode", "무음 모드",
                "mode debug", "debug mode", "디버그 모드",
            ],
            "시스템 명령어": [
                "wsl 활성화",
                "history", "히스토리",
                "status", "상태"
            ],
            "PK 프로세스": process_names
        }
        
        # 모든 옵션 합치기
        all_options = []
        for category, commands in command_categories.items():
            all_options.extend(commands)
        
        # get_value_completed 사용하여 자동완성 기능 제공
        command = get_value_completed("command=", all_options)
        
        if command is None:
            return "quit"  # 사용자가 취소한 경우
        
        return command.strip()
        
    except Exception as e:
        # 오류 발생 시 기본 input 사용
        ensure_printed(f"⚠️ 자동완성 오류: {e}", print_color='yellow')
        return input("command=").strip()


def get_voice_command() -> str:
    """음성 명령어 입력 받기 - 개선된 버전"""
    import speech_recognition as sr
    
    recognizer = sr.Recognizer()
    ensure_printed(" 음성을 인식하고 있습니다...", print_color='blue')
    
    try:
        with sr.Microphone() as source:
            # 노이즈 제거 개선
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            recognizer.energy_threshold = 4000  # 음성 감지 임계값 조정
            recognizer.dynamic_energy_threshold = True
            
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        
        # 여러 음성 인식 서비스 시도
        command = None
        services = [
            ('google', lambda: recognizer.recognize_google(audio, language="ko")),
            ('google', lambda: recognizer.recognize_google(audio, language="ko-KR")),
        ]
        
        for service_name, service_func in services:
            try:
                command = service_func()
                ensure_printed(f"🎤 {service_name} 인식: {command}", print_color='green')
                break
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                continue
        
        if command:
            return command.strip()
        else:
            ensure_printed("🎤 음성을 인식하지 못했습니다. CLI 모드로 전환합니다.", print_color='yellow')
            return get_cli_command()
            
    except Exception as e:
        ensure_printed(f"🎤 음성 인식 중 오류: {e}", print_color='red')
        return get_cli_command()


def process_command(command: str, state: JarvisState) -> bool:
    """명령어 처리 - 개선된 에러 처리"""
    command = command.lower()
    
    try:
        # 마이크 상태 확인 명령어
        if command in ["check mic", "마이크 확인"]:
            if state.check_microphone_status():
                ensure_printed("🎤 마이크가 정상적으로 연결되어 있습니다.", print_color='green')
                if state.current_mode == JarvisMode.CLI_COMMAND:
                    ensure_printed("💡 'mode voice' 명령어로 음성 모드로 전환할 수 있습니다.", print_color='cyan')
            else:
                ensure_printed(" 마이크가 연결되지 않았습니다.", print_color='red')
            return True
        
        # 모드 전환 명령어들
        if command in ["mode cli", "cli mode", "텍스트 모드"]:
            state.switch_mode(JarvisMode.CLI_COMMAND)
            return True
        elif command in ["mode voice", "voice mode", "음성 모드"]:
            if state.microphone_available:
                state.switch_mode(JarvisMode.VOICE_COMMAND)
            else:
                ensure_printed(" 마이크가 연결되지 않아 음성 모드로 전환할 수 없습니다.", print_color='red')
            return True
        elif command in ["mode hybrid", "hybrid mode", "하이브리드 모드"]:
            if state.microphone_available:
                state.switch_mode(JarvisMode.HYBRID)
            else:
                ensure_printed(" 마이크가 연결되지 않아 하이브리드 모드로 전환할 수 없습니다.", print_color='red')
            return True
        elif command in ["mode silent", "silent mode", "무음 모드"]:
            state.switch_mode(JarvisMode.SILENT)
            return True
        elif command in ["mode debug", "debug mode", "디버그 모드"]:
            state.switch_mode(JarvisMode.DEBUG)
            return True
        
        # 기본 명령어들
        if command in ["quit", "exit", "종료", "나가기"]:
            response = f"{PkMessages2025.QUIT_MESSAGE}"
            if state.current_mode != JarvisMode.SILENT:
                ensure_spoken(response)
            ensure_printed(f" {PkMessages2025.QUITTING}...", print_color='yellow')
            return False
        elif command in ["hello", "안녕", "안녕하세요"]:
            response = f"{PkMessages2025.HELLO_RESPONSE} {PkMessages2025.HELLO_GREETING}"
            if state.current_mode != JarvisMode.SILENT:
                ensure_spoken(response)
            ensure_printed(f" {PkMessages2025.HELLO_RESPONSE}", print_color='green')
        elif command in ["time", "시간", "몇시"]:
            now = datetime.now()
            time_str = f"{PkMessages2025.TIME_RESPONSE} {now.hour}시 {now.minute}분입니다."
            if state.current_mode != JarvisMode.SILENT:
                ensure_spoken(time_str)
            ensure_printed(f"⏰ {time_str}", print_color='blue')
        elif command in ["date", "날짜", "오늘"]:
            now = datetime.now()
            date_str = f"{PkMessages2025.DATE_RESPONSE} {now.year}년 {now.month}월 {now.day}일입니다."
            if state.current_mode != JarvisMode.SILENT:
                ensure_spoken(date_str)
            ensure_printed(f" {date_str}", print_color='blue')
        elif command in ["help", "도움말", "명령어"]:
            ensure_help_menu_shown(state)
        elif command in ["clear", "클리어", "정리"]:
            ensure_console_cleared()
            response = f"🧹 {PkMessages2025.CLEAR_RESPONSE}."
            if state.current_mode != JarvisMode.SILENT:
                ensure_spoken(response)
            ensure_printed(response, print_color='green')
        elif command in ["wsl 활성화"]:
            if not ensure_pk_wsl_distro_enabled():
                raise RuntimeError("WSL 배포판 설치/이름 변경에 실패했습니다.")
        elif command in ["history", "히스토리"]:
            show_command_history(state)
        elif command in ["status", "상태"]:
            show_current_status(state)
        elif command == "":
            if state.current_mode != JarvisMode.SILENT:
                ensure_printed(f" {PkMessages2025.WHAT_CAN_I_HELP}? (help 입력시 명령어 확인)", print_color='yellow')
        else:
            # pk_system 프로세스 실행 시도
            if try_execute_pk_process(command, state):
                return True
            
            # 매칭되지 않은 경우
            response = f"'{command}' {PkMessages2025.UNKNOWN_COMMAND}. 'help'를 입력하여 사용 가능한 명령어를 확인하세요."
            if state.current_mode != JarvisMode.SILENT:
                ensure_spoken(response)
            ensure_printed(f"❓ {response}", print_color='red')

        return True
        
    except Exception as e:
        error_msg = f"❌ 명령어 처리 중 오류: {e}"
        ensure_printed(error_msg, print_color='red')
        if state.current_mode != JarvisMode.SILENT:
            ensure_spoken(f"{PkMessages2025.ERROR_OCCURRED}")
        return True

def ensure_help_menu_shown(state: JarvisState):
    """개선된 도움말 메뉴"""
    if state.current_mode != JarvisMode.SILENT:
        ensure_spoken(f"{PkMessages2025.HELP_RESPONSE}")
    
    help_text = f"""
 {PkMessages2025.HELP_COMMANDS}

 기본 명령어:
  • hello/안녕: 인사
  • time/시간: 현재 시간
  • date/날짜: 현재 날짜
  • clear/클리어: 화면 정리
  • quit/종료: Jarvis 종료
  • help/도움말: 이 도움말 표시

 모드 전환:
  • mode cli/텍스트 모드: CLI 명령어 모드
  • mode voice/음성 모드: 음성 명령어 모드
  • mode hybrid/하이브리드 모드: CLI + 음성 모드
  • mode silent/무음 모드: 음성 출력 없음
  • mode debug/디버그 모드: 디버그 정보 표시

⚙️ 시스템 명령어:
  • wsl 활성화: WSL 배포판 활성화
  • history: 명령어 히스토리 표시
  • status: 현재 상태 표시

🚀 PK 시스템 프로세스:
  • Tab 키로 자동완성 가능한 모든 pk_* 프로세스 실행 가능
  • 예: pk_ensure_hello_world_printed, pk_ensure_chrome_opened 등

💡 팁: Tab 키를 눌러 명령어를 자동완성하고 선택하세요!
    """
    ensure_printed(help_text, print_color='cyan')


def try_execute_pk_process(command: str, state: JarvisState) -> bool:
    """pk_system 프로세스 실행 시도"""
    try:
        # 실행 가능한 프로세스 목록 가져오기
        pk_processes = get_excutable_pk_system_processes()
        
        # 파일명만 추출하여 매칭
        import os
        for file_to_excute in pk_processes:
            file_name = os.path.basename(file_to_excute).replace('.py', '')
            if command.lower() == file_name.lower():
                try:
                    prefix= pk_
                    file_to_excute = file_to_excute
                    file_title = os.path.basename(file_to_excute)
                    file_title = file_title.removeprefix(prefix)
                    ensure_py_system_process_ran_by_pnx(file_to_excute, file_title)
                    ensure_printed(f"✅ {file_name} 완료", print_color='green')
                    return True
                except Exception as e:
                    ensure_printed(f"❌ {file_name} 실행 중 오류: {e}", print_color='red')
                    return True
        
        return False
        
    except Exception as e:
        ensure_printed(f"⚠️ 프로세스 실행 시도 중 오류: {e}", print_color='yellow')
        return False


def show_command_history(state: JarvisState):
    """명령어 히스토리 표시"""
    ensure_printed("📜 명령어 히스토리:", print_color='cyan')
    for i, entry in enumerate(state.command_history[-10:], 1):  # 최근 10개
        timestamp = entry['timestamp'].strftime("%H:%M:%S")
        ensure_printed(f"  {i}. [{timestamp}] {entry['command']} ({entry['mode']})", print_color='white')


def show_current_status(state: JarvisState):
    """현재 상태 표시"""
    ensure_printed("📊 Jarvis 현재 상태:", print_color='cyan')
    ensure_printed(f"  모드: {state.current_mode.value}", print_color='white')
    ensure_printed(f"  마이크: {'연결됨' if state.microphone_available else '연결되지 않음'}", print_color='white')
    ensure_printed(f"  실행 중: {'예' if state.is_running else '아니오'}", print_color='white')
    ensure_printed(f"  명령어 수: {len(state.command_history)}", print_color='white')
    
    # 사용 가능한 프로세스 수 표시
    try:
        pk_processes = get_excutable_pk_system_processes()
        ensure_printed(f"  사용 가능한 프로세스: {len(pk_processes)}개", print_color='white')
    except:
        ensure_printed(f"  사용 가능한 프로세스: 확인 불가", print_color='white')
    
    if state.last_command_time:
        ensure_printed(f"  마지막 명력어: {state.last_command_time.strftime('%H:%M:%S')}", print_color='white')


def alert(now_time, state: JarvisState):
    """알림 함수: 모드에 따른 알림 방식 적용"""
    message = f"{PkMessages2025.ALERT_TIME} {now_time.hour}시 {now_time.minute}분입니다."
    if state.current_mode != JarvisMode.SILENT:
        ensure_spoken(message)
    ensure_printed(message, print_color='yellow')


def ensure_greeting_daily(state: JarvisState):
    """
    일일 인사 - 시간대에 따라 아침/점심/저녁 인사
    하루에 각 인사는 1번씩만, pk.sqlite에 상태 저장/불러오기
    """
    import sqlite3
    from datetime import datetime, date

    now = datetime.now()
    hour = now.hour
    today_str = date.today().isoformat()
    if 5 <= hour < 12:
        greeting_type = "morning"
        greeting = f"{PkMessages2025.GOOD_MORNING}"
    elif 12 <= hour < 18:
        greeting_type = "afternoon"
        greeting = f"{PkMessages2025.GOOD_AFTERNOON}"
    else:
        greeting_type = "evening"
        greeting = f"{PkMessages2025.GOOD_EVENING}"

    db_path = F_PK_SQLITE
    greeted = False
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS greeting_log (
                date TEXT,
                type TEXT,
                PRIMARY KEY (date, type)
            )
        """)
        cur.execute(
            "SELECT 1 FROM greeting_log WHERE date=? AND type=?",
            (today_str, greeting_type)
        )
        greeted = cur.fetchone() is not None
        if not greeted:
            cur.execute(
                "INSERT INTO greeting_log (date, type) VALUES (?, ?)",
                (today_str, greeting_type)
            )
            conn.commit()
        conn.close()
    except Exception as e:
        ensure_printed(f"⚠️ 인사 기록 DB 오류: {e}", print_color='yellow')
        # DB 오류 시에도 인사 1회만 수행(중복 가능성 감수)

    if not greeted:
        if state.current_mode != JarvisMode.SILENT:
            ensure_spoken(greeting)


def ensure_jarvis_ran():
    state = JarvisState()
    state.is_running = True
    
    # 시간 블록 설정
    # ensure_spoken(f"{PkMessages2025.SAMPLE_TIME_INPUT}")
    sleep_time_ranges_text = ["00:12-05:30"]
    lunch_time_ranges_text = ["12:00-13:00"]
    break_time_ranges_text = ["15:00-15:15"]
    exercise_time_ranges_text = ["18:30-18:50"]
    all_time_blocks = (
        parse_time_ranges(sleep_time_ranges_text)
        + parse_time_ranges(lunch_time_ranges_text)
        + parse_time_ranges(break_time_ranges_text)
        + parse_time_ranges(exercise_time_ranges_text)
    )

    # 대화형 루프
    while state.is_running:
        try:
            ensure_greeting_daily(state)
            
            # 사용자 입력 받기
            user_input = get_user_command_via_mode(state.current_mode)
            
            if user_input:
                # 명령어 히스토리에 추가
                state.add_command_to_history(user_input) 
                state.last_command_time = datetime.now()
            
            # 명령어 처리
            if not process_command(user_input, state):
                break
                
            ensure_printed("-" * 50, print_color='white')
            
        except KeyboardInterrupt:
            ensure_printed("\n⚠️ 사용자가 중단했습니다.", print_color='yellow')
            break
        except Exception as e:
            error_msg = f"❌ {PkMessages2025.ERROR_OCCURRED}: {e}"
            ensure_printed(error_msg, print_color='red')
            if state.current_mode != JarvisMode.SILENT:
                ensure_spoken(f"{PkMessages2025.ERROR_OCCURRED}")

        # 시간 기반 알림 처리
        now = datetime.now()
        now_time = now.time()

        # 1시간마다 콘솔 클리어
        if now.hour != state.last_cleared_hour:
            ensure_console_cleared()
            state.last_cleared_hour = now.hour
            state.alerted_blocks.clear()  # 새로운 시간 진입 시, 알림 상태 초기화
            if state.current_mode == JarvisMode.DEBUG:
                ensure_printed(f"{PkMessages2025.ALERT_BLOCKS}=({state.alerted_blocks})", print_color='yellow')

        # 현재 속한 구간 하나만 처리
        for idx, block in enumerate(all_time_blocks):
            if is_now_in_time_range(now_time, block):
                if idx not in state.alerted_blocks:
                    alert(now_time, state)
                    state.alerted_blocks.add(idx)
                    break
    
    # 종료 처리
    state.is_running = False
    ensure_printed("👋 Jarvis를 종료합니다.", print_color='green')
