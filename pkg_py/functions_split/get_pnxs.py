

def get_pnxs(with_walking: int, filter_option=None, d_working=None):
    from pkg_py.functions_split.is_d import is_d
    import os
    if with_walking == 1:
        if d_working is None:
            d_working = os.getcwd()

        f_list = []
        d_list = []

        for root, d_nx_list, f_nx_list in os.walk(d_working):
            d = os.path.abspath(root)
            d_list.append(d)

            for f_nx in f_nx_list:
                f = os.path.join(root, f_nx)
                f_list.append(f)

            # 하위 d 탐색을 원하지 않는 경우
            if filter_option == "d":  # d만 원하면 아래 항목에서 멈춤
                del d_nx_list[:]

        # 원하는 mode에 따라 결과 반환
        if filter_option == "f":
            pnx_list = f_list
        elif filter_option == "d":
            pnx_list = d_list
        else:
            pnx_list = f_list + d_list

        # 출력제한
        print_limit = 100000000
        if len(f_list) <= print_limit:
            # ensure_printed(f'''files={files}''')
            # ensure_printed(f'''directories={directories}''')
            pass

        return pnx_list
    elif with_walking == 0:
        import os
        if d_working is None:
            d_working = os.getcwd()

        # 절대경로로 변환
        d_working = os.path.abspath(d_working)

        pnx_nx_list = os.listdir(d_working)
        f_list = []
        d_list = []

        for pnx_nx in pnx_nx_list:
            pnx = os.path.join(d_working, pnx_nx)  # 절대경로로 결합
            if is_d(pnx):
                d_list.append(pnx)  # d의 절대경로 추가
            else:
                f_list.append(pnx)  # f의 절대경로 추가

        # 원하는 mode에 따라 결과 반환
        if filter_option == "f":
            pnx_list = f_list
        elif filter_option == "d":
            pnx_list = d_list
        else:
            pnx_list = f_list + d_list
        return pnx_list
