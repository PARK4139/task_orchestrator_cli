

from pkg_py.functions_split.is_f import is_f


def get_x(pnx):
    """ . 포함해서 리턴한다 ex> .txt """
    import os
    if is_f(pnx=pnx):
        return rf"{os.path.splitext(os.path.basename(pnx))[1]}"
    else:
        return ""
