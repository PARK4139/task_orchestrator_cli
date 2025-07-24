from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list


def save_to_f_and_get_video_list(f, d_working, ext_allowed_list, video_ignored_keyword_list):
    pk_print(f'''f={f} {'%%%FOO%%%' if LTA else ''}''')
    if not does_pnx_exist(pnx=f):
        ensure_pnx_made(pnx=f, mode='f')
    v_f_list = get_video_filtered_list(d_working, ext_allowed_list, video_ignored_keyword_list)
    write_list_to_f(v_f_list, f, mode='w')
    return v_f_list
