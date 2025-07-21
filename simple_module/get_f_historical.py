from pkg_py.pk_system_layer_directories import D_PKG_TXT
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style


def get_f_historical(file_id):
    f_historical = rf'{D_PKG_TXT}/historical_{file_id}.txt'
    f_historical = get_pnx_os_style(f_historical)
    return f_historical
