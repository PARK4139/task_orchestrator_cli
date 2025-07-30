import os

from pkg_py.system_object.directories import D_PKG_WINDOWS


def ensure_pk_system_enabled():
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.system_object.files import F_ENSURE_PK_SYSTEM_ENABLED_CMD

    os.chdir(D_PKG_WINDOWS)
    ensure_pk_system_enabled_cmd = get_pnx_os_style(rf"{F_ENSURE_PK_SYSTEM_ENABLED_CMD}")
    ensure_command_excuted_to_os(cmd=f'start ""  "{ensure_pk_system_enabled_cmd}"')
    # ensure_command_excuted_to_os(cmd=f'call "{ensure_pk_system_enabled_cmd}"')
