from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.functions_split.ensure_process_killed_by_window_title_seg import ensure_process_killed_by_window_title_seg
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pk_system_process_nxs import get_pk_system_process_nxs
from pkg_py.system_object.local_test_activate import LTA



def ensure_pk_system_processes_killed():


    get_pk_system_processes_and_idx = get_pk_system_process_nxs()
    for idx, get_pk_system_process_pnx in enumerate(get_pk_system_processes_and_idx):
        ensure_process_killed_by_window_title_seg(window_title_seg=get_nx(get_pk_system_process_pnx[int(idx)]))
    if not LTA:
        ensure_pk_program_suicided(self_f=get_nx(__file__))
