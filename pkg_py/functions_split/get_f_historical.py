from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.pk_system_object.directories import D_PKG_TXT


def get_f_historical(file_id):
    f_historical = rf'{D_PKG_TXT}/historical_{file_id}.txt'
    ensure_pnx_made(pnx=f_historical, mode="f")
    f_historical = get_pnx_os_style(f_historical)
    return f_historical
