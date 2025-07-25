from types import ModuleType

from pkg_py.functions_split.ensure_console_debuggable import ensure_console_debuggable
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP


def ensure_this_code_operated(ipdb: ModuleType):
    # based on from types import ModuleType
    pk_print(f"{PK_ANSI_COLOR_MAP['GREEN']}here! here! here! here! here! here! here! here! here! here! here! here! {PK_ANSI_COLOR_MAP['RESET']}")
    ensure_console_debuggable(ipdb)


