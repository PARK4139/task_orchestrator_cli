from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
from pkg_py.system_object.ttl_cache_manager import ensure_function_ttl_cached


@ensure_seconds_measured
@ensure_function_ttl_cached(ttl_seconds=60, maxsize=64) # pk_*
def get_fzf_command():
    import subprocess

    for name in ["fzf", "fzf.exe"]:
        try:
            subprocess.run([name, "--version"], capture_output=True, check=True)
            return name
        except Exception:
            continue
    return None
