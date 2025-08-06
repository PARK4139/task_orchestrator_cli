from pathlib import Path
from typing import Union

from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_pnx_os_style(pnx: Union[str, Path]) -> Union[str, Path]:
    from pathlib import Path
    from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
    from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
    from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

    if isinstance(pnx, Path):
        return pnx
    elif isinstance(pnx, str):
        pnx = str(Path(pnx))  # 안전한 정규화

    if is_os_wsl_linux():
        return get_pnx_wsl_unix_style(pnx)
    elif is_os_windows():
        return get_pnx_windows_style(pnx)
    else:
        return get_pnx_unix_style(pnx)
