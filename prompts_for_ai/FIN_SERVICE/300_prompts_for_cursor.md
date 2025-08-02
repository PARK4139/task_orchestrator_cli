PROMPT MANAGEMENT
_________________________________________________________________ EDIT
 

함수를 개선해줘

함수명을 ensure_ prefix 로 시작하는 표현으로 제안
함수명을 ensure_ prefix 로 시작하는 표현으로 변경


fin_service 서비스를 wsl 환경에서 컨테이너 빌드 진행 # pkg_finance_invest_assist
fin_service 서비스를 wsl 환경에서 컨테이너 실행 진행 # pkg_finance_invest_assist
fin_service 서비스를 wsl 환경에서 컨테이너 상태 확인 # pkg_finance_invest_assist
가지고 



이 채팅방에서의 컨테이너 빌드 테스트를 재현할 수 있도록 python 코드로 작성해줘, 코드 위치는 function_split 에 function 과 D_PROJECT 에 wrapper 를 작성해줘
컨테이너 빌드 테스트를 재현한 python 코드 실행해줘



_________________________________________________________________ service logic request

# TODO : tests의 디렉토리의 파일들 탭으로 펼치고 그중 하나를 엔터로 자동완성하여 선택된 단일파일의 테스트 코드를 실행

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


tests의 test 코드명을 좀더 명시적으로 변경해줘


tests 코드 refactor 요청
1. 프로젝트에 더이상 유효하지 않아보이는 test 코드는 파일명에 "#_" prefix 를 붙여서 rename 해줘
2. tests 내부의 코드들을 모두 dry_run 기능으로 수행하도록 수정요청
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
_________________________________________________________________ docs 
pkg_finance_invest_assist에 작성된 여러 md 들을 docs 디렉토리를 만들어
이동하고 README_for_pkg_finance_invest_assist.md 의 내용분류 후 가능한 시간순으로 작성
README.md에는 요약된 내용만 작성해줘

# 오늘 작업한 프롬프트들 정리해서 prompts_for_ai/docs/prompts_used_by_cursor.history 에 추가 작성
오늘 작업한 프롬프트들 정리해서 prompts_for_ai/docs/prompts_used_by_cursor.history 에 추가 작성
_________________________________________________________________ README.md
오늘 작업한 내용들 정리 후 일자로 분류하여 README_KOREAN.md 에 추가
현재 작업한 내용들 정리 후 일자로 분류하여 README_KOREAN.md 에 추가README_KOREAN.md 를 영문화 해서 README_ENGLISH.md 로 작성
README_ENGLISH.md 를 요약해서 README.md에 작성
내용을 README.md 에 추가해줘

<!-- README.md, README_KOREAN.md, README_ENGLISH.md pk_system 을 business_demo 로 단어를 모두 변경해줘 -->