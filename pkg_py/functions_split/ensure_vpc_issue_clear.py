from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_vpc_issue_clear():
    vpc_issue_code = get_vpc_issue_code()
    if vpc_issue_code:
        ensure_printed(f'''vpc_issue_code={vpc_issue_code} {'%%%FOO%%%' if LTA else ''}''')
        save_vpc_issue_code(vpc_issue_code)
        exec_vpc_doctor(vpc_issue_code)  # run solution function about solution code
