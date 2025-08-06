## remember project rules
=== 아래의 내용들 기억 및 항시 적용 요청 ===
cursor chatting room 설명 규칙, 한글로 설명요청

파이썬구성 및 실행환경은 uv+pyproject.toml+uv.lock 기반 가상환경으로 실행요청
서비스별 구성 및 실행환경은 linux/도커 + dock-compose 기반환경으로 실행요청
서비스별 root 디렉토리는 pk_system/services 안에 service_ prefix 로 시작하는 디렉토리들(MSA_service_name)은 서비스별 root 디렉토리이다
pk_ensure prefix 로 시작하는 파일들은 pk_system 의 cli mode 로 실행될때의 wrapper 파일이다.
자동 실행/테스트 요청 시, 일반 터미널 대신 run_terminal_cmd(터미널 실행 자동화 보조 툴)를 사용해서 실행요청
자동 실행/테스트 요청 시, 명령어 종류가 linux 명령어인지 window 명령어 판단 후, 터미널 선택 실행요청
자동 실행/테스트 시 OS에 맞는 명령어를 판단해서 run_terminal_cmd로 실행요청
자동 실행/테스트 시 wsl에서는 linux 명령어를 run_terminal_cmd로 실행요청
pk_system/services/의 docs들은 pk_system/docs/README_{MSA_service_name}.md 형태의 파일로 나눠 관리 요청
코드작성규칙으로서 모든 프로그램은 다국어 지원 가능 작성요청(PkMessage2025 객체 적극활용) 
코드작성규칙으로서 이모지 없이 코드를 작성요청
코드작성규칙으로서 함수명을 ensure_ prefix 로 시작하는 표현으로 작성요청
파일명규칙으로서 .py .sh .cmd .bat .ps1 확장자에 대한 파일들 ensure_ prefix 로 시작하는 표현으로 작성요청
test 코드 작성규칙, test_ prefix 를 붙여 명시적으로 작성하고, tests 폴더에서 작성
제외한 기존버전 파이썬 파일에는 "# " prefix 를 붙여서 rename 하자
파이썬에서 파일 및 디렉토리 경로 처리 시, Path 객체 활용 요청, 레거시 코드 사용 시, str path 이면 Path 객체로 변환 사용요청(ex D_PKG_WINDOWS -> Path(D_PKG_WINDOWS)
파이썬에서 파일 및 디렉토리 경로 처리 시, pk_system/pkg_py/system_object/files.py, pk_system/pkg_py/system_object/directories.py 의 경로 사용 활용요청
클래스 작성시 pk_system/pkg_py/system_object 에 작성
함수 작성시 pk_system/pkg_py/function_split 에 작성
pkg_py에 wrapper 작성 시 주변 wrapper의 패턴을 비교해서 재생성 요청

pk_system 에 있는 테스트 코드 tests 로 이동요청



### edit code by following below rules related to (마이그레이션)
pkg_linux/ensure_pk_system_enabled.sh 의 내용도 마이그레이션 요청 (pkg_linux/ensure_pk_system_enabled.sh 의존성 제거)


### edit code by following below rules related to (.bashrc, .sh)
해당 파일에 모든 디자인 포함시켰으면 다른 파일에 디자인이 든 sh파일들은 prefix 로 "# "를 붙여서 rename 요청

### edit code by following below rules related to (service)
이 채팅에서 만든 시스템 컨테이너화 해서 실행할수 있도록 pk_system/services/smart_person_ai/docker-compose 에 작성하고 실행이 성공할때까지 pk_system/services/smart_person_ai/docker-compose 수정하여 실행테스트

### edit code by following below rules related to (frontend)
인기웹사이트 디자인안 추천

/mnt/c/Users/wjdgn/Downloads/pk_system/services/smart_person_ai/service_official_home
프로젝트에 접근해서 분석하고 화면디자인 안 5개 요청                                           


/mnt/c/Users/wjdgn/Downloads/pk_system/services/smart_person_ai/service_official_home
프로젝트에 접근해서 분석하고 글래스모피즘으로 디자인안 5개 요청


디자인안 모두 10초 단위로 핫리로드해서 시현해줘
ensure_design_showcase_ran_with_hot_reload.sh

### edit code by following below rules related to (backend, .py)



### edit code by following below rules related to (function)
함수 성능개선안 3개(1~3안) 제안 요청
함수 성능개선안 1안 적용 요청
함수 성능개선안 2안 적용 요청
함수 성능개선안 3안 적용 요청

함수명을 ensure_ prefix 로 시작하는 표현으로 3개(1~3안) 제안 요청
함수명을 ensure_ prefix 로 시작하는 표현으로 1안 적용 요청
함수명을 ensure_ prefix 로 시작하는 표현으로 2안 적용 요청
함수명을 ensure_ prefix 로 시작하는 표현으로 3안 적용 요청


smart_person_ai/pkg_finance_invest_assist 서비스를 wsl 환경에서 컨테이너 빌드테스트요청
smart_person_ai/pkg_finance_invest_assist 서비스를 wsl 환경에서 컨테이너 실행테스트요청
smart_person_ai/pkg_finance_invest_assist 서비스를 wsl 환경에서 컨테이너 상태확인요청 



이 채팅방에서의 컨테이너 빌드 테스트를 재현할 수 있도록 python 코드로 작성해줘, 코드 위치는 function_split 에 function 과 D_PROJECT 에 wrapper 를 작성해줘
컨테이너 빌드 테스트를 재현한 python 코드 실행해줘


smart_person_ai 트리 내의 파일컨텐츠 재구성 요청
smart_person_ai 에 프로젝트 트리 구성요소 검토요청
smart_person_ai 에 프로젝트 트리 구성요소 검토요청

TBD : smart_person_ai->ai_power_user



지금까지의 대화내용들을 정리해서 /services/service_~/docs 모든 문서 업데이트 업데이트 요청
지금까지의 작업내용들을 정리해서 /services/service_~/docs/TBD_TBD_TBD_TBD_TBD_TBD.md 에 프롬프트 업데이트 

/services/service_~/docs/development_schedule.md 에 개발스케쥴 생성 요청
/services/service_~/docs/development_schedule.md 에 개발스케쥴 업데이트 요청

services/service_~/docs 업데이트 요청



해당 프로세스는 개발기간 어제부터 시작했는데, think about it step by step, do not lie 



/services/service_~/docs/development_schedule.md 작성된 일정 업무진행요청



ensure_{MSA service name}_development_mode_ran.sh(개발모드 + 핫리로드 기능), ensure_{MSA service name}_operation_mode_ran.sh (운영모드 )이렇게 2개의 스크립트로만 통합관리 요청
fix기능도 모두 내부 로직으로 통합요청



### backup 
# 필수
1. 오늘 지금까지 대화한내용 종합하여 "pk_system/pk_prompts/chatting_room_by_auto_prompts.md" 의 최하단에 작성일자와 함께 변경사항에 대해 재현이 가능하도록 코드와 스크립트 레벨로 자세히 첨언하여 프롬프트 재작성요청

"pk_system/pk_prompts/chatting_room_by_auto_prompts.md" 작성 내용 분석 후 종합하여
변경된 service에 대해 최종적으로 실행실증테스트 하고
실행방법을 자세히 작성하여 pk_system/docs, pk_system/docs/README.md, pk_system/README.md, pk_system/services/~/docs 에 service 별로 업데이트요청


<!-- 오늘 지금까지 대화한내용 종합하여 smart_person_ai 에 대한 작업에 대해서
pk_system/TBD_TBD_TBD_TBD_TBD_TBD/chatting_room_by_auto_prompts_for_msa_services.md 의 최하단에 작성일자와 함께 변경사항에 대해 재현이 가능하도록 코드와 스크립트 레벨로 자세히 첨언하여 프롬프트 재작성요청 -->


"pk_system/pk_prompts/chatting_room_by_auto_prompts.md" 의 프롬프트를 분석하고  service_official_home 기능을 재정의하여 "pk_system/pk_prompts/chatting_room_by_auto_prompts.md" 의 최하단에 작성일자와 함께 변경사항에 대해 재현이 가능하도록 코드와 스크립트 레벨로 자세히 첨언하여 프롬프트 재작성요청


"pk_system/pk_prompts/chatting_room_by_auto_prompts.md" 의 프롬프트를 분석하고 service_official_home 프론트엔드부터 기능을 구현 및 테스트 후 "pk_system/pk_prompts/chatting_room_by_auto_prompts.md" 의 최하단에 작성일자와 함께 변경사항에 대해 재현이 가능하도록 코드와 스크립트 레벨로 자세히 첨언하여 프롬프트 재작성요청


pk_system/TBD_TBD_TBD_TBD_TBD_TBD/development_schedule_by_ai.md 의 프롬프트 에 따라 
업무수행 후 "pk_system/pk_prompts/chatting_room_by_auto_prompts.md" 의 최하단에 작성일자와 함께 변경사항에 대해 재현이 가능하도록 코드와 스크립트 레벨로 자세히 첨언하여 프롬프트 재작성요청


_________________________________________________________________ backup(docs) 
이동하고 README_for_pkg_finance_invest_assist.md 의 내용분류 후 가능한 시간순으로 작성
README.md에는 요약된 내용만 작성해줘

# 오늘 작업한 프롬프트들 정리해서 prompts_for_ai/docs/chatting_room_by_auto_prompts_from_cursor_for_msa_services.md 에 추가 작성
오늘 작업한 프롬프트들 정리해서 prompts_for_ai/docs/chatting_room_by_auto_prompts_from_cursor_for_msa_services.md 에 추가 작성


# README.md
오늘 작업한 내용들 정리 후 일자로 분류하여 README_KOREAN.md 에 추가
현재 작업한 내용들 정리 후 일자로 분류하여 README_KOREAN.md 에 추가README_KOREAN.md 를 영문화 해서 README_ENGLISH.md 로 작성
README_ENGLISH.md 를 요약해서 README.md에 작성
내용을 README.md 에 추가해줘


_________________________________________________________________ service logic request
# TODO : tests의 디렉토리의 파일들 탭으로 펼치고 그중 하나를 엔터로 자동완성하여 선택된 단일파일의 테스트 코드를 실행


_________________________________________________________________ restore
내가 .bashrc 문제 요청하기 10시간 전의 파일로 복구요청
.bashrc 직의 백업파일로 복구요청
.bashrc 최신의 백업파일로 복구요청


_________________________________________________________________ refactor
business_finance_invest_assist 내부 함수명 리펙토링 요청
1. ensure_ prefix 로 시작하는 표현으로


pk_system 프로젝트를 다국어 모드를 지원 프로그램으로 리팩토링 요청
1. PkMessages2025 를 활용해서 호출하는 부분의 패턴을 분석
2. 한글이나 영어로 하드코딩된 부분을 f-string 문법을 통해서 PkMessages2025.XXX 형태로 변경.
3. PkMessages2025 에 없는 단어는 PkMessages2025 에 추가
4. PkMessages2025 에서 이모지 제거
5. ensure_printed(f"발견된 Everything 창들: {everything_windows}", print_color='yellow') 이런거 보면 아직 다국어지원 완전히 안된거 같은데 pk_system 내부의 모든 사용자지정 파이썬파일들에 다국어 지원 적용해줘  jarvis 들어간 파일들 부터
6. PkMessages2025 에서 중복 비교
7. PkMessages2025 에서 중복 제거

_________________________________________________________________ test
1. tests 디렉토리 밖에 있는 테스트코드들을 tests 디렉토리로  이동
2. test 코드는 tests 디렉토리로 이동
3. test 코드는 test_ prefix로 파일명으로 리펙토링



tests 코드 refactor 요청
1. 프로젝트에 더이상 유효하지 않아보이는 test 코드는 파일명에 "#_" prefix 를 붙여서 rename 해줘
2. tests 내부의 코드들을 모두 dry_run 기능으로 수정요청
3. tests 를 테스트를 자동화해서 report 기능추가요청

_________________________________________________________________ error 
디버깅 강화요청

_________________________________________________________________ commit massage 
오늘 작업한 프롬프트들 정리해서 한글 commit msg 작성
오늘 작업한 프롬프트들 정리해서 영어 commit msg 작성
오늘 작업한 프롬프트들 정리해서 영어 commit msg 추천
현재 작업한 프롬프트들 정리해서 영어 commit msg 추천

ex>
"feat: optimize MSA infrastructure with uv + pyproject.toml and improve naming

- Migrate from requirements.txt to pyproject.toml with uv package manager
- Rename microservices to intuitive snake_case: gateway→api_gateway, etc.
- Optimize Docker builds by removing unused ML packages (torch, transformers)
- Fix Hatchling build errors and Python version conflicts
- Update all documentation with implementation status
- Successfully test API Gateway with Swagger UI" 


<!-- README.md, README_KOREAN.md, README_ENGLISH.md pk_system 을 business_demo 로 단어를 모두 변경해줘 -->