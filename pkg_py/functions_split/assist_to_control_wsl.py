from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.functions_split.pk_print import pk_print


def assist_to_control_wsl(**pk_config):
    from colorama import init as pk_colorama_init
    import inspect
    import subprocess
    import time
    pk_colorama_init_once()
    func_n = inspect.currentframe().f_code.co_name

    class _PkWslController:
        def __init__(self):
            self._pk_wsl_controller_version = pk_config.get('pk_wsl_controller_version', 'auto_version.1.0')
            self._pk_wsl_cmd_exec_map_dict = pk_config.get('pk_wsl_cmd_exec_map_dict', {})
            self._pk_wsl_cmd_list = pk_config.get('pk_wsl_cmd_list', [])
            self._pk_wsl_cmd_map_dict = pk_config.get('pk_wsl_cmd_map_dict', {})
            self._pk_wsl_cmd_list_len = pk_config.get('pk_wsl_cmd_list_len', 0)

        def _print_pk_wsl_ver(self, version):
            pk_print(version, print_color='blue')

        def _print_pk_available_wsl_cmd_list(self):
            pk_print("======== Available WSL Commands ========")
            for idx, cmd in enumerate(self._pk_wsl_cmd_list):
                actual_cmd = ' '.join(self._pk_wsl_cmd_exec_map_dict.get(cmd, [cmd]))
                pk_print(f'wsl {idx} : {actual_cmd}')

        def _excute_wsl_cmd(self, idx_by_user_input, sys_arg2=None):

            user_cmd_key = self._pk_wsl_cmd_map_dict.get(idx_by_user_input)
            exec_cmd = self._pk_wsl_cmd_exec_map_dict.get(user_cmd_key)

            if exec_cmd is None:
                pk_print(f"Unknown command mapping for '{user_cmd_key}'", print_color='red')
                return

            if LTA:
                pk_print(f"Trying to run: {exec_cmd}")

            if "-d" in exec_cmd:
                real_distro = exec_cmd[-1]
                current_installed_distros = get_installed_wsl_distros()
                if not any(d['name'].strip().lower() == real_distro.strip().lower() for d in current_installed_distros):
                    pk_print(f"Distro '{real_distro}' not found. Please install it first.", print_color='red')
                    return

            try:
                if LTA:
                    pk_print(f"{STAMP_TRY_GUIDE} silently ran: {' '.join(exec_cmd)}")
                    pk_print(f"{' '.join(exec_cmd)} started in background", print_color='green')
                if "-d" in exec_cmd:
                    state_before_list = get_wsl_distro_info_std_list()
                    subprocess.Popen(exec_cmd, creationflags=subprocess.CREATE_NO_WINDOW)
                    while 1:
                        state_after_list = get_wsl_distro_info_std_list()
                        if state_before_list != state_after_list:
                            print_wsl_distro_info_std_list()
                elif '--shutdown' in exec_cmd:
                    state_before_list = get_wsl_distro_info_std_list()
                    subprocess.Popen(['wsl', '--shutdown'], creationflags=subprocess.CREATE_NO_WINDOW)
                    while 1:
                        state_after_list = get_wsl_distro_info_std_list()
                        if LTA:
                            pk_print(f'''state_before_list={state_before_list} {'%%%FOO%%%' if LTA else ''}''')
                            pk_print(f'''state_after_list={state_after_list} {'%%%FOO%%%' if LTA else ''}''')
                        if state_before_list != state_after_list:
                            print_wsl_distro_info_std_list()
                            break
                elif '-l' in exec_cmd and '-v' in exec_cmd:
                    print_wsl_distro_info_std_list()

            except Exception as e:
                pk_print(f"Failed to run {' '.join(exec_cmd)}: {e}", print_color='red')

        def _guide_error_mssage(self):
            pk_print(f'''{PkMessages2025.NOT_PREPARED_YET}{'%%%FOO%%%' if LTA else ''}''', print_color='green', mode_verbose=0)

    _pwc = _PkWslController()
    cnt_loop = 0
    pk_sys_argv = []
    while 1:
        if cnt_loop == 0:  # trigger : oneshoot
            cnt_loop = cnt_loop + 1
            # pk_sys_argv = ['wsl', '0']  # wsl 0 실행
        if is_office_pc():
            if cnt_loop == 1:
                cnt_loop = cnt_loop + 1
                # pk_sys_argv = ['wsl', '1']
                # pk_sleep(seconds = 4) # wsl 실행시간 대기
            if cnt_loop == 2:
                cnt_loop = cnt_loop + 1
                pk_sys_argv = ['wsl', '3']
                pk_seconds_limit = 5
                pk_time_s = time.time()
                while 1:
                    elapsed = time.time() - pk_time_s
                    if elapsed >= pk_seconds_limit:
                        pk_print(f'''time is limited (pk_time_limit={pk_seconds_limit}) {'%%%FOO%%%' if LTA else ''}''')
                        raise
                    user_input = pk_input_with_timeout("계속 wsl 환경을 쓸까요? 아무것도 안하면 환경이 종료됩니다. Enter를 누르면 유지됩니다",
                                                       timeout_secs=int(pk_seconds_limit - elapsed))
                    if user_input == "":
                        break
                    elif user_input is None:
                        pk_print(f'''time is limited (pk_time_limit={pk_seconds_limit}) {'%%%FOO%%%' if LTA else ''}''')
                        raise

        else:
            if cnt_loop == 1:
                pk_sys_argv = ['wsl', '1']
                cnt_loop = cnt_loop + 1

        if len(pk_sys_argv) == 1:
            _pwc._print_pk_available_wsl_cmd_list()

        elif len(pk_sys_argv) == 2:
            idx_map = get_idx_list(item_iterable=_pwc._pk_wsl_cmd_map_dict)
            idx_map = list(map(str, idx_map))

            if pk_sys_argv[1] in ['--version', '-v', 'ver']:
                _pwc._print_pk_wsl_ver(version=_pwc._pk_wsl_controller_version)

            elif pk_sys_argv[1] in ['--list', '-l', 'ls'] or pk_sys_argv == ['wsl', 'ls']:
                _pwc._print_pk_available_wsl_cmd_list()

            elif pk_sys_argv[1] in idx_map:
                _pwc._excute_wsl_cmd(idx_by_user_input=int(pk_sys_argv[1]))

            else:
                _pwc._guide_error_mssage()

        elif len(pk_sys_argv) == 3:
            idx_map = get_idx_list(item_iterable=_pwc._pk_wsl_cmd_map_dict)
            idx_map = list(map(str, idx_map))
            if pk_sys_argv[1] in idx_map:
                _pwc._excute_wsl_cmd(idx_by_user_input=int(pk_sys_argv[1]))

        pk_wsl_cmd_from_input = input(
            rf'{pk_get_colorful_working_str_with_stamp_enviromnet(func_n=func_n, ment="WRITE PK WSL CMD")} >>>')
        pk_wsl_cmd_from_input = pk_wsl_cmd_from_input.strip()
        pk_wsl_cmd_list = pk_wsl_cmd_from_input.split(" ")
        pk_sys_argv = pk_wsl_cmd_list
