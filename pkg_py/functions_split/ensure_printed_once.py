

def ensure_printed_once(msg):
    import os.path

    from pkg_py.system_object.directories import D_PKG_PKL
    from pkg_py.functions_split.load_logged_set import load_logged_set
    from pkg_py.functions_split.save_logged_set import save_logged_set
    from pkg_py.functions_split.ensure_printed import ensure_printed

    # 프로그램초기실행완료여부 pickle 에 저장  -> 프로그램초기실행완료여부==False 면 출력
    # 프로그램초기 1회 만 동작
    file_id = "state_about_ensure_printed_once"
    f_pkl = os.path.join(D_PKG_PKL, f'{file_id}.pkl')
    logged_set = load_logged_set(f_pkl)
    if msg in logged_set:
        return
    ensure_printed(msg)
    logged_set.add(msg)
    save_logged_set(logged_set, f_pkl)
