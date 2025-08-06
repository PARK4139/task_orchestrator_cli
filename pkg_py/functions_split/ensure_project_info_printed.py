from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_project_info_printed():
    import sys
    from pkg_py.functions_split import ensure_console_cleared
    from pkg_py.system_object.color_map import ANSI_COLOR_MAP
    from pkg_py.system_object.etc import PK_UNDERLINE
    from pkg_py.functions_split.get_project_info_from_pyproject import get_project_info_from_pyproject

    ensure_console_cleared()
    project_info = get_project_info_from_pyproject()

    print(f"""{(
        f"{ANSI_COLOR_MAP["BRIGHT_MAGENTA"]}{PK_UNDERLINE}\n"
        f"Project Information\n"
        f"Project Python version: {sys.version}\n"
        f"Project version: {__import__('pkg_py').__version__}\n"
        f"Project Name: {project_info.get('name', 'N/A')}\n"
        f"Project Version: {project_info.get('version', 'N/A')}\n"
        f"Project Description: {project_info.get('description', 'N/A')}\n"
        f"Project Author(s): {project_info['authors']}"
        if project_info and isinstance(project_info, dict) else
        f"Failed to load {ANSI_COLOR_MAP["RED"]}pyproject.toml{ANSI_COLOR_MAP["RESET"]} or cache issue occurred.\n"
        f"{ANSI_COLOR_MAP["BRIGHT_MAGENTA"]}Debug Info: project_info = {project_info}, type = {type(project_info)}"
    )}{ANSI_COLOR_MAP["RESET"]}""")
