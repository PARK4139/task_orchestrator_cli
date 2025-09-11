def print_highlighted(txt_whole, highlight_config_dict):
    from sources.functions.ensure_task_orchestrator_cli_colorama_initialized_once import ensure_task_orchestrator_cli_colorama_initialized_once
    from sources.functions.get_txt_highlighted import get_txt_highlighted
    ensure_task_orchestrator_cli_colorama_initialized_once()
    print(get_txt_highlighted(txt_whole, highlight_config_dict))
