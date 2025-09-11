from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_file_cleared(file):
    from sources.functions import ensure_pnx_made
    from sources.functions.ensure_pnx_removed import ensure_pnx_removed

    if file.exists():
        ensure_pnx_removed(pnx=file)
    ensure_pnx_made(pnx=file, mode='f')
