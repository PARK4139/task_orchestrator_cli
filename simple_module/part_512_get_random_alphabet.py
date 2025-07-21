

def get_random_alphabet():
    import random
    import string

    # pk_print(f"{inspect.currentframe().f_code.co_name}()")
    return random.choice(string.ascii_letters)
