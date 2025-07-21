def backup_workspace(D_PKG_ARCHIVED, d_working, func_n):
    import logging
    import os
    import tarfile
    from datetime import datetime

    from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
    os.makedirs(D_PKG_ARCHIVED, exist_ok=True)
    timestamp = datetime.now().strftime('%Y_%m%d_%H%M_%S')
    base_name = os.path.basename(d_working)
    archive_name = f"{base_name}_archived_before_work_{timestamp}_via_{func_n}.tar.bz2"
    archive_path = os.path.join(D_PKG_ARCHIVED, archive_name)
    with tarfile.open(archive_path, "w:bz2") as tar:
        tar.add(d_working, arcname=base_name)
    logging.info(f"[{PkMessages2025.BACKUP_DONE}] {archive_path}\n")
    return archive_path
