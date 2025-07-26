from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def check_latest_aifw_version_and_get_version_seleted(vpc_identifier, aifw_version):
    return aifw_version  # code for temp

    vpc_identifier = vpc_identifier.strip()
    vpc_identifier = vpc_identifier.lower()
    if 'no' in vpc_identifier:
        # todo gitlab 에서 latest 파싱하도록 후 vpc_aifw_version 와 비교, 같으면 진행, 다르면 질의(latest 는 몇입니다. 업데이트 할까요?)
        pass
    elif 'nx' in vpc_identifier:
        pass
    elif 'xc' in vpc_identifier:
        pass
    elif 'evm' in vpc_identifier:
        pass
    else:
        ensure_printed(f'''unknown vpc_identifier ({vpc_identifier}) {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        raise
    if LTA:
        ensure_printed(f'''aifw_version={aifw_version} {'%%%FOO%%%' if LTA else ''}''')
    return aifw_version
