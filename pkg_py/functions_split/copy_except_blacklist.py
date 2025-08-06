from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def copy_except_blacklist(src_dir, dst_dir, exclude_names):
    import os

    from pathlib import Path
    import shutil
    from pkg_py.system_object.map_massages import PkMessages2025

    # 경로 객체로 변환
    src_dir = Path(src_dir).resolve()
    dst_dir = Path(dst_dir).resolve()

    # 자기 자신 복사 방지
    if src_dir == dst_dir or src_dir in dst_dir.parents:
        print(f"❌ 잘못된 경로: 복사 대상이 원본과 같거나 하위 디렉토리입니다.")
        return

    # 기본적인 시스템 무시 디렉토리
    auto_exclude_dirs = {'.git', '__pycache__', '.venv', '.venv_linux', 'node_modules'}
    exclude_names = set(exclude_names) | auto_exclude_dirs

    if not dst_dir.exists():
        dst_dir.mkdir(parents=True, exist_ok=True)

    copied_count = 0
    reserved_names = {'nul', 'con', 'prn', 'aux', 'lpt1', 'com1'}

    for root, dirs, files in os.walk(src_dir):
        root_path = Path(root)

        # 디렉토리 필터링
        dirs[:] = [d for d in dirs if d not in exclude_names]

        for file_name in files:
            if file_name in exclude_names:
                continue

            src_path = root_path / file_name

            # 경로 유효성 검사
            if not src_path.exists():
                print(f"[스킵] 존재하지 않는 경로: {src_path}")
                continue

            # 심볼릭 링크 무시 (옵션)
            if src_path.is_symlink():
                print(f"[스킵] 심볼릭 링크 무시: {src_path}")
                continue

            # 예약된 장치명 방어
            if src_path.name.lower() in reserved_names:
                print(f"[스킵] 예약된 장치명: {src_path}")
                continue

            # 위험한 문자 방어
            if any(c in src_path.name for c in ['\0', '/', '\\']):
                print(f"[스킵] 위험한 문자 포함: {src_path}")
                continue

            try:
                rel_path = src_path.relative_to(src_dir)
            except ValueError as e:
                print(f"[스킵] 상대 경로 계산 실패: {src_path} ({e})")
                continue

            dst_path = dst_dir / rel_path

            try:
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, dst_path)
                print(f"[COPIED] {rel_path}")
                copied_count += 1
            except Exception as e:
                print(f"[스킵] 복사 실패: {src_path} → {dst_path} ({e})")
                continue

    print(f"[{PkMessages2025.DONE}] {copied_count} file(s) copied to '{dst_dir}'.")
