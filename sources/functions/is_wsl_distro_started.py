



from sources.objects.pk_local_test_activate import LTA
from sources.functions.ensure_command_executed import ensure_command_executed
import logging


def is_wsl_distro_started(wsl_distro_name):
    cmd = rf'wsl -l -v'
    # std_list = ensure_command_executed(cmd=cmd, encoding='utf-16')
    std_outs, std_errs = ensure_command_executed(cmd=cmd, encoding='utf-16-le')
    std_list = std_outs # Assign stdout_lines to std_list

    logging.debug(f"In is_wsl_distro_started, type(std_list)={type(std_list)}, std_list={std_list}")
    if std_list and len(std_list) > 0:
        logging.debug(f"In is_wsl_distro_started, type(std_list[0])={type(std_list[0])}, std_list[0]={std_list[0]}")
    try:
        from sources.functions.get_list_removed_by_removing_runtine import get_list_removed_by_removing_runtine
    except ImportError:
        logging.error("Failed to import get_list_removed_by_removing_runtine. Please ensure the module is available.")
        return 0 # Or handle the error appropriately
    std_list = get_list_removed_by_removing_runtine(working_list=std_list)
    signiture = wsl_distro_name
    signiture2 = 'Running'
    for line in std_list:
        if signiture in line:
            if signiture2 in line:
                if LTA:
                    logging.debug(f'''{wsl_distro_name} is started in wsl {'%%%FOO%%%' if LTA else ''}''')
                return 1
    return 0
