"""
Functions Split Package - Common imports for frequently used functions
TODO : 모든 import 문을 수집하여 이곳으로 이동.
"""

# 자주 사용되는 함수들을 여기서 import하여 간소화된 import 문 사용 가능 한지 확인필요
from .get_time_as_ import get_time_as_
from .ensure_printed import ensure_printed
from .ensure_spoken import ensure_spoken
from .ensure_spoken_hybrid import ensure_spoken_hybrid, VoiceConfig
from .ensure_command_excuted_to_os import ensure_command_excuted_to_os
from .ensure_slept import ensure_slept
from .does_pnx_exist import does_pnx_exist
from .get_pnx_os_style import get_pnx_os_style
from .get_value_completed import get_value_completed
from .ensure_console_cleared import ensure_console_cleared
from .ensure_pnx_made import ensure_pnx_made
from .get_os_n import get_os_n
from .chcp_65001 import chcp_65001
from .get_fzf_command import get_fzf_command

# __all__을 정의하여 명시적으로 export할 함수들 지정
__all__ = [
    'get_time_as_',
    'ensure_printed',
    'ensure_spoken',
    'ensure_spoken_hybrid',
    'VoiceConfig',
    'ensure_command_excuted_to_os',
    'ensure_slept',
    'does_pnx_exist',
    'get_pnx_os_style',
    'get_value_completed',
    'ensure_console_cleared',
    'ensure_pnx_made',
    'get_os_n',
    'chcp_65001',
    'get_fzf_command',
]
