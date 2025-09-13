from sources.functions.ensure_seconds_measured import ensure_seconds_measured
import logging


@ensure_seconds_measured
def fix_git_push_fail_for_large_file():
    """
    로컬 워킹 트리는 보존하면서 Git 히스토리에서 대용량 SQLite 파일을 제거하여 푸시 가능하도록 처리
    """
    import subprocess
    import tempfile
    import urllib.request
    from pathlib import Path
    
    logging.debug("🔧 Git 대용량 파일 히스토리 정리 시작...")
    
    def run_git_command(cmd, check=True):
        """Git 명령어 실행"""
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')
            if check and result.returncode != 0:
                logging.debug(f"🔧 Git 명령어 실패: {cmd}")
                logging.debug(f"에러: {result.stderr}")
                return None
            return result
        except Exception as e:
            logging.debug(f"🔧 명령어 실행 중 오류: {e}")
            return None
    
    def ensure_line_in_gitignore(line):
        """gitignore 파일에 라인 추가"""
        gitignore_path = Path('.gitignore')
        
        if gitignore_path.exists():
            content = gitignore_path.read_text(encoding='utf-8')
            if line not in content:
                with open(gitignore_path, 'a', encoding='utf-8') as f:
                    f.write(f'\n{line}\n')
                logging.debug(f"🔧 .gitignore에 추가: {line}")
            else:
                logging.debug(f"🔧 이미 존재: {line}")
        else:
            with open(gitignore_path, 'w', encoding='utf-8') as f:
                f.write(f'{line}\n')
            logging.debug(f"🔧 .gitignore 생성 및 추가: {line}")
    
    def download_git_filter_repo():
        """git-filter-repo 스크립트 다운로드"""
        temp_dir = Path(tempfile.gettempdir())
        script_path = temp_dir / "git-filter-repo.py"
        
        try:
            url = "https://raw.githubusercontent.com/newren/git-filter-repo/main/git-filter-repo"
            urllib.request.urlretrieve(url, script_path)
            logging.debug(f"🔧 git-filter-repo 다운로드 완료: {script_path}")
            return script_path
        except Exception as e:
            logging.debug(f"🔧 git-filter-repo 다운로드 실패: {e}")
            return None
    
    def check_git_filter_repo_available():
        """git-filter-repo 사용 가능 여부 확인"""
        result = run_git_command("git filter-repo --version", check=False)
        if result and result.returncode == 0:
            logging.debug("🔧 git-filter-repo 이미 설치됨")
            return True, None
        else:
            logging.debug("🔧 git-filter-repo 미설치, 직접 다운로드 시도...")
            script_path = download_git_filter_repo()
            return script_path is not None, script_path
    
    # n. Git 저장소 확인
    logging.debug("🔧 Git 저장소 상태 확인...")
    
    result = run_git_command("git rev-parse --is-inside-work-tree")
    if not result:
        logging.debug("🔧 Git 저장소가 아닙니다.")
        return False
    
    # 현재 브랜치 확인
    result = run_git_command("git rev-parse --abbrev-ref HEAD")
    if result:
        branch = result.stdout.strip()
        logging.debug(f"🔧 현재 브랜치: {branch}")
    else:
        branch = "main"
    
    # 원격 저장소 확인
    result = run_git_command("git remote get-url origin", check=False)
    if not result or result.returncode != 0:
        logging.debug("🔧 원격 저장소가 설정되지 않음")
    
    # n. 대용량 파일 탐지 (100MB 이상)
    logging.debug("🔧 대용량 파일 탐지 중...")
    
    def find_large_files(size_limit_mb=100):
        """대용량 파일 찾기"""
        large_files = []
        size_limit_bytes = size_limit_mb * 1024 * 1024
        
        # 현재 추적 중인 파일들 검사
        result = run_git_command("git ls-files", check=False)
        if result and result.stdout.strip():
            tracked_files = result.stdout.strip().split('\n')
            
            for file_path in tracked_files:
                file_path = file_path.strip()
                if file_path and Path(file_path).exists():
                    try:
                        file_size = Path(file_path).stat().st_size
                        if file_size > size_limit_bytes:
                            size_mb = file_size / (1024 * 1024)
                            large_files.append((file_path, size_mb))
                            logging.debug(f"🔧 대용량 파일 발견: {file_path} ({size_mb:.1f}MB)")
                    except Exception as e:
                        logging.debug(f"🔧 파일 크기 확인 실패: {file_path} - {e}")
        
        return large_files
    
    large_files = find_large_files()
    
    if large_files:
        logging.debug(f"🔧 총 {len(large_files)}개의 대용량 파일 발견")
        
        # .gitignore에 대용량 파일들 추가
        logging.debug("🔧 .gitignore 업데이트...")
        for file_path, size_mb in large_files:
            ensure_line_in_gitignore(file_path)
    else:
        logging.debug("🔧 100MB 이상의 대용량 파일이 없습니다")
    
    # .gitignore 변경사항 커밋
    run_git_command("git add .gitignore")
    result = run_git_command("git commit -m 'chore: ignore large files'", check=False)
    if result and result.returncode == 0:
        logging.debug("🔧 .gitignore 변경사항 커밋됨")
    else:
        logging.debug("🔧 .gitignore 변경사항 없음")
    
    # n. 추적 중인 대용량 파일 추적 해제
    if large_files:
        logging.debug("🔧 대용량 파일 추적 해제...")
        
        for file_path, size_mb in large_files:
            logging.debug(f"🔧 추적 해제: {file_path} ({size_mb:.1f}MB)")
            run_git_command(f"git rm --cached '{file_path}'", check=False)
        
        # 변경사항 커밋
        result = run_git_command("git commit -m 'chore: stop tracking large files'", check=False)
        if result and result.returncode == 0:
            logging.debug("🔧 대용량 파일 추적 해제 커밋됨")
    else:
        logging.debug("🔧 추적 해제할 대용량 파일 없음")
    
    # n. git-filter-repo 준비
    logging.debug("🔧 git-filter-repo 준비...")
    use_direct_script, filter_repo_path = check_git_filter_repo_available()
    
    if not use_direct_script and not filter_repo_path:
        logging.debug("🔧 git-filter-repo를 사용할 수 없습니다.")
        return False
    
    # n. Git GC 실행
    logging.debug("🔧 Git 정리...")
    run_git_command("git gc --prune=now --aggressive")
    
    # 6. 히스토리에서 대용량 파일 검사 및 제거
    logging.debug("🔧 Git 히스토리에서 대용량 파일 검사...")
    
    def find_large_files_in_unpushed_commits(size_limit_mb=100):
        """Push되지 않은 커밋에서만 대용량 파일 찾기"""
        history_large_files = []
        size_limit_bytes = size_limit_mb * 1024 * 1024
        
        # 원격 브랜치와 로컬 브랜치 차이 확인
        result = run_git_command(f"git rev-list --objects origin/{branch}..{branch}", check=False)
        if not result or not result.stdout.strip():
            # 원격 브랜치가 없거나 차이가 없으면 최근 10개 커밋만 검사
            logging.debug("🔧 원격 브랜치 차이 없음, 최근 10개 커밋만 검사...")
            result = run_git_command("git rev-list --objects -10 HEAD", check=False)
        else:
            logging.debug("🔧 Push되지 않은 커밋들에서 대용량 파일 검사...")
        
        if result and result.stdout.strip():
            objects = result.stdout.strip().split('\n')
            logging.debug(f"🔧 검사할 객체 수: {len(objects)}개")
            
            processed = 0
            for line in objects:
                line = line.strip()
                if line and ' ' in line:
                    # 객체 해시와 파일 경로 분리
                    parts = line.split(' ', 1)
                    if len(parts) == 2:
                        obj_hash, file_path = parts
                        
                        # 객체 크기 확인
                        size_result = run_git_command(f"git cat-file -s {obj_hash}", check=False)
                        if size_result and size_result.stdout.strip().isdigit():
                            obj_size = int(size_result.stdout.strip())
                            
                            if obj_size > size_limit_bytes:
                                size_mb = obj_size / (1024 * 1024)
                                history_large_files.append((file_path, size_mb, obj_hash))
                                logging.debug(f"🔧 히스토리 대용량 파일 발견: {file_path} ({size_mb:.1f}MB)")
                        
                        processed += 1
                        # 진행 상황 표시 (매 100개마다)
                        if processed % 100 == 0:
                            logging.debug(f"🔧 진행 상황: {processed}/{len(objects)} 객체 검사 완료...")
        
        return history_large_files
    
    history_large_files = find_large_files_in_unpushed_commits()
    
    # 현재 파일과 히스토리 파일 합치기 (중복 제거)
    all_large_files = large_files.copy()
    
    for hist_file, hist_size, hist_hash in history_large_files:
        # 이미 현재 파일 목록에 있는지 확인
        found = False
        for curr_file, curr_size in large_files:
            if curr_file == hist_file:
                found = True
                break
        
        if not found:
            all_large_files.append((hist_file, hist_size))
            logging.debug(f"🔧 히스토리 전용 대용량 파일 추가: {hist_file} ({hist_size:.1f}MB)")
    
    if all_large_files:
        logging.debug(f"🔧 총 {len(all_large_files)}개의 대용량 파일 발견 (현재: {len(large_files)}개, 히스토리: {len(history_large_files)}개)")
        logging.debug("🔧 대용량 파일 히스토리에서 제거...")
        
        # 히스토리에서 대용량 파일들 개별 제거 (안전한 방법)
        for file_path, size_mb in all_large_files:
            logging.debug(f"히스토리에서 제거 중: {file_path} ({size_mb:.1f}MB)")
            
            # git filter-branch로 개별 파일 제거
            cmd = f'git filter-branch --force --index-filter "git rm --cached --ignore-unmatch \\"{file_path}\\"" --prune-empty --tag-name-filter cat -- --all'
            result = run_git_command(cmd, check=False)
            
            if result and result.returncode == 0:
                logging.debug(f"🔧 {file_path} 히스토리에서 제거 완료")
            else:
                logging.debug(f"🔧 {file_path} 제거 실패, 계속 진행...")
        
        # filter-branch 정리
        logging.debug("🔧 히스토리 정리 작업...")
        run_git_command("git for-each-ref --format='delete %(refname)' refs/original | git update-ref --stdin", check=False)
        run_git_command("git reflog expire --expire=now --all", check=False)
        run_git_command("git gc --prune=now --aggressive", check=False)
        
        logging.debug("🔧 대용량 파일 히스토리 정리 완료")
    else:
        logging.debug("🔧 히스토리에서 제거할 대용량 파일이 없습니다")
    
    # 7. 강제 푸시 (원격 저장소가 있는 경우에만)
    logging.debug("🔧 원격 저장소 푸시 확인...")
    
    # 원격 저장소 재확인
    result = run_git_command("git remote get-url origin", check=False)
    if not result or result.returncode != 0:
        logging.debug("🔧 원격 저장소가 설정되지 않아 푸시를 건너뜁니다.")
        logging.debug("로컬 히스토리 정리는 완료되었습니다.")
        logging.debug("원격 저장소 설정 후 수동으로 푸시하세요: git push origin main --force")
    else:
        remote_url = result.stdout.strip()
        logging.debug(f"원격 저장소 확인: {remote_url}")

        # 안전한 강제 푸시 시도
        result = run_git_command(f"git push origin {branch} --force-with-lease", check=False)

        if result and result.returncode == 0:
            logging.debug("🔧 안전한 강제 푸시 성공")
        else:
            logging.debug("🔧 안전한 강제 푸시 실패, 일반 강제 푸시 시도...")
            result = run_git_command(f"git push origin {branch} --force", check=False)

            if result and result.returncode == 0:
                logging.debug("🔧 강제 푸시 성공")
            else:
                logging.debug("🔧 강제 푸시 실패")
                logging.debug("가능한 원인:")
                logging.debug("- 원격 저장소 푸시 권한 없음")
                logging.debug("- 브랜치 보호 규칙 설정됨")
                logging.debug("- 네트워크 연결 문제")
                logging.debug("수동 푸시 명령어: git push origin main --force")
                # 푸시 실패해도 로컬 정리는 성공했으므로 계속 진행

    # 8. 검증
    logging.debug("🔧 히스토리 검증...")
    if 'all_large_files' in locals() and all_large_files:
        result = run_git_command("git rev-list --objects --all", check=False)
        if result and result.stdout:
            remaining_large_files = []
            for file_path, size_mb in all_large_files:
                if file_path in result.stdout:
                    remaining_large_files.append(file_path)
            
            if remaining_large_files:
                logging.debug(f"🔧 일부 대용량 파일이 여전히 히스토리에 남아있을 수 있습니다: {remaining_large_files}")
            else:
                logging.debug("🔧 모든 대용량 파일이 히스토리에서 성공적으로 제거되었습니다")
        
        # 저장소 크기 변화 확인
        logging.debug("🔧 저장소 크기 확인...")
        result = run_git_command("git count-objects -vH", check=False)
        if result and result.stdout:
            logging.debug("저장소 통계:")
            for line in result.stdout.strip().split('\n'):
                if 'size-pack' in line or 'count' in line:
                    logging.debug(f"{line}")
    
    logging.debug("🔧 Git 대용량 파일 히스토리 정리 완료!")
    return True