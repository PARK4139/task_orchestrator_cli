from pkg_py.functions_split.pk_measure_seconds import pk_measure_seconds


@pk_measure_seconds
def backup_workspace(D_PKG_ARCHIVED, d_working, func_n):
    import traceback
    from pkg_py.pk_system_object.Local_test_activate import LTA
    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.pk_print import pk_print
    import logging
    import os
    import tarfile
    from datetime import datetime
    from pkg_py.pk_system_object.PkMessages2025 import PkMessages2025
    try:
        # 0. 경로 정규화
        from pathlib import Path
        d_working = Path(d_working).resolve()
        D_PKG_ARCHIVED = Path(D_PKG_ARCHIVED).resolve()

        # 대상 폴더 크기 계산
        def get_dir_size(path):
            total = 0
            for dirpath, dirnames, filenames in os.walk(path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if os.path.isfile(fp):
                        total += os.path.getsize(fp)
            return total

        target_size_mb = get_dir_size(d_working) / (1024 * 1024)
        if target_size_mb > 100:
            pk_print(
                f"[ALERT] 백업 대상 폴더({d_working})의 크기가 100MB를 초과했습니다: {target_size_mb:.2f} MB"
            )
            answer = input("계속 진행하시겠습니까? (y/n): ").strip().lower()
            if answer not in ("y", "yes"):
                pk_print("[INFO] 백업을 중단합니다.")
                return None

        pk_print(f'''[{PkMessages2025.DATA}] d_working={d_working} {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''[{PkMessages2025.DATA}] D_PKG_ARCHIVED={D_PKG_ARCHIVED} {'%%%FOO%%%' if LTA else ''}''')
        os.makedirs(D_PKG_ARCHIVED, exist_ok=True)
        timestamp = datetime.now().strftime('%Y_%m%d_%H%M_%S')
        base_name = os.path.basename(d_working)
        archive_name = f"{base_name}_archived_before_work_{timestamp}_via_{func_n}.tar.bz2"
        archive_path = os.path.join(D_PKG_ARCHIVED, archive_name)
        with tarfile.open(archive_path, "w:bz2") as tar:
            tar.add(d_working, arcname=base_name)
        logging.info(f"[{PkMessages2025.BACKUP_DONE}] {archive_path}\n")
        return archive_path
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
