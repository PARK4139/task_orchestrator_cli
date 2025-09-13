from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_gemini_cli_assistance_executed(gemini_cli_window_title):
    from functions.ensure_window_maximized_like_human import ensure_window_maximized_like_human
    from functions.ensure_window_title_replaced import ensure_window_title_replaced
    from functions.ensure_window_to_front import ensure_window_to_front
    from functions.get_gemini_prompt_interface_title import get_gemini_cli_assistance_title

    import inspect

    from sources.functions.ensure_value_completed_advanced import ensure_value_completed_advanced
    from sources.functions.is_gemini_opened import is_gemini_opened
    from sources.functions.get_gemini_prompt_starting import get_gemini_prompt_starting
    from enum import auto, Enum

    from sources.functions.ensure_gemini_cli_requests_processed_legacy import ensure_gemini_cli_requests_processed_legacy
    import textwrap
    import logging


    orchestrator_title = get_gemini_cli_assistance_title()
    ensure_window_title_replaced(orchestrator_title)
    ensure_window_to_front(orchestrator_title)
    ensure_window_maximized_like_human()

    if not is_gemini_opened():
        logging.debug("can not request prompt to gemini")
        return False

    class PkPromptGroups(Enum):
        PK_SCHEDULER = auto()
        SMART_PLUG = auto()
        ENSURE_SPOKEN = auto()
        COMMON = auto()

    # pk_prompts_favorite
    prompts_by_group = {
        PkPromptGroups.COMMON: textwrap.dedent(rf'''
                {get_gemini_prompt_starting()}

                지금까지 대화한내용인 prompts_new/prompts.history 숙지 요청

                각 모듈은 파일 단위 관리 요청

                테스트는 내가수행할게. 이 점 기억 요청
                
                주어진 scaffold 코드에 따라 코드 생성 및 제안 요청
                
                주어진 scaffold 코드에 따라 코드 생성 요청

                테스트결과 로그 logs/task_orchestrator_cli.log 확인 요청, 논리적으로 이상한 부분 수정제안 요청

                테스트결과 로그 logs/task_orchestrator_cli.log 확인 요청, ensure_slept 가 18분 정도가 진행이 되던데 그 원인 분석

                분석결과대로 코드 수정 요청

                ensure_draft_scenario_executed(__file__) 함수를 실행해서 시나리오를 테스트 요청

                해당 내용 .cursor/rules,  GEMINI.md 에 규칙추가 요청

                지금까지 대화한내용을 prompts_new/prompts.history 에 프롬프트 작성 요청
                지금까지 대화한내용을 prompts_new/prompts.history 에 프롬프트 최신내용으로 업데이트 요청

                계속 진행 요청
                
                ensure_matter_smart_plug_on.py 디버깅을 위한 사전 기능 분석 요청

                ensure_matter_smart_plug_on.py 하위 기능들 재사용성과 테스트 용이성을 확보하기 위해서 모듈화 진행 요청
                각 모듈은 파일 단위 관리 요청

                ensure_matter_smart_plug_on.py 하위에 사용된 print()출력 함수들 사용 부분을 모두 logging.debug() 로 마이그레이션 요청

                정확한 분석을 위해, 디버깅강화 요청, ensure_matter_smart_plug_on.py 관련 로직 standard output stream 출력을 받아와 logging.debug 사용해서 디버깅 가능하도록 코드 수정 요청

                ensure_matter_smart_plug_on.py 테스트 후 디버깅 요청

                테스트결과 로그 logs/task_orchestrator_cli.log 확인 요청, ensure_matter_smart_plug_on.py 기능구현 관점으로 분석 요청

                테스트결과 로그 logs/task_orchestrator_cli.log 확인 요청, ensure_slept 가 18분 정도가 진행이 되던데 그 원인 분석

                ensure_draft_scenario_executed(__file__) 함수를 실행해서 시나리오를 테스트 요청

                pk_ensure_matter_smart_plug_on.py .venv_windows 환경에서 테스트 후 디버깅 요청
                
                🔧 복붙 프롬프트 (Markdown · Tapo 전부 제외 · Windows+WSL · python-matter-server 전용)
                당신은 Windows + WSL2 + Docker + Matter 컨트롤러에 능숙한 시니어 엔지니어다.
                아래 요구사항을 질문 없이 한 번에 충족하는 결과물을 마크다운 문서로 만들어라.
                설명은 한국어, 코드/명령/주석/파일명은 모두 영어로 작성한다.
                모든 스니펫/파일은 복붙 즉시 실행 가능해야 한다.
                ⚠️ TP-Link Tapo/Kasa 로컬 API·통합·라이브러리 관련 내용은 일절 포함하지 말 것. (이번 과제는 Matter만 사용)
                🎯 목표
                Windows에서 WSL(Ubuntu) 안에 python-matter-server(Home Assistant 팀) 컨트롤러를 Docker로 실행한다.
                TP-Link Tapo P110M(Matter 지원 스마트 플러그)을 스마트폰(Apple Home/Google Home/SmartThings)에 먼저 연결한 뒤, Matter “Multi-Admin 공유 코드” 로 WSL의 Matter 서버에 커미셔닝(추가) 한다.
                파이썬 클라이언트 또는 Raw WebSocket으로 ON/OFF 제어하고, (가능 시) Matter 전력 속성을 읽는다.
                🧰 전제
                Windows 10/11 + WSL2 Ubuntu 22.04+
                Docker Desktop 설치 및 WSL2 기반 엔진 + Ubuntu 통합 활성화
                디바이스: TP-Link Tapo P110M (전원 연결)
                WSL/Docker의 BLE 제약으로 인해, 커미셔닝은 스마트폰에서 먼저 붙임 → Matter “Multi-Admin 공유 코드”로 서버에 공유 경로를 사용
                ✅ 출력 형식 (반드시 지킬 것)
                결과물을 하나의 마크다운 문서로 출력
                섹션 헤더(##) + 한국어 설명 + 복붙 가능한 코드/명령 블록(영어) 구성
                Windows PowerShell 과 WSL(Ubuntu) 셸 명령은 명확히 구분해 별도 코드블록으로 제공
                아래 정확한 파일명과 전체 내용을 코드블록으로 제공할 것:
                docker-compose.yml
                p110m_commission_via_ws.py (공유 코드로 커미셔닝; Raw WebSocket 사용)
                p110m_matter_ws_client.py (노드 목록 → ON/OFF → (가능 시) 전력 속성 읽기; 공식 파이썬 클라이언트 사용)
                p110m_ws_raw.py (Raw WebSocket으로 ON/OFF 제어)
                질문·추가 확인 금지, 불필요한 수다 금지 — 바로 실행 가능한 산출물만 제시
                1) WSL 네트워크 설정(.wslconfig) 갱신
                설명(한국어): Matter는 IPv6/멀티캐스트 의존도가 높다. mirrored 네트워킹을 통해 WSL의 네트워크 동작을 안정화한다.
                파일 경로: %UserProfile%\.wslconfig 
                http://localhost:5580/ 접속 OK
                p110m_commission_via_ws.py 실행 후 서버 로그/대시보드에 해당 노드가 추가됨
                p110m_matter_ws_client.py 실행 시 노드 목록 표시 및 On → Off 동작 확인
                (가능 시) ActivePower 속성 값 수신
                보이지 않으면 플랫폼/펌웨어에 따라 미노출인 정상 케이스일 수 있음
                8) 트러블슈팅 (간결)
                공유 코드 만료: 새 코드 발급(일반적으로 15분 유효)
                BLE 커미셔닝 문제: WSL/Docker는 BLE 접근이 제한적 → 스마트폰에서 먼저 연결 후 공유 코드 사용
                WS 연결 실패: ws://localhost:5580/ws 확인, docker compose logs -f 로 컨테이너 상태 확인
                WSL 네트워크: .wslconfig 수정 후 wsl --shutdown 수행했는지 확인
                IPv6/멀티캐스트 환경: 라우터/스위치 설정 영향 가능, 동일 서브넷에서 테스트 권장
                보안: 5580 포트 외부 포워딩 금지
                9) 정리/청소
                WSL(Ubuntu)
                cd ~/matter
                docker compose down
                🔚 요약
                WSL에서 python-matter-server 실행 → 공유 코드로 커미셔닝 → 파이썬/Raw WS로 ON/OFF 및 속성 읽기
                Tapo 로컬 API는 전부 제외, Matter만 사용
                위의 내용을 활용하여 다른 시도 해보기를 요청
                
                ensure_spoken.py 에 보면 TTS 관련 모듈의 하위 함수들에 대한 로깅만 안되게 할수 있을까?

                ensure_spoken.py 에 보면 TTS 관련 모듈의 하위 함수들에 대한 로깅만 안되게 할수 있을까?
                분석 후 방법 3가지를 제안하고 최선의 방법을 따로 제안 요청

                나는 ensure_spoken 에 verbose 모드 옵션을 인자로 추가하고, verbose=True 이면 위의 로그를 출력하고,
                verbose=False 이면 어떤 로그도 출력하고 싶지 않아,
                수정해줘
                
                text 는 verbose 모드 관계없이 logging.debug(rf"text={{text}}") 도입부에 실행했으면 좋겠어
                
                TODO : objects/pk_spoken_manager.py 전역 싱글톤 인스턴스 로서 관리하고, text 를 stack FIFO 구조로 쓰레드로 재생하도록,
                인스턴스 종료는 프로그램이 종료될때 따로 종료할수 있도록 종료함수 생성 요청
                
                pk_ensure_routine_draft_senario_executed.py 로 ensure_spoken() 기능 검증 요청
                1. ensure_spoken gtts 통한 파일 생성 확인 요청.
                2. ensure_spoken 의 재생기능을 다양한 재생용 라이브러리를 통해서 실험 요청, 동작되는 라이브러리를 알려줘
                
                현재 루틴 변경: 점심시간 (12:10-14:00) 콘소에 찍혔는데, 이거 찍힐때 비교하기 쉽게, 현재 시간도 찍히도록 수정 요청 비슷한 포멧으로
                
                현재 루틴 변경: 오후주간작업전준비 (14:00-14:10) - 현재 시간: 14:04:54  라고 나오는데 
                루틴에 해당하는 함수명도 같이 출력이 되면 좋겠어
                
                스케쥴러에서 루틴 변경되었는데도 루틴에 상응하는 함수가 실행 안되는 것 같아.
            ''').strip(),
    }

    # pk_option
    # prompt_groups = [field.name for field in PkPromptGroups]
    # selected = ensure_value_completed(key_hint='프롬프트 그룹=', values=prompt_groups)
    # prompt_group = PkPromptGroups[selected]
    # prompts_raw = prompts_by_group.get(prompt_group, "")

    # pk_option
    prompt_group = PkPromptGroups.COMMON
    prompts_raw = prompts_by_group.get(prompt_group, "")

    if not prompts_raw:
        logging.debug("선택된 그룹에 등록된 프롬프트가 없습니다.")
        return False

    parsed_prompts = [p.strip() for p in prompts_raw.split('\n\n') if p.strip()]

    # pk_option
    key_name = "prompt_to_request"
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    selected = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=parsed_prompts, editable=False)

    prompt = selected.replace('\n', r'\n')
    logging.debug(F"prompt={prompt}")


    ensure_gemini_cli_requests_processed_legacy(prompts=[prompt], gemini_cli_window_title=gemini_cli_window_title)

    # selected = ensure_value_completed(key_hint='프롬프트 수행완료 확인여부=', values=[PkTexts.YES, PkTexts.NO])

    return True
