from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from dirsync import sync
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def set_pk_plain_str(f_token, plain_str, f_key):
    f_token = get_pnx_os_style(f_token)
    if does_pnx_exist(f_token) and len(get_str_from_f(f=f_token).strip()) == 0:
        ensure_pnx_removed(f_token)

    if not does_pnx_exist(f_token):
        ensure_pnx_made(pnx=f_token, mode='f')
        import toml
        data = encrypt_token(plain_str, get_pk_key_from_f(f=f_key))
        o = {"api": data}
        with open(f_token, "w", encoding="utf-8") as f_obj:
            toml.dump(o, f_obj)
        if LTA:
            pk_print(f'''token set. {f_token} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
    else:
        if LTA:
            pk_print(f'''len(get_list_from_f(f_token))={len(get_list_from_f(f_token))} {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''token is already set {f_token} {'%%%FOO%%%' if LTA else ''}''')
