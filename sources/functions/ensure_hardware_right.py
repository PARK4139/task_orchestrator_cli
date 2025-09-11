from sources.objects.pk_local_test_activate import LTA
import logging


def ensure_hardware_right (target_device_data):
    ensure_wiring_pysical_right (target_device_data)
    ensure_dip_switch_position_right (target_device_data)

    if 'no' in target_device_data.device_identifier:
        pass
    elif 'nx' in target_device_data.device_identifier:
        logging.debug(f'''케이스 조립 전 종단저항 12개 remove{'%%%FOO%%%' if LTA else ''}''')
    elif 'xc' in target_device_data.device_identifier:
        logging.debug(f'''XC 메인보드에 특이사항 저항 없으면 출고불가능 처리{'%%%FOO%%%' if LTA else ''}''')
    elif 'evm' in target_device_data.device_identifier:
        logging.debug(f'''evm/메인보드/SD 카드 remove {'%%%FOO%%%' if LTA else ''}''')
        logging.debug(f'''evm/메인보드/2핀점퍼 remove {'%%%FOO%%%' if LTA else ''}''')
