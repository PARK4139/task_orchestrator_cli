def ensure_command_executed_like_human_as_admin(cmd):
    import logging
    import logging

    from sources.functions.is_os_windows import is_os_windows
    import subprocess
    import traceback
    from sources.objects.pk_local_test_activate import LTA

    # todo : refactor : need refactorying
    # 검증도 필요. like_pserson 으로 동작 하지 않는다.
    try:
        if is_os_windows():
            lines = subprocess.check_output(cmd, shell=True).decode('utf-8').split('\n')
        return lines
    except:
        logging.debug(rf'''traceback.format_exc()="{traceback.format_exc()}"  {'%%%FOO%%%' if LTA else ''}''')
    return None
