# Windows 권한 문제 해결 가이드

## 문제 상황
Windows에서 `ensure_pk_system_enabled.cmd` 실행 시 다음과 같은 권한 오류가 발생할 수 있습니다:
```
[Errno 13] Permission denied: 'C:\Users\wjdgn\Downloads\pk_system\pkg_windows\uv.exe'
[Errno 13] Permission denied: 'C:\Users\wjdgn\Downloads\pk_system\pkg_windows\fzf.exe'
```

## 해결 방법

### 1. 관리자 권한으로 실행 (권장)
```cmd
# 관리자 권한으로 실행되는 배치 파일 사용
pkg_windows\ensure_pk_system_enabled_admin.cmd
```

### 2. PowerShell을 관리자 권한으로 실행
1. 시작 메뉴에서 "PowerShell" 검색
2. "Windows PowerShell" 우클릭 → "관리자 권한으로 실행"
3. 다음 명령어 실행:
```powershell
cd C:\Users\wjdgn\Downloads\pk_system
python pkg_py\functions_split\ensure_pk_system_enabled.py
```

### 3. 명령 프롬프트를 관리자 권한으로 실행
1. 시작 메뉴에서 "cmd" 검색
2. "명령 프롬프트" 우클릭 → "관리자 권한으로 실행"
3. 다음 명령어 실행:
```cmd
cd C:\Users\wjdgn\Downloads\pk_system
python pkg_py\functions_split\ensure_pk_system_enabled.py
```

### 4. 대안 위치 사용
권한 문제가 지속되는 경우, 시스템이 자동으로 다음 위치에 설치를 시도합니다:
```
C:\Users\wjdgn\Downloads\uv.exe
C:\Users\wjdgn\Downloads\fzf.exe
```

## 예방 방법

### Windows Defender 설정
1. Windows Defender 보안 센터 열기
2. "바이러스 및 위협 방지" → "설정 관리"
3. "제외 항목 추가 또는 제거" → "제외 항목 추가"
4. 다음 폴더 추가:
   ```
   C:\Users\wjdgn\Downloads\pk_system\pkg_windows
   C:\Users\wjdgn\Downloads
   ```

### 바이러스 백신 설정
- 임시로 바이러스 백신을 비활성화하거나 예외 목록에 추가하세요
- 실시간 보호 기능을 일시적으로 끄고 설치 후 다시 켜세요

### 사용자 계정 제어(UAC) 설정
1. 제어판 → "사용자 계정" → "사용자 계정 제어 설정 변경"
2. 알림 수준을 "알림만 표시"로 설정
3. 설치 완료 후 원래 설정으로 복원

## 추가 도움말

### 문제가 지속되는 경우 다음을 확인하세요:
1. **Windows 업데이트 상태**: 최신 보안 업데이트 적용
2. **바이러스 백신 설정**: 예외 목록에 폴더 추가
3. **사용자 계정 권한**: 관리자 권한으로 실행
4. **디스크 공간**: 충분한 여유 공간 확보
5. **파일 잠금**: 다른 프로그램이 파일을 사용 중인지 확인

### 시스템 재부팅
권한 문제가 지속되면 시스템을 재부팅한 후 다시 시도하세요.

### 수동 설치
자동 설치가 실패하는 경우 다음 위치에서 수동으로 다운로드:
- UV: https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip
- FZF: https://github.com/junegunn/fzf/releases/latest/download/fzf-windows_amd64.zip

## 로그 확인
설치 과정에서 발생하는 오류는 다음 파일에서 확인할 수 있습니다:
```
C:\Users\wjdgn\Downloads\pk_system\pkg_log\
``` 