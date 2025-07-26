

def ensure_command_excuted_to_os_like_person_as_admin(cmd):
    import platform
    import subprocess
    import traceback
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA

    # todo : refactor : need refactorying
    # 검증도 필요. like_pserson 으로 동작 하지 않는다.
    if not platform.system() == 'Windows':
        cmd = cmd.replace("\\", "/")
    try:
        if platform.system() == 'Windows':
            # lines=subprocess.check_output('chcp 65001 >nul', shell=True).decode('utf-8').split('\n')
            # lines=subprocess.check_output(cmd, shell=True).decode('euc-kr').split('\n')
            lines = subprocess.check_output(cmd, shell=True).decode('utf-8').split('\n')
        return lines
    except:
        ensure_printed(str_working=rf'''traceback.format_exc()="{traceback.format_exc()}"  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        # os.system(cmd)
    return None
