

def get_nx(pnx):
    import os
    return rf"{os.path.splitext(os.path.basename(pnx))[0]}{os.path.splitext(os.path.basename(pnx))[1]}"
