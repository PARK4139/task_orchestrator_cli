import sys
from pkg_py.functions_split.ensure_bashrc_zshrc_backed_up import ensure_bashrc_zshrc_backed_up
from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once

ensure_colorama_initialized_once()

# 명령행 인수에서 custom suffix 받기
custom_suffix = None
if len(sys.argv) > 1:
    custom_suffix = sys.argv[1]
    print(f"📝 사용자 정의 suffix 사용: {custom_suffix}")

# 메인 실행
backed_up_files = ensure_bashrc_zshrc_backed_up(custom_suffix=custom_suffix)

if backed_up_files:
    print(f"✅ 총 {len(backed_up_files)}개 파일 백업 완료")
else:
    print("⚠️ 백업할 파일이 없습니다") 