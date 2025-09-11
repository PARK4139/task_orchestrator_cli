from sources.objects.task_orchestrator_cli_directories import D_PK_RECYCLE_BIN

MAX_DUPLICATE_ATTEMPTS = 100  # 중복 파일명을 허용하는 최대 시도 횟수

def ensure_files_gathered():
    from sources.functions.does_pnx_exist import is_pnx_existing
    from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
    from sources.functions.get_historical_list import get_historical_list
    from sources.functions.get_list_sorted import get_list_sorted
    from pathlib import Path
    from sources.functions.ensure_value_completed import ensure_value_completed
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_DOWNLOADS, D_PK_WORKING
    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.pk_map_texts import PkTexts

    import inspect
    from sources.functions.get_file_id import get_file_id
    from sources.functions.get_list_calculated import get_list_calculated
    import logging
    import os
    import shutil
    import datetime

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    key_name = "d_working"
    file_to_working = rf"{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/{get_file_id(key_name, func_n)}.history"
    file_to_working = Path(file_to_working)
    historical_pnxs = get_historical_list(f=file_to_working)
    options = historical_pnxs + get_list_sorted(working_list=[D_PK_WORKING, D_DOWNLOADS], mode_asc=1)
    if LTA:
        # d_working = rf"G:\Downloads\pk_test2"
        # d_working = rf"G:\Downloads\pk_test"
        d_working = ensure_value_completed(key_hint='d_working=', options=options)
    else:
        d_working = ensure_value_completed(key_hint='d_working=', options=options)
    d_working = Path(d_working)

    logging.debug(f'''len(historical_pnxs)={len(historical_pnxs)} {'%%%FOO%%%' if LTA else ''}''')
    logging.debug(f'''len(options)={len(options)} {'%%%FOO%%%' if LTA else ''}''')

    values_to_save = [v for v in [d_working] + historical_pnxs + options if is_pnx_existing(pnx=v)]
    values_to_save = get_list_calculated(origin_list=values_to_save, dedup=True)
    ensure_list_written_to_f(f=file_to_working, working_list=values_to_save, mode="w")

    if not os.path.exists(d_working):
        print(f"[ERROR] d_working 경로가 존재하지 않습니다: {d_working}")
        return

    # 1. 하위 모든 파일 수집
    all_files = []
    for root, _, files in os.walk(d_working):
        for f in files:
            full_path = os.path.join(root, f)
            if os.path.isfile(full_path):
                all_files.append(full_path)

    # 2. 파일 이동 (중복 처리 포함, 상수 사용)
    for file_path in all_files:
        filename = os.path.basename(file_path)
        base, ext = os.path.splitext(filename)
        dst_path = os.path.join(d_working, filename)

        attempt = 0

        while attempt < MAX_DUPLICATE_ATTEMPTS:
            if os.path.abspath(file_path) == os.path.abspath(dst_path):
                break  # 같은 위치면 skip

            if not os.path.exists(dst_path):
                try:
                    # os.chmod(file_path, 0o666)  # 읽기 전용 해제 시도
                    shutil.move(file_path, dst_path)
                    break
                except PermissionError:
                    print(f"[PERMISSION ERROR] 파일 이동 실패 (열려있을 수 있음): {file_path}")
                    break
                except Exception as e:
                    print(f"[ERROR] 파일 이동 실패: {file_path} → {dst_path} | {e}")
                    break
            else:
                now = datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S")
                new_filename = f"{base}_DUPLICATED_{now}_{attempt}{ext}"
                dst_path = os.path.join(d_working, new_filename)
                attempt += 1

    # 3. 하위 디렉토리 중 빈 디렉토리만 재귀적으로 제거
    for root, dirs, _ in os.walk(d_working, topdown=False):
        for dir_name in dirs:
            full_dir = os.path.join(root, dir_name)
            try:
                if not any(entry for entry in os.scandir(full_dir) if not entry.name.startswith('.')):
                    rel_path = os.path.relpath(full_dir, start=d_working)
                    new_dir_path = os.path.join(D_PK_RECYCLE_BIN, rel_path)

                    if os.path.exists(new_dir_path):
                        base = os.path.basename(rel_path)
                        now = datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S")
                        new_dir_path = os.path.join(D_PK_RECYCLE_BIN, f"{base}_DUPLICATED_{now}")

                    os.makedirs(os.path.dirname(new_dir_path), exist_ok=True)
                    shutil.move(full_dir, new_dir_path)
                    print(f"[INFO] 빈 디렉토리 이동됨: {full_dir} → {new_dir_path}")
            except Exception as e:
                print(f"[ERROR] 디렉토리 확인 중 오류 발생: {full_dir} - {e}")

    print(f"[INFO] 모든 파일은 d_working 최상위로 이동 완료: {d_working}")
    print(f"[INFO] 비어 있는 디렉토리는 {D_PK_RECYCLE_BIN} 으로 이동 완료")
