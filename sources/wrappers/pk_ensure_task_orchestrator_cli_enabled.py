

if __name__ == "__main__":
    from sources.functions.ensure_task_orchestrator_cli_log_initialized import ensure_task_orchestrator_cli_log_initialized
    from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
    from sources.functions.ensure_task_orchestrator_cli_enabled import ensure_task_orchestrator_cli_enabled
    import traceback
    from sources.functions.ensure_window_title_replaced import ensure_window_title_replaced
    from sources.functions.ensure_task_orchestrator_cli_wrapper_window_title_replaced import ensure_task_orchestrator_cli_wrapper_window_title_replaced

    from sources.functions.get_nx import get_nx
    from sources.functions.ensure_exception_routine_done import ensure_exception_routine_done
    from sources.functions.ensure_finally_routine_done import ensure_finally_routine_done
    from sources.functions.ensure_task_orchestrator_cli_colorama_initialized_once import ensure_task_orchestrator_cli_colorama_initialized_once
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI

    try:
        ensure_task_orchestrator_cli_wrapper_suicided(__file__)
        ensure_task_orchestrator_cli_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))
        ensure_task_orchestrator_cli_log_initialized(__file__)

        ensure_task_orchestrator_cli_enabled()
    except Exception as exception:
        ensure_exception_routine_done(__file__=__file__,traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done( __file__=__file__,D_TASK_ORCHESTRATOR_CLI=D_TASK_ORCHESTRATOR_CLI)
