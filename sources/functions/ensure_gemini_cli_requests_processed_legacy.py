from sources.functions import ensure_slept
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.functions.ensure_typed import ensure_typed
from sources.functions.ensure_window_maximized_like_human import ensure_window_maximized_like_human
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_gemini_cli_window_title import get_gemini_cli_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.is_window_title_front import is_window_title_front


@ensure_seconds_measured
def ensure_gemini_cli_requests_processed_legacy(prompts , gemini_cli_window_title=None):
    import traceback

    import logging

    prompts = prompts
    logging.debug(rf'prompts={prompts}')
    if 1 < len(prompts):
        logging.debug(f"수행할 프롬프트는, {len(prompts)}개, 입니다")
        # ensure_spoken(f"수행할 프롬프트는, {len(prompts)}개, 입니다")

    try:
        if gemini_cli_window_title is None:
            gemini_cli_window_title = get_gemini_cli_window_title()

        loop_cnt = 1
        for prompt in prompts:
            if is_window_opened(gemini_cli_window_title):
                ensure_window_to_front(gemini_cli_window_title)
                ensure_window_maximized_like_human()
                # ensure_slept(milliseconds=500)

                if is_window_title_front(window_title=gemini_cli_window_title):
                    ensure_typed(prompt)
                    ensure_slept(milliseconds=80)

                    ensure_pressed("esc")
                    ensure_slept(milliseconds=80)

                    ensure_pressed("enter")
            ensure_slept(milliseconds=80)

            # ensure_window_maximized_like_human()

            # if 1 < len(prompts):
            #     ensure_gemini_cli_single_request_done()

            loop_cnt += 1
    except:
        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
