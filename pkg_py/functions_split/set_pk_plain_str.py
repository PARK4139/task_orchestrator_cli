from pkg_py.functions_split.get_historical_list import get_historical_list

from dirsync import sync
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


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
            ensure_printed(f'''token set. {f_token} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
    else:
        if LTA:
            ensure_printed(f'''len(get_list_from_f(f_token))={len(get_list_from_f(f_token))} {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''token is already set {f_token} {'%%%FOO%%%' if LTA else ''}''')
