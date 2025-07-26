from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.system_object.files import F_PYCHARM64_EDITION_2025_01_03_EXE
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025

from functools import lru_cache

@lru_cache(maxsize=1)
def ensure_pnx_opened_by_ext(pnx):
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_os_n import get_os_n

    # TBD : tab 으로 뭘로 열지 설정하도록 ?
    if is_os_windows():
        import os
        # x = get_x(pnx).replace('.', '')
        x = os.path.splitext(pnx)[1].lower().replace('.', '')
        text_editor = None
        ext_to_program = None
        if get_os_n() == 'windows':
            # ext_to_program = get_value_completed(message="ext_to_program=", option_values=['xc', 'nx', 'no'])
            ext_to_program = {
                '': ('explorer.exe', 'directory, opening in windows explorer'),
                'txt': ('explorer.exe', 'text file, opening in windows explorer'),
                'csv': ('explorer.exe', 'csv file, opening in excel'),
                'xlsx': ('explorer.exe', 'excel file, opening in excel'),
                'xlsm': ('explorer.exe', 'excel file, opening in excel'),
                'xls': ('explorer.exe', 'excel file, opening in excel'),

                # Video files
                'mp4': ('explorer.exe', 'video file, opening in default player'),
                'avi': ('explorer.exe', 'video file, opening in default player'),
                'mkv': ('explorer.exe', 'video file, opening in default player'),
                'mov': ('explorer.exe', 'video file, opening in default player'),
                'wmv': ('explorer.exe', 'video file, opening in default player'),
                'flv': ('explorer.exe', 'video file, opening in default player'),
                'webm': ('explorer.exe', 'video file, opening in default player'),

                'history': ('explorer.exe', 'pk history file, opening in windows explorer'),

                # 'py': ('explorer.exe', 'python file, opening in windows explorer'),
                # 'py': ('python.exe', 'python file, opening in windows explorer'),
                'py': (get_pnx_windows_style(F_PYCHARM64_EDITION_2025_01_03_EXE), 'python file, opening in windows explorer'),
            }
        program, description = ext_to_program.get(x, (None, None))
        if program:
            text_editor = program
            pnx = get_pnx_windows_style(pnx=pnx)
            ensure_printed(f"ensure_pnx_opened_by_ext: {pnx} is a {description}", print_color='blue')
        # cmd = f' "{text_editor}" "{pnx}" '
        cmd = f'"{text_editor}" "{pnx}"'
        ensure_command_excuted_to_os(cmd=cmd, mode='a')
    else:
        ensure_printed(f'''{PkMessages2025.NOT_PREPARED_YET}{'%%%FOO%%%' if LTA else ''}''', print_color='green', mode_verbose=0)
        # if x == '':  # d 인 경우
        #     text_editor = 'explorer.exe'
        # elif x == 'txt':
        #     text_editor = 'gedit' # nvim, nano, vim, code
        # # elif x == 'csv':
        # #     text_editor = 'explorer.exe'
        # # elif x == 'xlsx':
        # #     text_editor = 'explorer.exe'
        # # elif x == 'xls':
        # #     text_editor = 'explorer.exe'
        # pnx = get_pnx_unix_style(pnx=pnx)
