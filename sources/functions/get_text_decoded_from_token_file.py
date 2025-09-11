def get_text_decoded_from_token_file(f_token, f_key):
    from sources.functions.decrypt_token import decrypt_token
    from sources.functions.get_pk_key_from_f import get_pk_key_from_f
    import toml
    config = toml.load(f_token)
    data = config["api"]
    key_byte = get_pk_key_from_f(f=f_key)
    return decrypt_token(data["ciphertext"], data["iv"], key_byte)

