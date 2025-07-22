from pkg_py.functions_split.pk_print import pk_print


def is_losslesscut_playing(threshold=5.0, check_duration=3, second_interval=1):
    import time
    cpu_usages = []

    for _ in range(check_duration):
        cpu_usage = get_cpu_usage(interval=1.0, process_n="LosslessCut")
        if cpu_usage is None:
            pk_print(f'''cpu_usage is None''', print_color='red')
            return 0  # exec  중이 아니면 False

        cpu_usages.append(cpu_usage)
        print(f"📊 CPU 사용량 측정: {cpu_usage}%")
        time.sleep(second_interval)  # 1초 간격으로 CPU 측정

    avg_cpu = sum(cpu_usages) / len(cpu_usages)  # 평균 CPU 사용량 계산
    print(f"📈 평균 CPU 사용량: {avg_cpu}%")

    return avg_cpu > threshold  # 설정한 임계값보다 높으면 "Playing" 상태로 판단
