def ensure_bit_torrent_exe_opened():
    from sources.objects.task_orchestrator_cli_files import F_BIT_TORRENT_EXE

    from sources.functions.ensure_command_executed import ensure_command_executed
    ensure_command_executed(cmd=fr"explorer.exe {F_BIT_TORRENT_EXE}")
