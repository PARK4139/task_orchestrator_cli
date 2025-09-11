from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.objects.pk_local_test_activate import LTA

@ensure_seconds_measured
def get_prompt_label(file_id):
    prompt_label = f"{file_id.split('_via_')[0]}"
    return prompt_label