

from pkg_py.system_object.directories import D_DOWNLOADS
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.get_d_working import get_d_working


def gather_pnxs_special():
    import inspect
    import os
    import traceback

    func_n = inspect.currentframe().f_code.co_name
    d_func_n = rf"{D_PROJECT}\{func_n}"  # func_n_d 에 저장
    ensure_pnx_made(pnx=d_func_n, mode="d")

    ensure_pnx_opened_by_ext(pnx=d_func_n)

    if not is_window_opened(window_title_seg=func_n):
        ensure_pnx_opened_by_ext(pnx=d_func_n)

    starting_d = get_d_working()

    dst = d_func_n
    if not os.path.exists(dst):
        return
    services = os.path.dirname(dst)
    os.chdir(services)
    storages = []
    cmd = rf'dir /b /s "{D_DOWNLOADS}"'
    lines = ensure_command_excuted_to_os_like_person_as_admin(cmd)
    for line in lines:
        if line.strip() != "":
            storages.append(line.strip())

    ensure_printed(rf'archive_py 는 storage 목록 에서 제외')
    withouts = ['archive_py']
    for storage in storages:
        for without in withouts:
            if is_pattern_in_prompt(prompt=storage, pattern=without, with_case_ignored=False):
                storages.remove(storage)
    for storage in storages:
        print(storage)

    ensure_printed(rf'이동할 storage 목록 중간점검 출력 시도')
    for storage in storages:
        print(os.path.abspath(storage))

    if not storages:
        ensure_printed(rf'이동할 storage 목록 이 없어 storage 이동을 할 수 없습니다')
    else:
        ensure_printed(rf'이동할 storage 목록 출력 시도')
        for storage in storages:
            print(os.path.abspath(storage))
        ensure_printed(rf'목적지 생성 시도')
        if not os.path.exists(dst):
            os.makedirs(dst)
        for storage in storages:
            # print(src)
            try:
                ensure_printed(rf'storage 이동 시도')
                move_pnx(storage, dst)
            except FileNotFoundError:
                ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

            except Exception as e:
                ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

    os.chdir(starting_d)
