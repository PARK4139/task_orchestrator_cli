import win32com.client
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from bs4 import ResultSet
from pkg_py.simple_module.part_014_pk_print import pk_print


def get_data_from_f_toml(f):
    import tomllib
    with open(f, "rb") as f_obj:
        data = tomllib.load(f_obj)
    return data
