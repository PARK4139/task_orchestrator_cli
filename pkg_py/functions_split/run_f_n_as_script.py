from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.encodings import Encoding
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style


def run_f_n_as_script():  # todo : chore : add parameter

    f_p = rf'{D_PKG_PY}'
    f_n = 'pk_save_chrome_youtube_cookies_to_f'
    f_pn_py = get_pnx_os_style(pnx=rf"{f_p}/{f_n}.py")
    f_pn_cmd = rf"{D_PKG_WINDOWS}\{f_n}.cmd"
    activate_bat = rf'{D_PROJECT}\.venv\Scripts\activate.cmd'
    python_exe = rf'{D_PROJECT}\.venv\Scripts\python.exe'
    CRLF = '%%%CRLF%%%'
    script_str = rf'''
       :: @echo off{CRLF}
       chcp 65001 >nul{CRLF}
       title %~nx0{CRLF}   
       cls{CRLF}

       :: 관리자 권한 요청{CRLF}
       :: net session >nul 2>&1{CRLF}
       :: if %errorLevel% neq 0 ({CRLF}
       ::     powershell -Command "Start-Process python -ArgumentList '\"%~dp0myscript.py\"' -Verb RunAs"{CRLF}
       ::     exit /b{CRLF}
       :: ){CRLF}
       :: cls{CRLF}

       call "{activate_bat}"{CRLF}
       set PYTHONPATH={D_PROJECT}{CRLF}
       "{python_exe}" "{f_pn_py}"{CRLF}
     '''
    script_list = script_str.split(CRLF)
    script_list = get_list_replaced_element_from_str_to_str(working_list=script_list, from_str='    ', to_str='')
    ensure_pnx_made(pnx=f_pn_cmd, mode='f', script_list=script_list)
    ensure_printed(rf"set PYTHONPATH={D_PROJECT}", print_color='blue')
    # ensure_command_excuted_to_os(cmd=rf'notepad "{activate_bat}"')
    # ensure_command_excuted_to_os(cmd=rf'notepad "{f_pn_cmd}"')
    ensure_command_excuted_to_os(cmd=rf'start call "{f_pn_cmd}" ', encoding=Encoding.UTF8, mode='a')
