from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_modules_saved_from_file(f_working, func_n):
    from sources.functions.get_modules_from_file import get_modules_from_file
    from pathlib import Path
    from sources.functions.ensure_pnx_made import ensure_pnx_made
    from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
    import logging
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.pk_map_texts import PkTexts
    import os

    save_file = os.path.join(D_TASK_ORCHESTRATOR_CLI_SENSITIVE, f"modules_collected.txt")
    ensure_pnx_made(pnx=save_file, mode="f")

    f_working = Path(f_working)
    modules = get_modules_from_file(f_working)
    
    if modules:  # 빈 리스트 체크로 성능 향상
        logging.debug(f'''{len(modules)}개 모듈 수집: {f_working} {'%%%FOO%%%' if LTA else ''}''')
        # 각 파일마다 append 하지 말고 리턴만 - 전체 중복제거는 ensure_modules_printed에서
        return modules, save_file
    
    return [], save_file
