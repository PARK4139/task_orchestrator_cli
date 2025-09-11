from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
from sources.functions.ensure_value_completed import ensure_value_completed


def assist_to_ensure_files_organized_by_x():
    import os

    while 1:
        d_working = ensure_value_completed(key_hint='d_working=', options=[os.getcwd(), D_PK_WORKING, D_TASK_ORCHESTRATOR_CLI, D_DOWNLOADS])
        # ext_set = {".webm"}
        ext_set = get_extensions_from_d(d_working)
        for ext in ext_set:
            d_dst_n = f"f_organized_by_{ext}".replace('.', "")  # [OPTION]
            d_dst = os.path.join(d_working, d_dst_n)
            pk_oraganize_f_list_to_d_by_x(d_working=d_working, ext=ext, d_dst=d_dst)
