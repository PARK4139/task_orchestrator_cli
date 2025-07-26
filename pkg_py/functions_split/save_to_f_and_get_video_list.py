from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list


def save_to_f_and_get_video_list(f, d_working, ext_allowed_list, video_ignored_keyword_list):
    ensure_printed(f'''f={f} {'%%%FOO%%%' if LTA else ''}''')
    if not does_pnx_exist(pnx=f):
        ensure_pnx_made(pnx=f, mode='f')
    v_f_list = get_video_filtered_list(d_working, ext_allowed_list, video_ignored_keyword_list)
    ensure_list_written_to_f(v_f_list, f, mode='w')
    return v_f_list
