from pkg_py.functions_split import get_pnx_os_style
from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
from pkg_py.functions_split.is_d import is_d


@ensure_seconds_measured
def ensure_modules_printed():
    import inspect
    from pkg_py.functions_split.ensure_modules_saved_from_file import ensure_modules_saved_from_file
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_pnxs_from_d_working import get_pnxs_from_d_working
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.functions_split.get_value_via_fzf_or_history_routine import get_value_via_fzf_or_history_routine
    from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
    from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f  # 추가된 import
    from pkg_py.functions_split.get_modules_from_file import get_modules_from_file  # 추가된 import
    from pkg_py.system_object.directories import D_PKG_PY, D_PKG_CACHE_PRIVATE  # D_PKG_CACHE_PRIVATE 추가
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025
    import os  # 추가된 import
    
    if LTA:
        decision = "d_working_mode"
        # decision = "f_working_mode"
        # decision = get_value_completed(key_hint=rf"{PkMessages2025.MODE}=", values=["d_working_mode", "f_working_mode"])
    else:
        decision = get_value_completed(key_hint=rf"{PkMessages2025.MODE}=", values=["d_working_mode", "f_working_mode"])
    if decision == "d_working_mode":
        all_modules = set()  # 전체 모듈을 저장할 set
        save_file = os.path.join(D_PKG_CACHE_PRIVATE, "modules_collected.txt")
        
        init_options = [
            get_pnx_os_style(directory)
            for directory in get_pnxs_from_d_working(D_PKG_PY, with_walking=True, only_dirs=True)
            if ".venv" not in directory
            if "__pycache__" not in directory
        ]
        
        # 모든 파일에서 모듈 수집
        for pnx in init_options:
            if is_d(pnx):
                ensure_printed(f'''[{PkMessages2025.DATA}] 디렉토리 처리: {pnx} {'%%%FOO%%%' if LTA else ''}''')
                python_files = [
                    get_pnx_os_style(file)
                    for file in get_pnxs_from_d_working(pnx, with_walking=True, only_files=True)
                    if file.endswith('.py')
                ]
                
                for python_file in python_files:
                    modules = get_modules_from_file(python_file)  # 직접 호출로 변경
                    all_modules.update(modules)  # set의 update로 빠른 중복제거
        
        # 한 번에 모든 모듈을 정렬하고 파일에 저장
        if all_modules:
            final_modules = sorted(all_modules, reverse=True)
            ensure_list_written_to_f(final_modules, save_file, mode='w')  # w 모드로 덮어쓰기
            ensure_printed(f'''[{PkMessages2025.DATA}] 총 {len(final_modules)}개 고유 모듈 저장됨 {'%%%FOO%%%' if LTA else ''}''')
            ensure_pnx_opened_by_ext(save_file)
        else:
            ensure_printed("처리할 파일이 없습니다.", print_color='yellow')
    elif decision == "f_working_mode":
        key_name = 'f_working'
        func_n = inspect.currentframe().f_code.co_name
        file_id = get_file_id(key_name, func_n)
        editable = False
        # editable = True
        init_options = [
            get_pnx_os_style(file)
            for file in get_pnxs_from_d_working(D_PKG_PY, with_walking=True, only_files=True)
            if ".venv" not in directory  # 수정: not in으로 변경
            if "__pycache__" not in directory  # 수정: not in으로 변경
            if file.endswith(".py")
        ]
        value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
        f_working = value
        save_file = ensure_modules_saved_from_file(f_working=f_working, func_n=f_working)
        ensure_pnx_opened_by_ext(save_file)
