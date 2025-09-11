from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_task_orchestrator_cli_version(project_info=None):
    """
    Retrieves the project version from the installed package metadata.
    Falls back to reading from pyproject.toml if the package is not found.
    """
    import importlib.metadata
    try:
        return importlib.metadata.version('task_orchestrator_cli')
    except importlib.metadata.PackageNotFoundError:
        from sources.functions.get_project_info_from_pyproject import get_project_info_from_pyproject
        project_info = project_info or get_project_info_from_pyproject()
        return project_info.get("version", "unknown")
