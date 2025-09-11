from sources.functions.ensure_chatgpt_opened import ensure_chatgpt_opened
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_chrome_opened():
    ensure_chatgpt_opened()