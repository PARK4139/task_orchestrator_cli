

def pk_print_once(msg):
    import os.path

    from pkg_py.pk_system_layer_directories import D_PKG_PKL
    from pkg_py.simple_module.part_001_load_logged_set import load_logged_set
    from pkg_py.simple_module.part_001_save_logged_set import save_logged_set
    from pkg_py.simple_module.part_014_pk_print import pk_print

    # 프로그램초기실행완료여부 pickle 에 저장  -> 프로그램초기실행완료여부==False 면 출력
    # 프로그램초기 1회 만 동작
    file_id = "state_about_pk_print_once"
    f_pkl = os.path.join(D_PKG_PKL, f'{file_id}.pkl')
    logged_set = load_logged_set(f_pkl)
    if msg in logged_set:
        return
    pk_print(msg)
    logged_set.add(msg)
    save_logged_set(logged_set, f_pkl)
