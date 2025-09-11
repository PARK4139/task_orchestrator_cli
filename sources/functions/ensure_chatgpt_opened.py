from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.functions.ensure_target_enabled import ensure_target_enabled


@ensure_seconds_measured
def ensure_chatgpt_opened():
    from sources.functions.ensure_window_to_front import ensure_window_to_front
    from sources.functions.get_execute_cmd_with_brakets import get_cmd_chains
    from sources.functions.get_nx import get_nx
    from sources.functions.is_window_opened import is_window_opened
    from sources.objects.task_orchestrator_cli_urls import URL_CHATGPT_PK_WORKING
    from sources.functions.ensure_command_executed import ensure_command_executed

    # ensure_target_enabled("explorer.exe", URL_CHATGPT_PK_WORKING)
    ensure_command_executed( get_cmd_chains("explorer.exe", URL_CHATGPT_PK_WORKING))


    # TODO : naver,  google, nyasii  URL tab 으로  고를때는 nickname,   맵으로 나오도록
    # 아침코딩이 오히려 즐겁다.
    # gtts 내가 고치자.
