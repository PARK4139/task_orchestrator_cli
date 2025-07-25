import inspect

from pygments.unistring import No

from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_pnx_list_from_d_working import get_pnxs_from_d_working
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_value_via_fzf_or_history_routine import get_value_via_fzf_or_history_routine
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
from pkg_py.functions_split.print import pk_print
from pkg_py.system_object.directories import D_PKG_PY, D_PKG_TXT
from pkg_py.system_object.files import F_PK_WORKSPACE_PY
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025


def ensure_modules_saved_from_file(f_working):
    import inspect
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
    from pkg_py.functions_split.write_list_to_f import ensure_list_written_to_f
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    import os

    func_n = inspect.currentframe().f_code.co_name
    save_file = os.path.join(D_PKG_TXT, f"{func_n}.txt")
    ensure_pnx_made(pnx=save_file, mode="f")

    save_file = get_pnx_os_style(save_file)
    f_working = get_pnx_os_style(f_working)

    modules = get_modules_from_file(f_working)
    modules_deduped = sorted(set(modules))

    ensure_list_written_to_f(modules_deduped, save_file, mode="a")
    print(f"modules: {modules}")
    return save_file


def get_modules_from_file(f_working):
    from pkg_py.functions_split.get_list_from_f import get_list_from_f

    modules = set()
    lines = get_list_from_f(f=f_working)
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        if line.startswith("import "):
            # 예: "import os, sys" 도 처리 가능하게
            imports = line.replace("import", "").strip().split(",")
            for imp in imports:
                modules.add(imp.strip().split(" ")[0])  # "as" 제거
        elif line.startswith("from "):
            # 예: "from os import path"
            parts = line.split()
            if len(parts) >= 2:
                modules.add(parts[1].strip())  # os
    return sorted(modules)



def ensure_modules_saved():
    if LTA:
        decision = "d_working_mode"
        # decision = "f_working_mode"
    else:
        decision = get_value_completed(key_hint=rf"{PkMessages2025.MODE}=", values=["f_working_mode", "d_working_mode"])
    if decision == "d_working_mode":
        save_file = None
        pnxs = get_pnxs_from_d_working(d_working=D_PKG_PY)
        for pnx in pnxs:
            if is_f(pnx):
                pk_print(f'''[{PkMessages2025.DATA}] pnx={pnx} {'%%%FOO%%%' if LTA else ''}''')
                save_file = ensure_modules_saved_from_file(f_working=pnx)
                ensure_filelines_deduplicated(f_working=pnx)
        ensure_pnx_opened_by_ext(save_file)
    elif decision == "f_working_mode":
        key_name = 'f_working'
        func_n = inspect.currentframe().f_code.co_name
        file_id = get_file_id(key_name, func_n)
        editable = False
        # editable = True
        init_options = [F_PK_WORKSPACE_PY]
        value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
        f_working = value
        ensure_modules_saved_from_file(f_working=f_working)
