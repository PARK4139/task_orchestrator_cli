from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.print_pk_divider import print_pk_divider


class A2zCarDataStructure:
    # vpc_data_orm
    class RemoteDeviceDataStructure:
        vpc_local_ssh_public_key = None
        vpc_local_ssh_private_key = None
        vpc_purpose = None
        vpc_type = None
        vpc_ip = None
        vpc_port = None
        vpc_user_n = None
        vpc_pw = None
        vpc_side = None
        vpc_aifw_version = None
        vpc_aifw_packing_mode = None
        vpc_aifw_branch_n = None
        vpc_with_flash_image = None
        vpc_flash_image_version = None
        vpc_core_cnt = None
        vpc_proceser_name = None
        vpc_nvidia_serial = None
        vpc_os_distro_n = None
        vpc_identifier = None
        vpc_identifier_number = None
        vpc_jetpack_version = None
        vpc_wired_connection_reset = {}
        vpc_wired_connection_initial = {}
        vpc_wired_connection_1_new = {}
        vpc_wired_connection_3_new = {}
        vpc_available_test_ip_set = set()

        def __init__(self):
            pass

        def set_remote_device_data_field_all(self, pk_structure):
            try:
                # self.identifier = pk_structure.identifier
                # self.jetpack_ver = pk_structure.jetpack_ver
                # self.vpc_flash_image = pk_structure.vpc_flash_image

                # swallow copy all field of pk_structure
                for key, value in pk_structure.__dict__.items():
                    setattr(self, key, value)

            except:
                import traceback
                pk_print(working_str=rf"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''} ", print_color='red')

        def print_remote_device_data_field_all(self, instance_name, with_none=0):
            if instance_name is None:
                instance_name = self.__class__.__name__
            print_pk_divider('%%%FOO%%%')
            if with_none == 1:
                for key, value in self.__dict__.items():
                    pk_print(f'''{instance_name}.{key}={value} {'%%%FOO%%%' if LTA else ''}''', print_color='blue')
            else:
                for key, value in self.__dict__.items():
                    if value is not None:
                        pk_print(f'''{instance_name}.{key}={value} {'%%%FOO%%%' if LTA else ''}''', print_color='blue')
            print_pk_divider('%%%FOO%%%')
