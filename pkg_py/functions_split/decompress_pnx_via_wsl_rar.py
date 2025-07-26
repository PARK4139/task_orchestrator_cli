

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def decompress_pnx_via_wsl_rar(f_zip, dst):  # 테스트필요 f_rar 같음
    import os.path

    if not os.path.exists(f_zip):
        raise FileNotFoundError(f"Source file not found: {f_zip}")

    if not f_zip.lower().endswith('.rar'):
        raise ValueError("The source file must be a .rar file")
    if not os.path.exists(dst):
        os.makedirs(dst)
    f_zip = get_pnx_wsl_unix_style(pnx=f_zip)
    dst = get_pnx_wsl_unix_style(pnx=dst)

    try:
        cmd = f"wsl rar x {f_zip} {dst}"
        ensure_command_excuted_to_os(cmd=cmd)

    except Exception as e:
        raise RuntimeError(f"Failed to decompress the .rar file: {e}")
