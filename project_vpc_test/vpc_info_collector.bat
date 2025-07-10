chcp 65001
title %~nx0
@echo off
cls


:: test local to wsl
set IP_LOCAL=192.168.2.76
set IP_REMOTE=172.23.225.110
set USER_REMOTE=pk_system


:: 설정: IP 주소
@REM set IP_LOCAL=192.168.2.76
@REM set IP_REMOTE=192.168.10.11
@REM set USER_REMOTE=nvidia


:: run for local device (exec )
@REM python %~n0.py

:: 타겟 존재 확인
@REM dir c:\Users\%USERNAME%\Downloads\pk_system\vpc_info_collector_for_issue_tracking.py

@rem ssh 연결 확인
ssh %USER_REMOTE%@%IP_REMOTE%

@rem ssh 연결 pw없이 접속 설정
ssh-keygen -t rsa -b 4096
@REM ssh-copy-id %USER_REMOTE%@%IP_REMOTE% @rem fail Windows에서 ssh-copy-id를 사용하려면, Cygwin 또는 Git Bash 같은 도구를 설치필요, windows에 다른 도구를 설치하는 것보다는 wsl을 설치하고 linux 패키지 쓰는 것이 쉽게 가능 방법같아 보인다.
@REM ssh server에 접속해서 직접 ssh public key을 등록을 하면 된다 (자동화) # success #아무것도 설치하지 않고 성공
type "C:\Users\%USERNAME%\.ssh\id_rsa.pub" | ssh %USER_REMOTE%@%IP_REMOTE% "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys"
sudo sed -i 's/^#PubkeyAuthentication.*/PubkeyAuthentication yes/' /etc/ssh/sshd_config
cat /etc/ssh/sshd_config | grep PubkeyAuthentication
sudo systemctl restart ssh


:: move file to 전방 영상처리제어기
@REM rsync %IP_LOCAL%:./%~n0.py %IP_REMOTE%:~/Downloads # windows 에는 rsync 가 없다. 제어PC에서 wsl 써도 되는지 rsync 설치해도 되는지...안되면 robocopy 써야함.
@REM robocopy "\\%IP_LOCAL%\%USERPROFILE%\Downloads\pk_system" "\\%IP_REMOTE%\Users\username\Downloads" %~n0.py @rem windows->wsl 테스트 불가능
scp c:/Users/%USERNAME%/Downloads/[]/pk_system/%~n0.py %USER_REMOTE%@%IP_REMOTE%:~/home/%USER_REMOTE%/Downloads/ @rem windows 10 이상이면 Powershell에 scp 내장됨. # path unix style 로 converting 해야 사용 사능.
scp c:/Users/%USERNAME%/Downloads/[]/pk_system/vpc_info_collector_for_issue_tracking.py %USER_REMOTE%@%IP_REMOTE%:~/Downloads/ @rem # wsl 상으로 테스트를 하려니 경로도 달라진다.


:: (exec 권한 부여)
ssh %USER_REMOTE%@%IP_REMOTE% chmod 755 ~/Downloads/%~n0.py
@REM ssh %USER_REMOTE%@%IP_REMOTE% chmod 777 ~/Downloads/vpc_info_collector_for_issue_tracking.py
ssh %USER_REMOTE%@%IP_REMOTE% chmod 755 ~/Downloads/vpc_info_collector_for_issue_tracking.py


:: (exec  및 exec 결과 작성)
@REM ssh %USER_REMOTE%@%IP_REMOTE% "python ~/Downloads/%~n0.py > ~/Downloads/%~n0_log.txt 2>&1; echo $? > ~/Downloads/%~n0_exit_status.txt"
@REM $? : 최근에 exec 한 명령어의 종료 상태 코드
@REM 0  : 정상 종료
ssh %USER_REMOTE%@%IP_REMOTE% "python ~/Downloads/%~n0.py"
@REM ssh %USER_REMOTE%@%IP_REMOTE% "python3 ~/Downloads/vpc_info_collector_for_issue_tracking.py > ~/Downloads/vpc_info_collector_for_issue_tracking_log.txt 2>&1; echo $? > ~/Downloads/vpc_info_collector_for_issue_tracking_exit_status.txt"
ssh %USER_REMOTE%@%IP_REMOTE% "python3 ~/Downloads/vpc_info_collector_for_issue_tracking.py"  @rem wsl Ubuntu-24.04 에는 python3가 기본설치(3.12.x),  wsl Ubuntu-18.04 python 기본설치(2.7.x) # fail:원격지에서는 f.py exec 하면 f.txt 생성되는데 로컬에서 exec 하면 f.txt  생성 안됨.
ssh %USER_REMOTE%@%IP_REMOTE% "python3 ~/Downloads/vpc_info_collector_for_issue_tracking.py > ~/Downloads/vpc_info_collector_for_issue_tracking.txt"


:: run for remote device (exec 결과 이동 to local device)
rsync %USER_REMOTE%@%IP_REMOTE% ~/Downloads/%~n0.txt ./%~n0.txt
@REM rsync %USER_REMOTE%@%IP_REMOTE% ~/Downloads/vpc_info_collector_for_issue_tracking.txt ./vpc_info_collector_for_issue_tracking.txt
scp %USER_REMOTE%@%IP_REMOTE%:~/Downloads/vpc_info_collector_for_issue_tracking.txt c:/Users/%USERNAME%/Downloads/


:: (exec 결과 확인)
cd c:/Users/%USERNAME%/Downloads/
ssh %USER_REMOTE%@%IP_REMOTE% "tail -n 1  ~/Downloads/%~n0.txt"
ssh %USER_REMOTE%@%IP_REMOTE% "tail -n 1  ~/Downloads/vpc_info_collector_for_issue_tracking.txt"
type %~n0.txt
type vpc_info_collector_for_issue_tracking.txt



:: 타이머 시작 (최대 10초 동안 exec 결과 확인)
set /a "timeout=10"
set /a "elapsed_time=0"

:start_loop
timeout /t 10 >nul
set /a "elapsed_time+=10"

@REM echo $(ssh %USER_REMOTE%@%IP_REMOTE% "tail -n 1 ~/Downloads/vpc_info_collector_for_issue_tracking.txt")
@echo off
for /f "delims=" %%i in ('ssh %USER_REMOTE%@%IP_REMOTE% "tail -n 1 ~/Downloads/vpc_info_collector_for_issue_tracking.txt"') do (
@REM     echo %%i
    if ($?) {
        echo "0"
        goto :end_loop
    } else {
        echo "1"
        scp %USER_REMOTE%@%IP_REMOTE%:~/Downloads/vpc_info_collector_for_issue_tracking.txt c:/Users/%USERNAME%/Downloads/
        ssh %USER_REMOTE%@%IP_REMOTE% "tail -n 1 ~/Downloads/vpc_info_collector_for_issue_tracking.txt"
    }
)
if %elapsed_time% geq 10 (
    :: 10초 초과 시 종료
    echo 10초가 경과하여 종료합니다.
)
goto start_loop
:end_loop








