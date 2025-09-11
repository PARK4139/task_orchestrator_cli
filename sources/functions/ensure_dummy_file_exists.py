from sources.objects.pk_map_texts import PkTexts

from sources.functions.ensure_pnx_made import ensure_pnx_made
from sources.functions.get_x import get_x
from pathlib import Path
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.get_p import get_p
from sources.functions.ensure_func_info_saved import ensure_func_info_saved


def ensure_dummy_file_exists(file_pnx):
    import inspect
    file_pnx = Path(file_pnx)
    ensure_pnx_made(get_p(file_pnx), mode="d")
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    if not is_pnx_existing(file_pnx):
        x = get_x(file_pnx)
        with open(file_pnx, 'wb') as f:
            f.write(b'\x00')  # 1바이트 더미
        func_data = {
            "n": func_n,
            "state": PkTexts.SUCCEEDED,
            "file_pnx": file_pnx,
        }
        ensure_func_info_saved(func_n, func_data)
        # return func_data
        # 이제 return 안하고 db 에서 가져와도 됨.
