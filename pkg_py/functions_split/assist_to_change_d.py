from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_TBD_pnx_working_with_idx_dict import get_TBD_pnx_working_with_idx_dict
from pkg_py.functions_split.get_d_working_in_python import get_pwd_in_python
from pkg_py.functions_split.get_list_from_f import get_list_from_f
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.pk_cd import pk_cd
from pkg_py.functions_split.pk_debug_state_for_py_data_type import pk_debug_state_for_py_data_type
from pkg_py.functions_split.pk_get_colorful_str_working_with_stamp_enviromnet import pk_get_colorful_str_working_with_stamp_enviromnet
from pkg_py.functions_split.pk_input_validated import pk_input_validated
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.save_d_to_f import save_d_to_f
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.directories import D_PKG_PY, D_DESKTOP, D_PKG_TXT, D_WORKING, D_DOWNLOADS, D_J_DRIVE, D_I_DRIVE, D_H_DRIVE, D_G_DRIVE, D_F_DRIVE, D_D_DRIVE, D_C_DRIVE
from pkg_py.system_object.directories_reuseable import D_PROJECT, D_HOME
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE


def assist_to_change_d():
    import os
    import inspect
    import sys

    pk_colorama_init_once()

    f_cd_txt = os.path.join(D_PKG_TXT, "pk_cd.txt")
    if not does_pnx_exist(f_cd_txt):
        ensure_pnx_made(f_cd_txt, mode='f')

    minus_list = [rf"{D_PKG_PY}/???.py"]
    minus_list = [get_pnx_os_style(element) for element in minus_list]
    from os import path

    plus_list = [
        D_PKG_PY,
        D_PROJECT,
        D_WORKING,
        D_DOWNLOADS,
        D_HOME,
        D_DESKTOP,
        D_C_DRIVE,
        D_D_DRIVE,
        D_F_DRIVE,
        D_G_DRIVE,
        D_H_DRIVE,
        D_I_DRIVE,
        D_J_DRIVE,
    ]
    plus_list = [p for p in plus_list if path.exists(p)]  # 존재하는 경로만 필터링
    plus_list = [get_pnx_os_style(p) for p in plus_list]  # 파일경로 OS 스타일로 업데이트

    pk_cmd_n = 'cd'
    pk_cmd_single_dict = {
        '.': '.',
        'cls': 'cls',
        'cmd': 'cmd',
    }
    func_n = inspect.currentframe().f_code.co_name
    # stamp_func_n = rf'({func_n})'

    first_loop = 1
    if LTA:
        pk_print(f'''first_loop={first_loop} {'%%%FOO%%%' if LTA else ''}''')

    while 1:
        d_working_list = get_pnx_list(with_walking=0, d_working=get_pwd_in_python(), filter_option='d')
        d_working_with_idx_dict = get_TBD_pnx_working_with_idx_dict(origin_list=d_working_list, minus_list=minus_list,
                                                                    pnx_plus_list=plus_list)

        pk_cmd = None
        pk_cmd_str = None
        pk_sys_argv = None
        if first_loop:  # trigger : oneshoot

            first_loop = 0
            if LTA:
                pk_print(f'''first_loop={first_loop} {'%%%FOO%%%' if LTA else ''}''')
            pk_cmd = ''
            pk_cmd_str = pk_cmd.strip()
            pk_sys_argv = pk_cmd_str.split(" ")
        else:
            pk_cmd = pk_input_validated(str_working='', mode_verbose=0, mode_upper=0, mode_blank_validation=0,
                                        input_str=rf'''{pk_get_colorful_str_working_with_stamp_enviromnet(func_n=func_n, ment=f'{get_pwd_in_python()} >>>')}''')  # best practice input
            pk_cmd_str = pk_cmd.strip()
            pk_sys_argv = pk_cmd_str.split(" ")

        if len(pk_sys_argv) >= 2:
            if not str.isdigit(pk_sys_argv[1]):
                pk_print(f'''{STAMP_TRY_GUIDE} cd {{index}} , index is not str ' {'%%%FOO%%%' if LTA else ''}''',
                         print_color='red')
                continue
            if str.isdigit(pk_sys_argv[1]):
                if int(pk_sys_argv[1]) >= len(d_working_with_idx_dict):
                    pk_print(f'''{STAMP_TRY_GUIDE} cd {{index}} , out of index' {'%%%FOO%%%' if LTA else ''}''',
                             print_color='red')
                    continue

        if LTA:
            pk_print(f'''pk_cmd_argv={pk_sys_argv} {'%%%FOO%%%' if LTA else ''}''')
            pk_print(f'''len(pk_cmd_argv)={len(pk_sys_argv)} {'%%%FOO%%%' if LTA else ''}''')

        if len(pk_sys_argv) == 1:
            if pk_cmd_single_dict['.'] == pk_sys_argv[0]:
                if is_os_windows():
                    cmd_to_os(f'explorer.exe {get_pwd_in_python()}')
                continue
            elif pk_cmd_single_dict['cls'] == pk_sys_argv[0]:  # fail
                if is_os_windows():
                    cmd_to_os(f'cls')
                continue
            elif pk_cmd_single_dict['cmd'] == pk_sys_argv[0]:
                if is_os_windows():
                    # cmd_to_os(f'start "" cmd')
                    cmd_to_os(f'cmd /k')
                continue
            elif pk_cmd_str == "":
                highlight_config_dict = {
                    "green": [
                        'cd',
                        pk_cmd_n
                    ],
                    'red': [
                        'Stopped'
                    ],
                }
                list_to_print = []
                for idx, pnx_working in enumerate(d_working_with_idx_dict):
                    list_to_print.append(f'''{pk_cmd_n} {idx:<2} ({d_working_with_idx_dict[idx]})''')
                pk_debug_state_for_py_data_type(pk_stamp='%%%FOO%%%-1', data_working=list_to_print,
                                                highlight_config_dict=highlight_config_dict, with_LTA=0)
                continue
            else:
                pk_print(f'''{PkMessages2025.NOT_PREPARED_YET}{'%%%FOO%%%' if LTA else ''}''', print_color='green', mode_verbose=0)
                continue

        if len(pk_sys_argv) == 2:
            nx_by_user_input = pk_sys_argv[1]
            if str.isdigit(nx_by_user_input):
                if LTA:
                    pk_print(f'''인자가 숫자 입니다. {'%%%FOO%%%' if LTA else ''}''')
                idx_by_user_input = int(pk_sys_argv[1])
                d_idx = d_working_with_idx_dict[idx_by_user_input]
                nx_idx = get_nx(d_working_with_idx_dict[idx_by_user_input])
                cmd = f'cd {d_idx}"'
                os.chdir(d_idx)
                # pk_copy(str_working=d_idx)
                if LTA:
                    pk_print(f'{pk_cmd_n} {pk_sys_argv[1]} {get_nx(d_idx)}')
                    pk_print(f'''{STAMP_TRY_GUIDE} {cmd} {'%%%FOO%%%' if LTA else ''}''')
                save_d_to_f(d=d_idx, f=f_cd_txt)
                if LTA:
                    f_cd_txt_list = get_list_from_f(f=f_cd_txt)
                    pk_print(f'''f_cd_txt_list={f_cd_txt_list} {'%%%FOO%%%' if LTA else ''}''')
                pk_cd(sys_argv=sys.argv)
                continue
            else:
                if LTA:
                    pk_print(f'''인자가 숫자가 아닙니다. {'%%%FOO%%%' if LTA else ''}''')
                continue

        elif len(sys.argv) < 2:
            if LTA:
                pk_print(f'인자가 {len(pk_sys_argv)}개 입력되었습니다 {'%%%FOO%%%' if LTA else ''}')

        break
