from pkg_py.simple_module.part_014_pk_print import pk_print


def analize_tree(d_src):
    # todo : print_size : 드래그한상태에서 특정단축키를 누르면, chatgpt 에게 질문을 하는 프로세스
    import os
    largest_f = None
    largest_size = 0
    for root, d_nx_list, f_nx_list in os.walk(d_src):
        for f_nx in f_nx_list:
            f = os.path.join(root, f_nx)
            try:
                file_size = os.path.getsize(f)  # f 크기 확인
                if file_size > largest_size:
                    largest_size = file_size
                    largest_f = f
            except Exception as e:
                print(f"f 크기를 확인할 수 없습니다: {f}. 오류: {e}")
    if largest_f:
        pk_print(f'''largest_f={largest_f}''')
    else:
        pk_print(working_str="d에 f이 없거나 f 크기를 확인할 수 없습니다.")
