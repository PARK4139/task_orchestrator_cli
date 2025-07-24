
from pkg_py.functions_split.is_f import is_f

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def rename_pnx(src, pnx_new):
    import os
    import time
    import traceback

    # 이름을 변경하는 경우에 재귀적으로 바뀌어야 하는 것으로 생각되어 os.renames 를 테스트 후 적용하였다.
    # os.rename 사용 중에 d  인 경우는 재귀적으로 변경이 안된다
    try:
        if not does_pnx_exist(pnx=src):
            pk_print(f'''rename 할 f이 없습니다 {src}''', print_color='red')
            return

        if src == pnx_new:
            pk_print(f'''현재f명 과 바꾸려는f명 이 같아 rename 하지 않았습니다 src={src} pnx_new={pnx_new}''')
            return

        if does_pnx_exist(pnx=pnx_new):
            pk_print(f'''dst에 중복된 f이 있습니다. {pnx_new}" ''', print_color='red')
            return

        if is_f(src):
            type_name = "f"
        else:
            type_name = "d"

        os.renames(src, pnx_new)
        time_limit = 3
        waiting_limit = 20
        time_s = time.time()
        while 1:
            if does_pnx_exist(pnx=pnx_new):
                pk_print(f'''rename {type_name} from {src} to {pnx_new}''', print_color='green')
                break
            else:
                time_e = time.time()
                time_diff = time_e - time_s
                if time_diff == time_limit:
                    return 0
                pk_sleep(milliseconds=waiting_limit)
    except:
        pk_print(
            str_working=rf'''traceback.format_exc()="{traceback.format_exc()}" rename 확인필요 src={src} pnx_new={pnx_new}  {'%%%FOO%%%' if LTA else ''}''',
            print_color='red')
