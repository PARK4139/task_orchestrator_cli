import logging
import time
import traceback

from functions import ensure_slept
from functions.ensure_console_paused import ensure_console_paused
from objects.pk_etc import PK_UNDERLINE
from objects.pk_local_test_activate import LTA
from sources.objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP


class PkColorfulLoggingFormatter(logging.Formatter):
    """컬러풀한 로깅 포맷터 - DEBUG=GREY, WARNING=YELLOW, 타임스탬프=GREY, 파일명=GREY, 메시지=CYAN"""


    # ANSI 컬러 코드
    COLORS = TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP

    # 로그 레벨별 컬러 매핑
    LEVEL_COLORS = {
        'DEBUG': 'GREY',
        # 'INFO': 'GREY',
        'INFO': 'CYAN',
        'WARNING': 'YELLOW',
        'ERROR': 'RED',
        'CRITICAL': 'RED'
    }

    def __init__(self, use_pkmessage=True):
        super().__init__()
        self.use_pkmessage = use_pkmessage

    def format(self, record):
        """로그 레코드를 컬러풀하게 포맷팅"""
        # print(f"--- FORMATTER CALLED FOR LEVEL: {record.levelname} ---") # Diagnostic print
        try:
            # PkMessage 사용 여부에 따라 레벨명 변경
            level_name = record.levelname
            if self.use_pkmessage:
                level_name = self._get_pkmessage_level(record.levelname)

            # 타임스탬프 (GREY)
            timestamp = self.formatTime(record, datefmt='%Y-%m-%d %H:%M:%S')
            timestamp_colored = f"{self.COLORS['GREY']}{timestamp}{self.COLORS['RESET']}"

            # 레벨명 (각 레벨별 컬러)
            level_color = self.LEVEL_COLORS.get(record.levelname, 'WHITE')
            level_colored = f"{self.COLORS[level_color]}{level_name}{self.COLORS['RESET']}"

            # 파일명:라인번호 (GREY)
            file_info = f"{record.filename}:{record.lineno}"
            file_info_colored = f"{self.COLORS['GREY']}{file_info}{self.COLORS['RESET']}"

            # 메시지 (CYAN)
            message = record.getMessage()
            # Escape curly braces in the message to prevent f-string errors
            escaped_message = message.replace('{', '{{').replace('}', '}}')
            # message_colored = f"{self.COLORS['CYAN']}{escaped_message}{self.COLORS['RESET']}"
            message_colored = f"{self.COLORS['GREY']}{escaped_message}{self.COLORS['RESET']}"

            # 대괄호 (WHITE)
            bracket_open = self.COLORS['WHITE'] + '[' + self.COLORS['RESET']
            bracket_close = self.COLORS['WHITE'] + ']' + self.COLORS['RESET']

            # 최종 포맷 조립
            formatted = f"{bracket_open}{timestamp_colored}{bracket_close} {bracket_open}{level_colored}{bracket_close} {bracket_open}{file_info_colored}{bracket_close} {bracket_open}{message_colored}{bracket_close}"

            return formatted

        except Exception as e:
            print("--- PK SYSTEM LOG DEBUG(TEST PRINT)---")
            print(PK_UNDERLINE)
            traceback.print_exc()
            print(PK_UNDERLINE)
            time.sleep(10000000)


    def _get_pkmessage_level(self, level_name):
        """로그 레벨을 PkMessage로 변환"""
        try:
            # lazy import로 순환 import 방지
            from sources.objects.pk_map_texts import PkTexts

            level_mapping = {
                'DEBUG': PkTexts.DEBUG if hasattr(PkTexts, 'DEBUG') else 'DEBUG',
                'INFO': PkTexts.INFO if hasattr(PkTexts, 'INFO') else 'INFO',
                'WARNING': PkTexts.WARNING if hasattr(PkTexts, 'WARNING') else 'WARNING',
                'ERROR': PkTexts.ERROR if hasattr(PkTexts, 'ERROR') else 'ERROR',
                'CRITICAL': PkTexts.ERROR if hasattr(PkTexts, 'ERROR') else 'CRITICAL'
            }

            return level_mapping.get(level_name, level_name)

        except ImportError:
            # PkMessage import 실패 시 기본값 사용
            return level_name
