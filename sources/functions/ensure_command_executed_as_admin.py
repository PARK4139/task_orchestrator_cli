def ensure_command_executed_as_admin(cmd):
    import textwrap

    from objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES
    from sources.objects.encodings import Encoding

    import platform
    import importlib

    import os
    if platform.system() == 'Windows':
        subprocess = importlib.import_module("subprocess")

        os.system(rf'chcp 65001')

        file = rf"{D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES}\elevate_cmd.cmd"
        # pk_* : 배치파일 생성
        script = textwrap.dedent(rf'''
                @echo off
                echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\ElevateScript.vbs"
                echo UAC.ShellExecute "cmd.exe", "/c ""%~1""", "", "runas", 1 >> "%temp%\ElevateScript.vbs"
                cscript //nologo "%temp%\ElevateScript.vbs"
                del "%temp%\ElevateScript.vbs"
                ''').lstrip()
        with open(file, 'w', encoding='utf-8') as f:
            f.write(script)

        # 배치파일 실행
        admin_cmd = f'cmd.exe /c {file} "{cmd}"'
        result = subprocess.run(admin_cmd, shell=True, encoding=Encoding.UTF8.value, errors="replace", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode, result.stdout, result.stderr
