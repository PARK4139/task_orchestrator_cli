from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed


def pk_assist_to_ensure_f_list_organized_by_x():
    import os

    while 1:
        d_working = get_value_completed(key_hint='d_working=', values=[os.getcwd(), D_WORKING, D_PROJECT, D_DOWNLOADS])
        # ext_set = {".webm"}
        ext_set = get_extension_set_from_d(d_working)
        for ext in ext_set:
            d_dst_n = f"f_organized_by_{ext}".replace('.', "")  # [OPTION]
            d_dst = os.path.join(d_working, d_dst_n)
            pk_oraganize_f_list_to_d_by_x(d_working=d_working, ext=ext, d_dst=d_dst)
