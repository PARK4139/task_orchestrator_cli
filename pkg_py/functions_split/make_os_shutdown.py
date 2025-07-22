

def ensure_os_shutdown(seconds=None, milliseconds=None, mins=None, restart_mode=0, cancel_mode=0):
    from pkg_py.functions_split.cmd_to_os import cmd_to_os
    from pkg_py.functions_split.pk_print import pk_print
    mode_list = [restart_mode, cancel_mode]
    false_count = mode_list.count(False)

    none_list = [seconds, milliseconds, mins]
    none_count = none_list.count(None)

    if false_count == 2 and none_count == 3:
        pk_print(f"이 함수의 최소인자의 수는 1개 입니다")
        return

    if false_count < 2:
        if restart_mode == 1:
            cmd = f'shutdown.exe /r'
            cmd_to_os(cmd=cmd)
            return

        if cancel_mode == 1:
            cmd = f'shutdown.exe /a'
            cmd_to_os(cmd=cmd)
            return
    else:

        if none_count != 2:
            pk_print(f"이 함수는 시간단위에 대한인자를 1개의 인자만 받도록 만들어졌습니다")
            return

        # sys_shutdown(seconds=x)
        # sys_shutdown(mins=x)
        if milliseconds is not None:
            seconds = milliseconds
        elif mins is not None:
            seconds = mins * 60

        cmd = f'shutdown.exe /s /t {seconds}'
        cmd_to_os(cmd=cmd)
