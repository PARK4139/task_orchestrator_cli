from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_excutable_pk_system_processes():
    from pkg_py.system_object.directories import D_PKG_PY
    import os
    from glob import glob
    # return sorted(glob(os.path.join(D_PKG_PY, "pk_*.py")))
    result = sorted(
        f for f in glob(os.path.join(D_PKG_PY, "pk_*.py"))
        if not os.path.basename(f).startswith("pk_system_layer")
    )
    return result
