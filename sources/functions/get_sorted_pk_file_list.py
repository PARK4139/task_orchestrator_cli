from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
# @ensure_function_return_ttl_cached(ttl_seconds=300, maxsize=16)  # 5분 캐시 활성화, not LTA 모드에서 활성화
def get_excutable_wrappers():
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_WRAPPERS
    import os
    from glob import glob

    result = sorted(
        f for f in glob(os.path.join(D_TASK_ORCHESTRATOR_CLI_WRAPPERS, "*.py"))
    )
    return result
