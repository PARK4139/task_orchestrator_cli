chatgpt_4o_00. 
핀테크 서비스 기획/설계/생산/배포/서비스

chatgpt_4o_10. 
핀테크 서비스 만들고 싶어 기획/설계/생산/배포/서비스를 도와줄래?
목표는 제테크를 하는데 필요한 정보들을 크롤링이나 금융 API를 통해서 수집하고 client 에게 제공 하도록 할거야

chatgpt_4o_20. : service ~
MSA 형태로 유지보수가 아주편리하도록 하자

chatgpt_4o_30. 
가능한 모든 구성요소는 Python , Fastapi 기반으로 만들거야, web 부분은 Django 를 사용하자

chatgpt_4o_40. 
client 가 end point에 접근하는 통신프로토콜은 http 프로토콜로 구성하자 (추후 https 로 전환예정)


chatgpt_4o_50. : release
chatgpt_4o_AWS 에서 EC 2로 배포하자 


chatgpt_4o_51. : service environment isolation  
Docker 컨테이너들로 서비스를 운영하자
Python 가상환경관리는 uv + pyproject.toml + uv.lock 으로 관리리하자


chatgpt_4o_70. : project tree 
프로젝트 트리는 네가 작성한 트리를 모두 pkg_finance_invest_assist 으로 이동해서 관리하자
function 의 위치는 function_split 에서 작성
pkg_py 에서 function 명 작성 시, pk_ prefix 를 붙여서 작성


chatgpt_4o_71. : Database
# DB는 추천해줄래?
DB는 PostgreSQL Docker Container 로 사용하자
EC2에서 PostgreSQL Docker Container 띄워서 사용하자


chatgpt_4o_60. : CI/CD
CI/CD 는 추천해줄래?


chatgpt_4o_72. : functions
function 명 작성 시, ensure_ 로 prefix로서 시작 ex>  ensure_string_printed(), ensure_investing_timing_guided
function 명 작성 시, 완료형 동사를 suffix로서 종료 ex>  ensure_string_printed(), ensure_investing_timing_guided
function 명 작성 시, doc string 에는 특징을 적는 것이 중요. 
function 명 작성 시, snake case 로 작성
function_split 에서 function 명 작성 시, pk_ prefix 를 붙이지 않고 작성성

chatgpt_4o_78. : docs
README 에 표현된 기능들 중에 구현중인 것은 구현중임을 표기하고 아직 안된것은 안되었다고 표기해줘. docs 업데이트시에는 항상 기억해


chatgpt_4o_80.
기능추가 요청
- recommand_투입_timming
- recommand_harvesting_timming

chatgpt_4o_90.
생각정리를 해줘 

chatgpt_4o_95.
think about it step by step.

chatgpt_4o_100.
# 그동한 한 대화를 토대로 프롬프트를 만들어 project_requirements_for_msa_services.md 파일에 작성해 줄래?
그동한 한 대화를 토대로 Cursor AI에게 전달할 프롬프트를 만들어 project_requirements_for_msa_services.md 파일에 작성해 줄래?
그동한 한 대화를 토대로 Cursor AI에게 전달할 프롬프트를 다시 만들어 project_requirements_for_msa_services.md 파일에 작성해 줄래?