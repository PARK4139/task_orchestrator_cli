from sources.objects.pk_local_test_activate import LTA
import logging


def ensure_target_issue_clear():
    target_device_issue_code = get_target_issue_code()
    if target_device_issue_code:
        logging.debug(f'''vpc_issue_code={vpc_issue_code} {'%%%FOO%%%' if LTA else ''}''')
        save_target_issue_code(vpc_issue_code)
        exec_target_doctor(vpc_issue_code)  # run solution function about solution code
