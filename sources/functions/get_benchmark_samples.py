from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_benchmark_samples(function_name: str) -> list:
    from sources.objects.pk_sample_benchmark_logger import sampls_benchmark_logger
    return sampls_benchmark_logger.get_function_samples(function_name)
