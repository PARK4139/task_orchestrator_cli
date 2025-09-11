from objects.pk_ttl_cache_manager import ensure_function_return_ttl_cached
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_function_return_ttl_cached(ttl_seconds=5, maxsize=10)
@ensure_seconds_measured
def get_project_name(project_info=None):
    from sources.functions.get_project_info_from_pyproject import get_project_info_from_pyproject
    if project_info is None:
        project_info = get_project_info_from_pyproject()
    project_name = project_info.get("name", "unknown")
    return project_name
