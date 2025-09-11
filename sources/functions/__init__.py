"""
this code for : deduplicate `import script`.

TODO :
    collect all `import scripts` from  functions/
    parse and modify as

    from .does_pnx_exist import is_pnx_existing

"""
from .does_pnx_exist import is_pnx_existing
from .ensure_chcp_65001 import ensure_chcp_65001
from .ensure_command_executed import ensure_command_executed
from .ensure_console_cleared import ensure_console_cleared
from .ensure_pnx_made import ensure_pnx_made
from .ensure_slept import ensure_slept
from .ensure_spoken import ensure_spoken
from .ensure_value_completed import ensure_value_completed
from .get_fzf_command import get_fzf_command
from .get_os_n import get_os_n
from .get_pnx_os_style import get_pnx_os_style
from .get_time_as_ import get_time_as_

# __all__을 정의하여 명시적으로 export할 함수들 지정
# __all__ = [
    # 'get_time_as_',.
    # 'ensure_spoken',
    # 'ensure_command_executed',
    # 'ensure_slept',
    # 'is_pnx_existing',
    # 'get_pnx_os_style',
    # 'ensure_value_completed',
    # 'ensure_console_cleared',
    # 'ensure_pnx_made',
    # 'get_os_n',
    # 'ensure_chcp_65001',
    # 'get_fzf_command',
# ]
