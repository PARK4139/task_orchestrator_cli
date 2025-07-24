# chcp 65001
# title %~nx0
# @echo off
# cls
 
# explorer.exe \\xxx.xxx.x.xx\30_vision_dev\ACU_NO\20_flash
# explorer.exe \\xxx.xxx.x.xx\30_vision_dev\ACU_NX\20_flash
# explorer.exe \\xxx.xxx.x.xx\30_vision_dev\Xavier_custom_board


import subprocess

# 파일 경로
paths = [
    r"\\xxx.xxx.x.xx\30_vision_dev\ACU_NO\20_flash",
    r"\\xxx.xxx.x.xx\30_vision_dev\ACU_NX\20_flash",
    r"\\xxx.xxx.x.xx\30_vision_dev\Xavier_custom_board"
]

# 각 경로에 대해 Explorer.exe 열기
for path in paths:
    subprocess.run(["explorer.exe", path])

