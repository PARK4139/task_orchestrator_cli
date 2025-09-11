from sources.objects.pk_local_test_activate import LTA
import logging


def print_and_open_py_pkg_global_path():
    import sys

    for sys_path in sys.path:
        logging.debug(sys_path)
        if is_pattern_in_prompt(prompt=sys_path, pattern='site-packages') == True:
            logging.debug(f'''sys_path={sys_path}  {'%%%FOO%%%' if LTA else ''}''')
            logging.debug(rf'echo "{sys_path}"')
            ensure_pnx_opened_by_ext(sys_path)
