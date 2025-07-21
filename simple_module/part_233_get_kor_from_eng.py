import shlex
import requests
import re
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from moviepy import VideoFileClip
from datetime import timedelta
from bs4 import BeautifulSoup
from pkg_py.pk_system_layer_directories import D_PKG_PY


def get_kor_from_eng(english_word: str):
    translating_dictionary = {
        "id": "아이디",
        "pw": "패스워드",
        "e mail": "이메일",
    }
    result = ""
    try:
        result = translating_dictionary[english_word]
    except:
        result = english_word
    return result
