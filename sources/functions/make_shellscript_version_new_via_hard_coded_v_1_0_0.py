

from sources.objects.pk_local_test_activate import LTA
import logging


def make_shellscript_version_new_via_hard_coded_v_1_0_0():
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    import os.path

    import os
    import shutil
    import re

    def get_f_next_versioned(f_nx):
        import inspect

        from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()

        # f 이름과 확장자를 분리
        f_n, f_x = os.path.splitext(f_nx)

        # 현재 _d_에 있는 모든 f 리스트
        f_list = os.listdir("..")

        # 정규표현식으로 "v1.x.y" 형태의 버전을 찾기
        f_versioned_list = [f for f in f_list if re.match(fr"{re.escape(f_n)}_v\d+\.\d+\.\d+{re.escape(f_x)}", f)]

        if f_versioned_list:
            # 최신 버전을 찾기 위해 버전별로 분리하여 정렬
            latest_version = max(f_versioned_list, key=lambda x: list(map(int, re.findall(r"\d+", x)[-3:])))
            major, minor, patch = map(int, re.findall(r"\d+", latest_version)[-3:])

            # 버전을 업데이트, 다음 패치 버전 생성
            patch += 1
            next_version = f"{major}.{minor}.{patch}"
        else:
            # 기존 버전이 없으면 기본 v1.0.0으로 생성
            next_version = "1.0.0"

        return f"{f_n}_v{next_version}{f_x}"

    def copy_with_version(file_pnx):

        import inspect
        from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()

        # f 유효성 검사
        if not os.path.isfile(file_pnx):
            logging.debug(rf'''file_pnx="{file_pnx}"  {'%%%FOO%%%' if LTA else ''}''')
            return

        # 복사
        file_pnx_new = get_f_next_versioned(os.path.basename(file_pnx))
        shutil.copy2(file_pnx, file_pnx_new)
        logging.debug(rf'''file_pnx_new="{file_pnx_new}"  {'%%%FOO%%%' if LTA else ''}''')

    # 절대 경로를 사용하여 대상 f의 절대 경로를 입력
    file_pnxs = [
        os.path.expanduser(r"~/Downloads/pk_working/task_orchestrator_cli/vpc_info_collector.sh"),
        os.path.expanduser(r"~/Downloads/pk_working/task_orchestrator_cli/pk_ip_connection_update_for_114.sh"),
        os.path.expanduser(r"~/Downloads/pk_working/task_orchestrator_cli/pk_ip_connection_update_for_front.sh"),
        os.path.expanduser(r"~/Downloads/pk_working/task_orchestrator_cli/pk_ip_connection_update_for_rear.sh"),
        os.path.expanduser(r"~/Downloads/pk_working/task_orchestrator_cli/pk_ip_connection_update_for_reset.sh"),
    ]

    # 각 f을 복사하여 버전별로 관리
    for file_pnx in file_pnxs:
        copy_with_version(file_pnx)
