import logging


def rename_pnxs(pnx_list):
    import traceback

    for pnx in pnx_list:
        try:
            src = pnx[0]
            pnx_new = pnx[1]
            rename_pnx(src=src, pnx_new=pnx_new)
        except:
            logging.debug(f"{traceback.format_exc()}")
