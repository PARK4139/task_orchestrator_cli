from urllib.parse import urlparse
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style


def debug_state_for_py_data_type(pk_stamp, data_working, highlight_config_dict=None, with_LTA=1):
    pk_debug_state_for_py_data_type_v2(pk_stamp=pk_stamp, data_working=data_working,
                                       highlight_config_dict=highlight_config_dict, with_LTA=with_LTA)
