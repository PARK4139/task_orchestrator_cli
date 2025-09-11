

from sources.objects.encodings import Encoding


def ensure_command_executed_as_admin(cmd):
    """Windows에서 관리자 권한으로 명령 프롬프트 exec  (배치 f 사용)"""
    # todo : fix
    import platform
    import importlib

    import os
    if platform.system() == 'Windows':
        subprocess = importlib.import_module("subprocess")

        os.system(rf'chcp 65001')

        f_cmd = rf"{D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES}\elevate_cmd.cmd"
        CRLF = '%%%CRLF%%%'
        script_str = rf'''
                        @echo off{CRLF}
                        echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\ElevateScript.vbs"{CRLF}
                        echo UAC.ShellExecute "cmd.exe", "/c ""%~1""", "", "runas", 1 >> "%temp%\ElevateScript.vbs"{CRLF}
                        cscript //nologo "%temp%\ElevateScript.vbs"{CRLF}
                        del "%temp%\ElevateScript.vbs"{CRLF}
                        '''
        script_list = script_str.split(CRLF)
        script_list = get_list_replaced_element_from_str_to_str(working_list=script_list, from_str='    ', to_str='')
        ensure_pnx_made(pnx=f_cmd, mode='f', script_list=script_list)
        # ensure_command_executed(cmd=rf"notepad {bat_f}")

        # 관리자 권한 exec
        admin_cmd = f'cmd.exe /c {f_cmd} "{cmd}"'

        result = subprocess.run(admin_cmd, shell=True, encoding=Encoding.UTF8, errors="replace",
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        return result.returncode, result.stdout, result.stderr
