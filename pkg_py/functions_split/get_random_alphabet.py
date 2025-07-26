

def get_random_alphabet():
    import random
    import string

    # ensure_printed(f"{inspect.currentframe().f_code.co_name}()")
    return random.choice(string.ascii_letters)
