from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def get_vpc_issue_code(vpc_issue_code=None):
    if not vpc_issue_code:
        ensure_printed(f'''등록된 모든 테스트를 진행합니다. {'%%%FOO%%%' if LTA else ''}''')
    else:
        ensure_printed(f'''vpc_issue_code 에 대한 특정 테스트를 진행했습니다. {'%%%FOO%%%' if LTA else ''}''')
