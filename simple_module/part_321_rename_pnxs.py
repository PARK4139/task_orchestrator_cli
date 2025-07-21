from pkg_py.simple_module.part_014_pk_print import pk_print


def rename_pnxs(pnx_list):
    import traceback

    for pnx in pnx_list:
        try:
            src = pnx[0]
            pnx_new = pnx[1]
            rename_pnx(src=src, pnx_new=pnx_new)
        except:
            pk_print(f"{traceback.format_exc()}", print_color='red')
