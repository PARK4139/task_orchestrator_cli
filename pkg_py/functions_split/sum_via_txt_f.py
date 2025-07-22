from pkg_py.pk_system_object.directories_reuseable import D_PROJECT

from pkg_py.functions_split.pk_print import pk_print


def sum_via_txt_f():
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    f_func_n_txt = rf'{D_PROJECT}\pkg_txt\{func_n}.txt'
    ensure_pnx_made(pnx=f_func_n_txt, mode="f")
    open_pnx_by_ext(f_func_n_txt)

    texts = get_list_from_f(f=f_func_n_txt)
    # texts=texts.split("\n")
    texts = get_list_striped_element(working_list=texts)
    total = 0
    for text in texts:
        if text is not None:
            total += int(text.strip())
    [pk_print(item) for item in texts]
    pk_print(f'''len(texts)={len(texts)}''')
    pk_print(f'''total={total}''')
