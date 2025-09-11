from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.ensure_command_executed import ensure_command_executed

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_window_to_front import ensure_window_to_front


def run_powershell_exe():
    ensure_command_executed('start "" powershell', mode='a')
    ensure_window_to_front(window_title_seg = rf'powershell')
