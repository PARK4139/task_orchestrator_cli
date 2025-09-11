def ensure_text_encrypted_to_token_file(f_token, text_plain, f_key):
    from sources.functions import ensure_pnx_made
    from sources.functions.does_pnx_exist import is_pnx_existing
    from sources.functions.encrypt_token import encrypt_token
    from sources.functions.ensure_pnx_removed import ensure_pnx_removed
    import logging
    from sources.functions.get_list_from_f import get_list_from_f
    from sources.functions.get_pk_key_from_f import get_pk_key_from_f
    from pathlib import Path
    from sources.functions.get_str_from_f import get_str_from_f
    from sources.objects.pk_local_test_activate import LTA
    f_token = Path(f_token)
    if is_pnx_existing(f_token) and len(get_str_from_f(f=f_token).strip()) == 0:
        ensure_pnx_removed(f_token)

    if not is_pnx_existing(f_token):
        ensure_pnx_made(pnx=f_token, mode='f')
        import toml
        data = encrypt_token(text_plain, get_pk_key_from_f(f=f_key))
        o = {"api": data}
        with open(f_token, "w", encoding="utf-8") as f_obj:
            toml.dump(o, f_obj)
        if LTA:
            logging.debug(f'''token set. {f_token} {'%%%FOO%%%' if LTA else ''}''')
    else:
        if LTA:
            logging.debug(f'''len(get_list_from_f(f_token))={len(get_list_from_f(f_token))} {'%%%FOO%%%' if LTA else ''}''')
        logging.debug(f'''token is already set {f_token} {'%%%FOO%%%' if LTA else ''}''')


