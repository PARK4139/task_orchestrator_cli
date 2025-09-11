from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_refactor_py_file_list():
    import os
    import glob
    import logging
    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.pk_map_texts import PkTexts
    from sources.functions.ensure_slept import ensure_slept

    # Build refactor_dir path (absolute)
    current_dir = os.path.dirname(__file__)
    refactor_dir = os.path.abspath(os.path.join(current_dir, "..", "refactor"))

    # Print refactor_dir path for debugging
    log_msg = f"refactor_dir={refactor_dir}"
    logging.debug(log_msg + (" %%%FOO%%%" if LTA else ""))

    # List all .py files in refactor_dir
    pattern = os.path.join(refactor_dir, "*.py")
    return sorted(glob.glob(pattern))
