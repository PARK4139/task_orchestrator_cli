from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.pk_print import pk_print


def gather_empty_d(d_working: str, d_dst=None):
    import os

    """
    d_src에서 빈 d를 찾아 d_dst 로 이동하는 함수.
    """
    if d_dst is None:
        d_dst = r"D:\[]\[empty]"

    ensure_pnx_made(pnx=d_dst, mode="d")  # 대상 d 생성

    if not is_d(d_working):
        pk_print(f"'{d_working}' is not a valid d.", print_color='red')
        return

    #  1. 빈 d를 찾아 이동 (한 번만 exec )
    for root, d_nx_list, f_nx_list in os.walk(d_working, topdown=False):
        if not d_nx_list and not f_nx_list and is_empty_d(root):
            move_pnx(pnx=root, d_dst=d_dst)

    #  2. 빈 트리(리프 d)를 이동 후 remove
    pk_print(f"d_working={d_working}  {'%%%FOO%%%' if LTA else ''}")

    if is_empty_tree(d_working):  # d_src 전체를 검사
        for root, d_nx_list, _ in os.walk(d_working, topdown=True):
            for d_nx in d_nx_list:
                d_working = os.path.abspath(os.path.join(root, d_nx))
                if is_leaf_d(d_working):
                    move_pnx(pnx=d_working, d_dst=d_dst)
