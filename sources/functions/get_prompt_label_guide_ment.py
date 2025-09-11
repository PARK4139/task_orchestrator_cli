from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_prompt_label_guide_ment(prompt_label):
    prompt_label_guide_ment = f"{prompt_label}를 입력해 주세요"
    return prompt_label_guide_ment
