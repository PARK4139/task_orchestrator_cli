import undetected_chromedriver as uc
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from Cryptodome.Random import get_random_bytes
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist


def ensure_unique(dst_dir, name):
    """
    dst_dir에 name과 같은 파일이 이미 있으면
    (1), (2), ... suffix를 붙여 고유명으로 반환
    """
    import os

    base, ext = os.path.splitext(name)
    candidate = name
    n = 1
    while os.path.exists(os.path.join(dst_dir, candidate)):
        candidate = f"{base}({n}){ext}"
        n += 1
    return candidate
