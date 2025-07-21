from pkg_py.simple_module.part_001_ensure_pnx_made import ensure_pnx_made
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f


def set_values_to_historical_file(f_historical, values):
    ensure_pnx_made(pnx=f_historical, mode='f')
    write_list_to_f(f=f_historical, working_list=values, mode="w")
