from pkg_py.system_object.directories import D_PKG_CACHE_PRIVATE
from pkg_py.system_object.directories  import D_PROJECT


def back_up_pnx_list_from_f_txt(dst):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    f_txt = rf'{D_PROJECT}\pkg_cache_private\{func_n}.txt'
    ensure_pnx_made(pnx=D_PKG_CACHE_PRIVATE, mode="d")
    ensure_pnx_made(pnx=f_txt, mode="f")
    # open_pnx(f_func_n_txt)
    texts = get_list_from_f(f=f_txt)
    texts = get_list_deduplicated(working_list=texts)
    texts = get_list_striped_element(working_list=texts)
    for text in texts:
        pk_back_up_pnx(pnx_working=text, d_dst=dst)
