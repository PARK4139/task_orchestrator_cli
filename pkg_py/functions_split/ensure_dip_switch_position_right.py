from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def ensure_dip_switch_position_right(vpc_data):
    vpc_identifier = vpc_data.vpc_identifier
    if 'no' in vpc_identifier:
        locate_dip_switchitch_on_board_to_left_down()
    elif 'nx' in vpc_identifier:
        pass
    elif 'xc' in vpc_identifier:
        pass
    elif 'evm' in vpc_identifier:
        pass
    else:
        pk_print(f'''unknown vpc_identifier ({vpc_identifier}) {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        raise
