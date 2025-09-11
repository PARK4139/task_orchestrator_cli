from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING, D_DOWNLOADS
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.functions.ensure_value_completed import ensure_value_completed
import logging


def ensure_files_organized_by_keyword_and_x():
    import os

    try:
        while 1:
            d_working = ensure_value_completed(key_hint='d_working=',
                                               options=[os.getcwd(), D_PK_WORKING, D_TASK_ORCHESTRATOR_CLI, D_DOWNLOADS])
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
                                ensure_pnx_moved(pnx=pnx, d_dst=d_new)
                                logging.debug(f"f 이동 {f_nx} → {f_new}")
                    if x_extracted in x_to_organize_list:
                        d_new = os.path.join(d_working, x_extracted.replace(".", ""))
                        os.makedirs(d_new, exist_ok=True)
                        f_new = get_pnx_new(d_working=d_new, pnx=pnx)
                        if not os.path.exists(f_new):
                            ensure_pnx_moved(pnx=pnx, d_dst=d_new)
                            logging.debug(f"f 이동 {f_nx} → {f_new}")
    except KeyboardInterrupt:
        logging.debug(" 모니터링 중지됨.")
