from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
from pkg_py.system_object.ttl_cache_manager import ensure_function_ttl_cached


@ensure_seconds_measured
# @ensure_function_ttl_cached(ttl_seconds=300, maxsize=16)  # 5분 캐시 활성화, not LTA 모드에서 활성화
def get_excutable_pk_system_processes():
    import os
    from glob import glob

    from pkg_py.system_object.directories import D_PKG_PY
    result = sorted(
        f for f in glob(os.path.join(D_PKG_PY, "pk_*.py"))
        if not os.path.basename(f).startswith("pk_system_layer")
    )
    return result