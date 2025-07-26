def test_wsl_제어():
    # from pkg_py.system_object.500_live_logic import debug_state_for_py_data_type, check_installed_wsl
    # from pkg_py.system_object.print_util import print
    import sys
    # from pkg_py.system_object.500_live_logic import LTA
    state_wsl_installed, pk_wsl_cmd_map_dict = check_installed_wsl()
    if not state_wsl_installed:
        pk_debug_state_for_py_data_type(pk_stamp='%%%FOO%%%-2', data_working=pk_wsl_cmd_map_dict)
        ensure_printed("wsl installed", print_color='red')
        sys.exit(0)
    else:
        if LTA:
            pk_debug_state_for_py_data_type(pk_stamp='%%%FOO%%%-3', data_working=pk_wsl_cmd_map_dict)
            ensure_printed("wsl installed", print_color='green')

