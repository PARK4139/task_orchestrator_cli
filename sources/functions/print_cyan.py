from sources.functions.print_prompt_via_colorama import print_prompt_via_colorama


def print_cyan(prompt, flush=True, line_feed_mode=1):
    print_prompt_via_colorama(prompt, 'CYAN', flush, line_feed_mode)
