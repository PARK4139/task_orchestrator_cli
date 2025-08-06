from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_fzf_prompt_text():
    from pkg_py.functions_split.get_project_info_from_pyproject import get_project_info_from_pyproject
    from pkg_py.system_object.map_massages import PkMessages2025
    prompt_text = None
    project_info = get_project_info_from_pyproject()
    if project_info:
        project_name = project_info.get("name", "unknown")
        project_version = project_info.get("version", "unknown")
        prompt_text = f"{project_name} v{project_version}> "
    else:
        prompt_text = f"{PkMessages2025.COMMANDS}> "
    return prompt_text