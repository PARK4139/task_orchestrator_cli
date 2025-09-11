from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def copy_pnx_to_wsl(f, dst="~/Downloads/"):
    f = get_pnx_wsl_unix_style(f)
    ensure_command_executed(cmd=rf'wsl sudo cp -r {f} {dst}')
