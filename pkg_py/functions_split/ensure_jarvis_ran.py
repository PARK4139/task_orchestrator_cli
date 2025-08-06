import datetime
from datetime import datetime, time
from enum import Enum
from sys import prefix
from typing import Optional, Callable, List, Tuple, Dict
import re
import os

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.functions_split.ensure_pk_wsl_distro_enabled import ensure_pk_wsl_distro_enabled
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_py_system_process_ran_by_pnx import ensure_py_system_process_ran_by_pnx
from pkg_py.functions_split.ensure_spoken import ensure_spoken
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_sorted_pk_file_list import get_excutable_pk_system_processes
from pkg_py.system_object.etc import pk_
from pkg_py.system_object.files import F_PK_SYSTEM_SQLITE
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.functions_split.is_mic_device_connected import is_mic_device_connected


class JarvisMode(Enum):
    """Jarvis 동작 모드 정의"""
    KEYBOARD_CONVERSATION = "keyboard_conversation"  # 키보드 대화 모드
    VOICE_CONVERSATION = "voice_conversation"        # 음성 대화 모드
    HYBRID = "hybrid"                                # 하이브리드 모드 (키보드 + 음성)
    SILENT = "silent"                                # 무음 모드 (음성 출력 없음)
    DEBUG = "debug"                                  # 디버그 모드


def check_microphone_available():
    """마이크 사용 가능 여부 확인 - 기존 함수 활용"""
    try:
        # 기존 마이크 감지 함수 사용
        mic_connected = is_mic_device_connected()
        
        if mic_connected:
            ensure_printed(" 마이크가 감지되었습니다.", print_color='green')
            return True
        else:
            ensure_printed(" 마이크가 감지되지 않습니다.", print_color='yellow')
            return False
            
    except Exception as e:
        ensure_printed(f" 마이크 확인 중 오류: {e}", print_color='yellow')
        return False


class DynamicCommandMapper:
    """동적 명령어-함수 매핑 클래스"""
    
    def __init__(self):
        self.mapping = {}
        self.cache_timestamp = None
        self.cache_duration = 300  # 5분 캐시
        self._refresh_mappings()

    def _refresh_mappings(self):
        """pkg_py 하위의 모든 파일에서 함수명을 추출해 동적 매핑 생성"""
        self.mapping = {}
        base_dir = os.path.join(os.path.dirname(__file__), '..')
        pkg_py_dir = os.path.abspath(os.path.join(base_dir, '..', 'pkg_py'))
        
        for root, dirs, files in os.walk(pkg_py_dir):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, encoding='utf-8') as f:
                            content = f.read()
                        # 함수명 추출 (def 함수명)
                        for match in re.finditer(r'def\s+([a-zA-Z0-9_]+)\s*\(', content):
                            func_name = match.group(1)
                            # 형태소 분석 대신 언더스코어/영어 단어 분리
                            tokens = re.split(r'[_]', func_name)
                            for token in tokens:
                                if len(token) > 1:  # 한 글자 토큰은 제외
                                    self.mapping.setdefault(token.lower(), set()).add(func_name)
                            # 전체 함수명도 매핑
                            self.mapping.setdefault(func_name.lower(), set()).add(func_name)
                    except Exception as e:
                        pass  # 파일 읽기 실패는 무시

        # set → list 변환
        for k in self.mapping:
            self.mapping[k] = list(self.mapping[k])

    def find_matching_functions(self, command: str):
        """명령어에 매칭되는 함수명(들) 반환"""
        self._refresh_mappings()
        command_lower = command.lower().strip()
        matches = set()
        # 완전 일치
        if command_lower in self.mapping:
            matches.update(self.mapping[command_lower])
        # 부분 일치 (토큰)
        for key in self.mapping:
            if key in command_lower or command_lower in key:
                matches.update(self.mapping[key])
        return list(matches)

    def print_current_mapping(self, command: str):
        matches = self.find_matching_functions(command)
        ensure_printed(f"[동적 함수 매핑] '{command}' → {matches if matches else '매칭 없음'}", print_color='yellow')


class ProcessMatcher:
    """PK 프로세스와 자연어 명령어 매칭 클래스"""
    
    def __init__(self):
        self.process_cache = {}
        self.cache_timestamp = None
        self.cache_duration = 300  # 5분 캐시
        self.dynamic_mapper = DynamicCommandMapper()
        
    def get_process_names(self) -> List[str]:
        """PK 프로세스 목록 가져오기 (캐시 적용)"""
        now = datetime.now()
        if (self.cache_timestamp is None or 
            (now - self.cache_timestamp).seconds > self.cache_duration):
            try:
                pk_system_processes = get_excutable_pk_system_processes()
                import os
                # pk_ prefix 제거하고 파일명만 추출
                process_names = []
                for file_path in pk_system_processes:
                    file_name = os.path.basename(file_path).replace('.py', '')
                    # pk_ prefix 제거
                    if file_name.startswith('pk_'):
                        clean_name = file_name[3:]  # pk_ 제거
                    else:
                        clean_name = file_name
                    process_names.append(clean_name)
                
                self.process_cache = process_names
                self.cache_timestamp = now
            except Exception as e:
                ensure_printed(f"️ 프로세스 목록 가져오기 오류: {e}", print_color='yellow')
                return []
        
        return self.process_cache
    
    def analyze_morphemes(self, text: str) -> List[str]:
        """형태소 분석 (konlpy 사용)"""
        try:
            from konlpy.tag import Okt
            okt = Okt()
            
            # 명사, 동사, 형용사 추출
            nouns = okt.nouns(text)
            verbs = okt.verbs(text)
            adjectives = okt.adjectives(text)
            
            # 모든 형태소 합치기
            morphemes = nouns + verbs + adjectives
            
            # 중복 제거 및 빈 문자열 제거
            morphemes = list(set([m for m in morphemes if m.strip()]))
            
            return morphemes
            
        except ImportError:
            # konlpy가 없는 경우 개선된 단순 분리
            ensure_printed("️ konlpy가 설치되지 않아 개선된 단순 분리로 대체합니다.", print_color='yellow')
            return self._improved_simple_tokenize(text)
        except Exception as e:
            ensure_printed(f"️ 형태소 분석 오류: {e}", print_color='yellow')
            return self._improved_simple_tokenize(text)

    def _improved_simple_tokenize(self, text: str) -> List[str]:
        """개선된 단순 토큰화 (konlpy 없을 때 사용)"""
        import re
        
        # 1. 한글, 영문, 숫자만 추출 (특수문자 제거)
        tokens = re.findall(r'[가-힣a-zA-Z0-9]+', text)
        
        # 2. 2글자 이상만 유지
        tokens = [token for token in tokens if len(token) > 1]
        
        # 3. 한국어 조사 제거
        korean_particles = ['은', '는', '이', '가', '을', '를', '의', '에', '에서', '로', '으로', '와', '과', '도', '만', '부터', '까지', '처럼', '같이', '보다', '마다', '당', '씩', '마다', '당', '씩']
        tokens = [token for token in tokens if token not in korean_particles]
        
        # 4. 일반적인 불용어 제거
        stop_words = ['그', '이', '저', '것', '수', '등', '때', '곳', '말', '일', '년', '월', '일', '시', '분', '초']
        tokens = [token for token in tokens if token not in stop_words]
        
        return tokens

    def calculate_similarity(self, user_command: str, process_name: str) -> float:
        """사용자 명령어와 프로세스명 간의 유사도 계산"""
        try:
            # 사용자 명령어 형태소 분석
            user_morphemes = self.analyze_morphemes(user_command.lower())
            
            # 프로세스명 형태소 분석
            process_morphemes = self.analyze_morphemes(process_name.lower())
            
            if not user_morphemes or not process_morphemes:
                return 0.0
            
            # 공통 형태소 수 계산
            common_morphemes = set(user_morphemes) & set(process_morphemes)
            
            # Jaccard 유사도 계산
            union_morphemes = set(user_morphemes) | set(process_morphemes)
            
            if not union_morphemes:
                return 0.0
            
            similarity = len(common_morphemes) / len(union_morphemes)
            
            # 추가 가중치: 정확한 부분 문자열 매칭
            if any(morpheme in process_name.lower() for morpheme in user_morphemes):
                similarity += 0.2
            
            # 추가 가중치: 키워드 매칭
            keywords = {
                '크롬': ['chrome', 'browser', '웹'],
                '열기': ['open', 'start', '실행'],
                '파일': ['file', 'document'],
                '백업': ['backup', 'save', '저장'],
                '정리': ['clean', 'clear', '정리'],
                '시스템': ['system', 'os'],
                '프로세스': ['process', 'task'],
                '종료': ['kill', 'stop', 'end'],
                '확인': ['check', 'verify', 'status'],
                '설정': ['config', 'setting', 'option']
            }
            
            for user_word in user_morphemes:
                for keyword, related_words in keywords.items():
                    if user_word in keyword or keyword in user_word:
                        for related_word in related_words:
                            if related_word in process_name.lower():
                                similarity += 0.3
                                break
            
            return min(similarity, 1.0)
            
        except Exception as e:
            ensure_printed(f"️ 유사도 계산 오류: {e}", print_color='yellow')
            return 0.0
    
    def find_similar_processes(self, user_command: str, threshold: float = 0.1) -> List[Tuple[str, float]]:
        """사용자 명령어와 유사한 프로세스들 찾기"""
        process_names = self.get_process_names()
        similar_processes = []
        
        for process_name in process_names:
            similarity = self.calculate_similarity(user_command, process_name)
            if similarity >= threshold:
                similar_processes.append((process_name, similarity))
        
        # 유사도 순으로 정렬
        similar_processes.sort(key=lambda x: x[1], reverse=True)
        
        return similar_processes

    def find_dynamic_matches(self, command: str) -> List[str]:
        return self.dynamic_mapper.find_matching_functions(command)

    def print_dynamic_mapping(self, command: str):
        self.dynamic_mapper.print_current_mapping(command)


class JarvisState:
    """Jarvis 상태 관리 클래스"""
    def __init__(self):
        # 마이크 사용 가능 여부에 따라 초기 모드 결정
        if check_microphone_available():
            self.current_mode = JarvisMode.VOICE_CONVERSATION
            ensure_printed(" 마이크가 감지되어 음성 대화 모드로 시작합니다.", print_color='green')
        else:
            self.current_mode = JarvisMode.KEYBOARD_CONVERSATION
            ensure_printed("️ 키보드 대화 모드로 시작합니다.", print_color='cyan')
            
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
        self.process_matcher = ProcessMatcher()  # 프로세스 매칭기
        
        # 음성 인식 오류 카운터 추가
        self.voice_recognition_error_count = 0
        self.max_voice_errors = 30  # 30번 오류 후 CLI 모드로 전환
        
    def switch_mode(self, new_mode: JarvisMode):
        """모드 전환 - 마이크 상태 확인"""
        old_mode = self.current_mode
        
        # 음성 대화 모드로 전환하려면 마이크가 필요
        if new_mode in [JarvisMode.VOICE_CONVERSATION, JarvisMode.HYBRID]:
            if not self.microphone_available:
                ensure_printed(" 마이크가 연결되지 않아 음성 대화 모드로 전환할 수 없습니다.", print_color='red')
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
                ensure_printed(f"️ 프로세스 목록 캐시 오류: {e}", print_color='yellow')
        return self.process_cache

    def check_microphone_status(self):
        """마이크 상태 재확인 - 기존 함수 활용"""
        self.microphone_available = bool(is_mic_device_connected())
        return self.microphone_available
    
    def increment_voice_error_count(self):
        """음성 인식 오류 카운터 증가 및 키보드 대화 모드 전환 체크"""
        self.voice_recognition_error_count += 1
        ensure_printed(f" 음성 인식 오류 {self.voice_recognition_error_count}/{self.max_voice_errors}", print_color='yellow')
        
        # 디버깅 정보 추가
        if self.current_mode == JarvisMode.DEBUG:
            ensure_printed(f" [DEBUG] 현재 모드: {self.current_mode.value}, 마이크 상태: {self.microphone_available}", print_color='cyan')
        
        if self.voice_recognition_error_count >= self.max_voice_errors:
            ensure_printed(f"️ 음성 인식 오류가 {self.max_voice_errors}번 발생하여 키보드 대화 모드로 자동 전환합니다.", print_color='red')
            self.switch_mode(JarvisMode.KEYBOARD_CONVERSATION)
            self.voice_recognition_error_count = 0  # 카운터 리셋
            return True
        return False
    
    def reset_voice_error_count(self):
        """음성 인식 오류 카운터 리셋"""
        old_count = self.voice_recognition_error_count
        self.voice_recognition_error_count = 0
        ensure_printed(f" 음성 인식 성공! 오류 카운터 리셋: {old_count} → 0", print_color='green')


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


def get_user_command_via_mode(mode: JarvisMode, state: JarvisState = None) -> str:
    try:
        if mode == JarvisMode.VOICE_CONVERSATION:
            return get_voice_command_with_error_tracking(state)
        elif mode == JarvisMode.HYBRID:
            # 하이브리드 모드에서는 음성 우선, 실패시 키보드
            try:
                return get_voice_command_with_error_tracking(state)
            except:
                return get_cli_command(state)
        else:  # KEYBOARD_CONVERSATION, SILENT, DEBUG
            return get_cli_command(state)
    except KeyboardInterrupt:
        return "quit"
    except EOFError:
        return "quit"


def get_cli_command(state: JarvisState = None) -> str:
    """CLI 명령어 입력 받기 - 개선된 자동완성"""
    try:
        # 캐시된 프로세스 목록 사용
        pk_system_processes = state.get_cached_processes() if state else get_excutable_pk_system_processes()
        
        # 파일명만 추출 (경로 제거)
        import os
        process_names = [os.path.basename(f).replace('.py', '') for f in pk_system_processes]
        
        # 카테고리별 명령어 그룹화
        command_categories = {
            "모드 전환": [
                "mode keyboard", "keyboard mode", "키보드 모드", "mode cli", "cli mode", "텍스트 모드",
                "mode voice", "voice mode", "음성 모드", "음성 대화 모드",
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
        ensure_printed(f"️ 자동완성 오류: {e}", print_color='yellow')
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
                ensure_printed(f" {service_name} 인식: {command}", print_color='green')
                break
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                continue
        
        if command:
            return command.strip()
        else:
            ensure_printed(" 음성을 인식하지 못했습니다. CLI 모드로 전환합니다.", print_color='yellow')
            return get_cli_command()
            
    except Exception as e:
        ensure_printed(f" 음성 인식 중 오류: {e}", print_color='red')
        return get_cli_command()


def get_voice_command_with_error_tracking(state: JarvisState = None) -> str:
    """오류 추적 기능이 있는 음성 명령어 입력 받기"""
    import speech_recognition as sr
    
    recognizer = sr.Recognizer()
    ensure_printed(" 음성을 인식하고 있습니다...", print_color='blue')
    
    # 디버깅 정보 추가
    if state and state.current_mode == JarvisMode.DEBUG:
        ensure_printed(f" [DEBUG] 음성 인식 시작 - 현재 오류 카운터: {state.voice_recognition_error_count}", print_color='cyan')
    
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
                ensure_printed(f" {service_name} 인식: {command}", print_color='green')
                # 성공 시 오류 카운터 리셋
                if state:
                    state.reset_voice_error_count()
                break
            except sr.UnknownValueError:
                if state and state.current_mode == JarvisMode.DEBUG:
                    ensure_printed(f" [DEBUG] {service_name} 서비스에서 음성 인식 실패", print_color='cyan')
                continue
            except sr.RequestError:
                if state and state.current_mode == JarvisMode.DEBUG:
                    ensure_printed(f" [DEBUG] {service_name} 서비스 요청 오류", print_color='cyan')
                continue
        
        if command:
            return command.strip()
        else:
            # 음성 인식 실패 시 오류 카운터 증가
            if state:
                state.increment_voice_error_count()
            ensure_printed(" 음성을 인식하지 못했습니다.", print_color='yellow')
            
            # 30회 미만이면 음성 모드 유지, 30회 이상이면 키보드 모드로 전환
            if state and state.voice_recognition_error_count >= state.max_voice_errors:
                ensure_printed("️ 키보드 대화 모드로 전환합니다.", print_color='red')
                return get_cli_command(state)
            else:
                # 음성 모드 유지하면서 다시 시도
                ensure_printed(" 음성 인식을 다시 시도합니다...", print_color='blue')
                return get_voice_command_with_error_tracking(state)
            
    except Exception as e:
        # 음성 인식 오류 시 오류 카운터 증가
        if state:
            state.increment_voice_error_count()
        ensure_printed(f" 음성 인식 중 오류: {e}", print_color='red')
        
        # 30회 미만이면 음성 모드 유지, 30회 이상이면 키보드 모드로 전환
        if state and state.voice_recognition_error_count >= state.max_voice_errors:
            ensure_printed("️ 키보드 대화 모드로 전환합니다.", print_color='red')
            return get_cli_command(state)
        else:
            # 음성 모드 유지하면서 다시 시도
            ensure_printed(" 음성 인식을 다시 시도합니다...", print_color='blue')
            return get_voice_command_with_error_tracking(state)


def suggest_and_execute_process(user_command: str, state: JarvisState) -> bool:
    """유사한 프로세스 제안 및 실행"""
    try:
        # 유사한 프로세스 찾기
        similar_processes = state.process_matcher.find_similar_processes(user_command, threshold=0.1)
        
        if not similar_processes:
            ensure_printed(f" '{user_command}'와 유사한 프로세스를 찾을 수 없습니다.", print_color='red')
            return False
        
        # 상위 5개만 표시
        top_similar = similar_processes[:5]
        
        ensure_printed(f" '{user_command}'와 유사한 프로세스들:", print_color='cyan')
        for i, (process_name, similarity) in enumerate(top_similar, 1):
            similarity_percent = similarity * 100
            ensure_printed(f"  {i}. {process_name} (유사도: {similarity_percent:.1f}%)", print_color='white')
        
        # 사용자 선택 받기
        ensure_printed("실행할 프로세스 번호를 선택하세요 (0: 취소):", print_color='yellow')
        try:
            choice = input("선택=").strip()
            if not choice or choice == "0":
                ensure_printed("취소되었습니다.", print_color='yellow')
                return True
            
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(top_similar):
                selected_process = top_similar[choice_idx][0]
                
                # 실행 확인
                ensure_printed(f"'{selected_process}' 프로세스를 실행하시겠습니까? (y/n):", print_color='yellow')
                confirm = input("확인=").strip().lower()
                
                if confirm in ['y', 'yes', '예', '네']:
                    # 프로세스 실행
                    return execute_pk_process(selected_process, state)
                else:
                    ensure_printed("실행이 취소되었습니다.", print_color='yellow')
                    return True
            else:
                ensure_printed("잘못된 선택입니다.", print_color='red')
                return True
                
        except ValueError:
            ensure_printed("숫자를 입력해주세요.", print_color='red')
            return True
        except KeyboardInterrupt:
            ensure_printed("취소되었습니다.", print_color='yellow')
            return True
            
    except Exception as e:
        ensure_printed(f" 프로세스 제안 중 오류: {e}", print_color='red')
        return False


def execute_pk_process(process_name: str, state: JarvisState) -> bool:
    """PK 프로세스 실행"""
    try:
        # pk_ prefix 추가
        full_process_name = f"pk_{process_name}"
        
        # 실행 가능한 프로세스 목록에서 찾기
        pk_system_processes = get_excutable_pk_system_processes()
        
        import os
        for file_to_execute in pk_system_processes:
            file_name = os.path.basename(file_to_execute).replace('.py', '')
            if file_name == full_process_name:
                try:
                    prefix = pk_
                    file_title = os.path.basename(file_to_execute)
                    file_title = file_title.removeprefix(prefix)
                    ensure_py_system_process_ran_by_pnx(file_to_execute, file_title)
                    ensure_printed(f" {process_name} 실행 완료", print_color='green')
                    return True
                except Exception as e:
                    ensure_printed(f" {process_name} 실행 중 오류: {e}", print_color='red')
                    return True
        
        ensure_printed(f" {process_name} 프로세스를 찾을 수 없습니다.", print_color='red')
        return False
        
    except Exception as e:
        ensure_printed(f" 프로세스 실행 중 오류: {e}", print_color='red')
        return False


def process_command(command: str, state: JarvisState) -> bool:
    """명령어 처리 - 개선된 에러 처리"""
    command = command.lower()
    
    try:
        # 마이크 상태 확인 명령어
        if command in ["check mic", "마이크 확인"]:
            if state.check_microphone_status():
                ensure_printed(" 마이크가 정상적으로 연결되어 있습니다.", print_color='green')
                if state.current_mode == JarvisMode.KEYBOARD_CONVERSATION:
                    ensure_printed(" 'mode voice' 명령어로 음성 대화 모드로 전환할 수 있습니다.", print_color='cyan')
            else:
                ensure_printed(" 마이크가 연결되지 않았습니다.", print_color='red')
            return True
        
        # 모드 전환 명령어들
        if command in ["mode keyboard", "keyboard mode", "키보드 모드", "mode cli", "cli mode", "텍스트 모드"]:
            state.switch_mode(JarvisMode.KEYBOARD_CONVERSATION)
            return True
        elif command in ["mode voice", "voice mode", "음성 모드", "음성 대화 모드"]:
            if state.microphone_available:
                state.switch_mode(JarvisMode.VOICE_CONVERSATION)
            else:
                ensure_printed(" 마이크가 연결되지 않아 음성 대화 모드로 전환할 수 없습니다.", print_color='red')
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
        
        # 종료 명령어
        if command in ["quit", "exit", "종료", "나가기"]:
            response = f"{PkMessages2025.QUIT_MESSAGE}"
            if state.current_mode != JarvisMode.SILENT:
                ensure_spoken(response)
            ensure_printed(f" {PkMessages2025.QUITTING}...", print_color='yellow')
            return False
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
            # 동적 매핑 정보 항상 출력
            state.process_matcher.print_dynamic_mapping(command)
            
            # 1. 동적 매핑 우선 실행
            dynamic_matches = state.process_matcher.find_dynamic_matches(command)
            if dynamic_matches:
                ensure_printed(f" 동적으로 매핑된 함수: {dynamic_matches}", print_color='cyan')
                # 실제 실행은 나중에 구현, 일단 매핑 정보만 출력
                return True
            
            # 2. 정확한 프로세스명 매칭 시도
            if try_execute_pk_process(command, state):
                return True
            
            # 3. 유사도 기반 제안
            if suggest_and_execute_process(command, state):
                return True
            
            # 매칭되지 않은 경우
            response = f"'{command}' {PkMessages2025.UNKNOWN_COMMAND}. 자연어로 프로세스를 설명해보세요."
            if state.current_mode != JarvisMode.SILENT:
                ensure_spoken(response)
            ensure_printed(f" {response}", print_color='red')

        return True
        
    except Exception as e:
        error_msg = f" 명령어 처리 중 오류: {e}"
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

 모드 전환:
   • mode keyboard/키보드 모드: 키보드 대화 모드
   • mode voice/음성 대화 모드: 음성 대화 모드
   • mode hybrid/하이브리드 모드: 키보드 + 음성 모드
   • mode silent/무음 모드: 음성 출력 없음
   • mode debug/디버그 모드: 디버그 정보 표시

️ 시스템 명령어:
  • wsl 활성화: WSL 배포판 활성화
  • history: 명령어 히스토리 표시
  • status: 현재 상태 표시

 PK 시스템 프로세스:
  • 정확한 프로세스명 입력: 직접 실행
  • 자연어 명령어: 유사한 프로세스 제안 후 선택 실행
  • 예: "크롬 열기", "파일 백업", "시스템 정리" 등

 팁: 자연어로 원하는 작업을 설명하면 유사한 프로세스를 찾아 제안합니다!
    """
    ensure_printed(help_text, print_color='cyan')


def try_execute_pk_process(command: str, state: JarvisState) -> bool:
    """pk_system 프로세스 실행 시도"""
    try:
        # 실행 가능한 프로세스 목록 가져오기
        pk_system_processes = get_excutable_pk_system_processes()
        
        # 파일명만 추출하여 매칭
        import os
        for file_to_excute in pk_system_processes:
            file_name = os.path.basename(file_to_excute).replace('.py', '')
            if command.lower() == file_name.lower():
                try:
                    prefix= pk_
                    file_to_excute = file_to_excute
                    file_title = os.path.basename(file_to_excute)
                    file_title = file_title.removeprefix(prefix)
                    ensure_py_system_process_ran_by_pnx(file_to_excute, file_title)
                    ensure_printed(f" {file_name} 완료", print_color='green')
                    return True
                except Exception as e:
                    ensure_printed(f" {file_name} 실행 중 오류: {e}", print_color='red')
                    return True
        
        return False
        
    except Exception as e:
        ensure_printed(f"️ 프로세스 실행 시도 중 오류: {e}", print_color='yellow')
        return False


def show_command_history(state: JarvisState):
    """명령어 히스토리 표시"""
    ensure_printed(" 명령어 히스토리:", print_color='cyan')
    for i, entry in enumerate(state.command_history[-10:], 1):  # 최근 10개
        timestamp = entry['timestamp'].strftime("%H:%M:%S")
        ensure_printed(f"  {i}. [{timestamp}] {entry['command']} ({entry['mode']})", print_color='white')


def show_current_status(state: JarvisState):
    """현재 상태 표시"""
    ensure_printed(" Jarvis 현재 상태:", print_color='cyan')
    ensure_printed(f"  모드: {state.current_mode.value}", print_color='white')
    ensure_printed(f"  마이크: {'연결됨' if state.microphone_available else '연결되지 않음'}", print_color='white')
    ensure_printed(f"  실행 중: {'예' if state.is_running else '아니오'}", print_color='white')
    ensure_printed(f"  명령어 수: {len(state.command_history)}", print_color='white')
    
    # 사용 가능한 프로세스 수 표시
    try:
        pk_system_processes = get_excutable_pk_system_processes()
        ensure_printed(f"  사용 가능한 프로세스: {len(pk_system_processes)}개", print_color='white')
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

    db_path = F_PK_SYSTEM_SQLITE
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
        ensure_printed(f"️ 인사 기록 DB 오류: {e}", print_color='yellow')
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
            user_input = get_user_command_via_mode(state.current_mode, state)
            
            if user_input:
                # 명령어 히스토리에 추가
                state.add_command_to_history(user_input) 
                state.last_command_time = datetime.now()
            
            # 명령어 처리
            if not process_command(user_input, state):
                break
                
            ensure_printed("-" * 50, print_color='white')
            
        except KeyboardInterrupt:
            ensure_printed("\n️ 사용자가 중단했습니다.", print_color='yellow')
            break
        except Exception as e:
            error_msg = f" {PkMessages2025.ERROR_OCCURRED}: {e}"
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
    ensure_printed(" Jarvis를 종료합니다.", print_color='green')
 