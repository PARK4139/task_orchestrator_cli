# import win32gui
# import pywin32
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_014_pk_print import pk_print
from bs4 import BeautifulSoup


def encrypt_token(token, key):
    from base64 import b64encode
    from Cryptodome.Cipher import AES
    from Cryptodome.Random import get_random_bytes
    def pad(s):
        return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

    iv = get_random_bytes(16)  # 16바이트 IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_token = pad(token).encode()
    ciphertext = cipher.encrypt(padded_token)
    return {
        "ciphertext": b64encode(ciphertext).decode("utf-8"),
        "iv": b64encode(iv).decode("utf-8")
    }
