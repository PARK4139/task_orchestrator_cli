from sources.objects.pk_local_test_activate import LTA
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
import logging
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.get_video_filtered_list import get_video_filtered_list


def save_to_f_and_get_video_list(f, d_working, ext_allowed_list, video_name_parts_to_ignore):
    logging.debug(f'''f={f} {'%%%FOO%%%' if LTA else ''}''')
    if not is_pnx_existing(pnx=f):
        ensure_pnx_made(pnx=f, mode='f')
    v_f_list = get_video_filtered_list(d_working, ext_allowed_list, video_name_parts_to_ignore)
    ensure_list_written_to_f(v_f_list, f, mode='w')
    return v_f_list
