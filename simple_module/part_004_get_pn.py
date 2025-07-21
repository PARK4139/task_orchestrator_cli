

def get_pn(pnx):
    import os
    return rf"{os.path.dirname(pnx)}\{os.path.splitext(os.path.basename(pnx))[0]}"
