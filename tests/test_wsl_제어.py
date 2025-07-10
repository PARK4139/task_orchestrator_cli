def test_wsl_제어():
    from pkg_py.pk_core import pk_debug_state_for_py_data_type, check_installed_wsl
    from pkg_py.pk_colorful_cli_util import pk_print
    import sys
    from pkg_py.pk_core import LTA
    state_wsl_installed, pk_wsl_cmd_map_dict = check_installed_wsl()
    if not state_wsl_installed:
        pk_debug_state_for_py_data_type(pk_stamp='%%%FOO%%%-2', data_working=pk_wsl_cmd_map_dict)
        pk_print("wsl installed", print_color='red')
        sys.exit(0)
    else:
        if LTA:
            pk_debug_state_for_py_data_type(pk_stamp='%%%FOO%%%-3', data_working=pk_wsl_cmd_map_dict)
            pk_print("wsl installed", print_color='green')

