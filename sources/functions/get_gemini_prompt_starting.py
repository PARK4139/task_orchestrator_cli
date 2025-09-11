from objects.pk_ttl_cache_manager import ensure_function_return_ttl_cached
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
@ensure_function_return_ttl_cached(ttl_seconds=60 * 1 * 1, maxsize=10)
def get_gemini_prompt_starting():
    prompt_starting = rf"( [*너는 시니어 개발자야, 나는 중급 개발자고, 코드작업 수행을 위해서, GEMINI.md 의 모든 내용과 규칙들 숙지하고 대기요청], [] )"
    return prompt_starting
