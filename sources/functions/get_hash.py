from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_hash(key_src):
    # key_src = f"담고싶은|것들을|담는다|예를 들어서"
    import hashlib


    key_hash = hashlib.md5(key_src.encode()).hexdigest()
    return key_hash
