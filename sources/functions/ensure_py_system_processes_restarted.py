

def ensure_py_system_processes_restarted(task_orchestrator_cli_python_files):
    from sources.functions import ensure_slept
    from sources.functions.ensure_process_killed import ensure_process_killed
    from sources.functions.ensure_py_system_process_ran_by_pnx import ensure_py_system_process_ran_by_pnx
    from sources.functions.get_nx import get_nx
    for file_to_execute in task_orchestrator_cli_python_files:
        ensure_process_killed(window_title_seg=get_nx(file_to_execute))
    ensure_slept(milliseconds=80)
    for file_to_execute in task_orchestrator_cli_python_files:
        ensure_py_system_process_ran_by_pnx(file_to_execute=file_to_execute)
