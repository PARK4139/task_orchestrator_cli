from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_hardware_right(vpc_data):
    ensure_wiring_pysical_right(vpc_data)
    ensure_dip_switch_position_right(vpc_data)

    if 'no' in vpc_data.vpc_identifier:
        pass
    elif 'nx' in vpc_data.vpc_identifier:
        ensure_printed(f'''케이스 조립 전 종단저항 12개 remove{'%%%FOO%%%' if LTA else ''}''')
    elif 'xc' in vpc_data.vpc_identifier:
        ensure_printed(f'''XC 메인보드에 특이사항 저항 없으면 출고불가능 처리{'%%%FOO%%%' if LTA else ''}''')
    elif 'evm' in vpc_data.vpc_identifier:
        ensure_printed(f'''evm/메인보드/SD 카드 remove {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''evm/메인보드/2핀점퍼 remove {'%%%FOO%%%' if LTA else ''}''')
