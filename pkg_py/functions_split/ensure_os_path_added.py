from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT

from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_historical_list import get_historical_list


def ensure_os_path_added():
    # from pkg_py.pk_system_object.auto_completer import get_value_completed
    #
    #
    # not tested this function
    # this function is 종속적이다.
    import os, inspect

    # pkg_py 내부 함수들은 전역으로 사용 가능하다고 가정

    func_n = inspect.currentframe().f_code.co_name
    f_func_n_txt = rf'{D_PROJECT}\pkg_txt\{func_n}.txt'
    ensure_pnx_made(pnx=f_func_n_txt, mode="f")

    # 히스토리에서 이전 입력들 불러오기
    hist_file = rf'historical_{func_n}.txt'
    historical_list = get_historical_list(f=hist_file)

    # 사용자로부터 추가할 경로 입력
    os_path_to_add = get_value_completed(
        key_hint='os_path_to_add=',
        values=historical_list
    ).strip()

    # 실제 디렉터리가 존재할 때만 처리
    if does_pnx_exist(pnx=os_path_to_add, mode='d'):
        # 현재 PATH를 분할하고, 중복 없이 수집
        current_paths = os.environ.get('PATH', '').split(os.pathsep)
        unique_paths = []
        for p in current_paths:
            if p and p not in unique_paths and p != os_path_to_add:
                unique_paths.append(p)

        # 마지막에 새 경로 추가
        unique_paths.append(os_path_to_add)

        # OS별 구분자로 합쳐서 export
        new_path_str = os.pathsep.join(unique_paths)
        cmd_to_os(cmd=f'export PATH="{new_path_str}"')

    # 히스토리에 입력값을 맨 앞에 기록
    write_list_to_f(
        f=hist_file,
        working_list=[os_path_to_add] + historical_list,
        mode="w"
    )
