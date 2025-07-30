from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_refactor_py_file_list():
    import os
    import glob
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025
    from pkg_py.functions_split.ensure_slept import ensure_slept

    # Build refactor_dir path (absolute)
    current_dir = os.path.dirname(__file__)
    refactor_dir = os.path.abspath(os.path.join(current_dir, "..", "refactor"))

    # Print refactor_dir path for debugging
    log_msg = f"[{PkMessages2025.DATA}] refactor_dir={refactor_dir}"
    ensure_printed(log_msg + (" %%%FOO%%%" if LTA else ""), print_color="blue")

    # List all .py files in refactor_dir
    pattern = os.path.join(refactor_dir, "*.py")
    return sorted(glob.glob(pattern))
