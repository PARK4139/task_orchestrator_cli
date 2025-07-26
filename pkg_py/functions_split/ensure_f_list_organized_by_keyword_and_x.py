from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_f_list_organized_by_keyword_and_x():
    import os

    try:
        while 1:
            d_working = get_value_completed(key_hint='d_working=',
                                            values=[os.getcwd(), D_PK_WORKING, D_PROJECT, D_DOWNLOADS])
            keyword_to_organize_list = get_values_completed(key_hint='keyword_to_organize_list=',
                                                            values=[['seg', 'SEG']])
            x_to_organize_list = get_values_completed(key_hint='x_to_organize_list=', values=[['mp4', 'mkv', 'avi'],
                                                                                              ['.jpg', '.jpeg', '.png',
                                                                                               '.webp', '.jfif']])
            if ensure_d_size_stable(d_working, limit_seconds=5):
                pnx_nx_list = os.listdir(d_working)  # _d_ 목록 가져오기
                for pnx_nx in pnx_nx_list:
                    pnx = os.path.join(d_working, pnx_nx)
                    if not os.path.isfile(pnx):
                        continue  # _d_는 무시
                    f_nx = pnx_nx
                    x_extracted = get_x(pnx).lower()  # 확장자 캐싱
                    for keyword in keyword_to_organize_list:
                        if keyword in f_nx:
                            d_new = os.path.join(d_working, keyword.lower())
                            os.makedirs(d_new, exist_ok=True)
                            f_new = get_pnx_new(d_working=d_new, pnx=pnx)
                            if not os.path.exists(f_new):
                                move_pnx(pnx=pnx, d_dst=d_new)
                                ensure_printed(f"f 이동 {f_nx} → {f_new}", print_color='green')
                    if x_extracted in x_to_organize_list:
                        d_new = os.path.join(d_working, x_extracted.replace(".", ""))
                        os.makedirs(d_new, exist_ok=True)
                        f_new = get_pnx_new(d_working=d_new, pnx=pnx)
                        if not os.path.exists(f_new):
                            move_pnx(pnx=pnx, d_dst=d_new)
                            ensure_printed(f"f 이동 {f_nx} → {f_new}", print_color='green')
    except KeyboardInterrupt:
        ensure_printed("\n 모니터링 중지됨.")
