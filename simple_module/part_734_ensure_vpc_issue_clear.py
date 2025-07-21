from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def ensure_vpc_issue_clear():
    vpc_issue_code = get_vpc_issue_code()
    if vpc_issue_code:
        pk_print(f'''vpc_issue_code={vpc_issue_code} {'%%%FOO%%%' if LTA else ''}''')
        save_vpc_issue_code(vpc_issue_code)
        exec_vpc_doctor(vpc_issue_code)  # run solution function about solution code
