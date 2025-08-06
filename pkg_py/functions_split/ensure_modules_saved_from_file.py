from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_modules_saved_from_file(f_working, func_n):
    from pkg_py.functions_split.get_modules_from_file import get_modules_from_file
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
    from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.directories import D_PKG_CACHE_PRIVATE
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025
    import os

    save_file = os.path.join(D_PKG_CACHE_PRIVATE, f"modules_collected.txt")
    ensure_pnx_made(pnx=save_file, mode="f")

    f_working = get_pnx_os_style(f_working)
    modules = get_modules_from_file(f_working)
    
    if modules:  # 빈 리스트 체크로 성능 향상
        ensure_printed(f'''[{PkMessages2025.DATA}] {len(modules)}개 모듈 수집: {f_working} {'%%%FOO%%%' if LTA else ''}''')
        # 각 파일마다 append 하지 말고 리턴만 - 전체 중복제거는 ensure_modules_printed에서
        return modules, save_file
    
    return [], save_file
