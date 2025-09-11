from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_fzf_prompt_text():
    from sources.functions.get_project_name import get_project_name
    from sources.functions.get_task_orchestrator_cli_version import get_task_orchestrator_cli_version
    from sources.functions.get_project_info_from_pyproject import get_project_info_from_pyproject
    from sources.objects.pk_map_texts import PkTexts
    prompt_text = None
    project_info = get_project_info_from_pyproject()
    if project_info:
        project_name = get_project_name(project_info)
        project_version = get_task_orchestrator_cli_version(project_info)
        prompt_text = f"{project_name} v{project_version[:12]}> "
    else:
        prompt_text = f"{PkTexts.COMMANDS}> "
    return prompt_text
