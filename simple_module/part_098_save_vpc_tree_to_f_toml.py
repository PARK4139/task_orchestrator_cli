from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style


def save_vpc_tree_to_f_toml(f, config_remote_os):
    f = get_pnx_os_style(pnx=f)
    vpc_tree = get_remote_tree(**config_remote_os, d_path="~/")
    vpc_tree_list = vpc_tree.split('\n')
    data = {"tree": {"paths": vpc_tree_list}}
    set_data_to_f_toml(data, f)
