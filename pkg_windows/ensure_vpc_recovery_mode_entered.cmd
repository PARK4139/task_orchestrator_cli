start "keep wsl session" wsl
timeout 14

안되겠음. 얘는 파이썬으로 구현해야함.
pause


start "1: usbipd list" wsl watch -n 0.3 usbipd.exe list
start "2: lsusb" wsl watch -n 0.3 lsusb
start "3: usbipd bind -b $BUSID" cls && usbipd bind -b $BUSID
start "4: usbipd attach --wsl --busid $BUSID --auto-attach" cls && usbipd attach --wsl --busid $BUSID --auto-attach
start "5: cd ~/flash/no_flash/Linux_for_Tegra" cmd.exe /k "wsl sudo find ~/flash -type f -name 'flash.sh'"

@REM start "sudo ./flash.sh -r -S 58GiB jetson-agx-xavier-industrial mmcblk0p1" wsl sudo ./flash.sh -r -S 58GiB jetson-agx-xavier-industrial mmcblk0p1
@REM start "sudo ./a2z_flash.sh a" wsl sudo ./a2z_flash.sh a    # this try is failed for "["
@REM  sudo ./flash.sh -r a2z-acuno-rp-5G mmcblk0p1

start "cd ~/flash/no_flash/Linux_for_Tegra/bootroader" wsl sudo find ~/flash -type f -name "system.img*"
@REM system.img 로 이름 변경
@REM a ~.img 로 이름 원복

@REM system.img 로 이름 변경
@REM b ~.img 로 이름 원복


@REM module-type   ( at vpc )

