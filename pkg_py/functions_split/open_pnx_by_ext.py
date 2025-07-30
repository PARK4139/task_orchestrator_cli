from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.system_object.files import F_PYCHARM64_EDITION_EXE
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025

from functools import lru_cache

# @lru_cache(maxsize=1)
def ensure_pnx_opened_by_ext(pnx):
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_os_n import get_os_n
    from pkg_py.functions_split.get_value_completed import get_value_completed

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
                'log': ('explorer.exe', 'text file, opening in windows explorer'),

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
                'py': (get_pnx_windows_style(F_PYCHARM64_EDITION_EXE), 'python file, opening in windows explorer'),
            }
        program, description = ext_to_program.get(x, (None, None))
        if program:
            text_editor = program
            pnx = get_pnx_windows_style(pnx=pnx)
            ensure_printed(f"ensure_pnx_opened_by_ext: {pnx} is a {description}", print_color='blue')
        
        # text_editor가 None이면 사용자 입력 받기
        if text_editor is None:
            ensure_printed(f"확장자 '{x}'에 대한 기본 프로그램이 설정되지 않았습니다.", print_color='yellow')
            
            # 사용자에게 프로그램 선택 옵션 제공
            program_options = [
                "explorer.exe (Windows 탐색기에서 열기)",
                "notepad.exe (메모장에서 열기)",
                "code (VS Code에서 열기)",
                "pycharm64.exe (PyCharm에서 열기)",
                "python.exe (Python으로 실행)",
                "사용자 정의 프로그램 입력"
            ]
            # selected_option = get_value_completed("프로그램을 선택하세요: ", program_options) # pk_option
            selected_option = "explorer.exe (Windows 탐색기에서 열기)"
            
            if selected_option is None:
                ensure_printed("프로그램 선택이 취소되었습니다.", print_color='yellow')
                return
            
            if selected_option == "explorer.exe (Windows 탐색기에서 열기)":
                text_editor = "explorer.exe"
            elif selected_option == "notepad.exe (메모장에서 열기)":
                text_editor = "notepad.exe"
            elif selected_option == "code (VS Code에서 열기)":
                text_editor = "code"
            elif selected_option == "pycharm64.exe (PyCharm에서 열기)":
                text_editor = get_pnx_windows_style(F_PYCHARM64_EDITION_EXE)
            elif selected_option == "python.exe (Python으로 실행)":
                text_editor = "python.exe"
            elif selected_option == "사용자 정의 프로그램 입력":
                custom_program = input("프로그램 경로나 명령어를 입력하세요: ").strip()
                if custom_program:
                    text_editor = custom_program
                else:
                    ensure_printed("프로그램이 입력되지 않았습니다.", print_color='red')
                    return
        
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
