from pkg_py.functions_split.ensure_printed import ensure_printed


def rename_pnxs(pnx_list):
    import traceback

    for pnx in pnx_list:
        try:
            src = pnx[0]
            pnx_new = pnx[1]
            rename_pnx(src=src, pnx_new=pnx_new)
        except:
            ensure_printed(f"{traceback.format_exc()}", print_color='red')
