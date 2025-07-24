

from pkg_py.system_object.directories import D_PKG_PY


def get_excutable_pk_system_file_list():
    # pk_*.py 파일 절대경로 리스트
    import os
    from glob import glob
    # return sorted(glob(os.path.join(D_PKG_PY, "pk_*.py")))
    result = sorted(
        f for f in glob(os.path.join(D_PKG_PY, "pk_*.py"))
        if not os.path.basename(f).startswith("pk_system_layer")
    )
    return result
