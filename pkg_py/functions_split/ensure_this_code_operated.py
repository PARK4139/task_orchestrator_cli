from types import ModuleType


def ensure_this_code_operated(ipdb: ModuleType):
    from pkg_py.functions_split.ensure_console_debuggable import ensure_console_debuggable
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP

    # based on from types import ModuleType
    ensure_printed(f"{PK_ANSI_COLOR_MAP['GREEN']}here! here! here! here! here! here! here! here! here! here! here! here! {PK_ANSI_COLOR_MAP['RESET']}")
    ensure_console_debuggable(ipdb)
