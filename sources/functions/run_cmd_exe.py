def ensure_cmd_exe_executed():
    from sources.functions.ensure_command_executed import ensure_command_executed
    ensure_command_executed(cmd=rf"start /MAX "" cmd.exe /k", mode="a")
