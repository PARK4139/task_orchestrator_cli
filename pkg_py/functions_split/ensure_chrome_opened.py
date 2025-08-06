from pkg_py.functions_split.ensure_chatgpt_opened import ensure_chatgpt_opened
from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_chrome_opened():
    ensure_chatgpt_opened()