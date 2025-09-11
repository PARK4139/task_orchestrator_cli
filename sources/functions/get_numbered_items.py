from typing import List

from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_numbered_items(items: List):
    from sources.objects.pk_local_test_activate import LTA

    import logging
    numbered_prompts = []
    for i, prompt in enumerate(items):
        numbered_prompts.append(f"{i + 1}. {prompt}")
        if LTA:
            # logging.debug(f"{i + 1}. {prompt}")
            pass
    return numbered_prompts
