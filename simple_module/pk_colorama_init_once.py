

def pk_colorama_init_once():
    from colorama import init as pk_colorama_init
    # pk_colorama_init(autoreset=True)
    pk_colorama_init(autoreset=True, strip=False, convert=False)  # 환경 감지 없이 바로 초기화 #	속도 향상 기대


