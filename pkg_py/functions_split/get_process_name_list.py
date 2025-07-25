
"""
:param sort: True일 경우 알파벳 순 정렬
:param unique: True일 경우 중복 remove
:return: 프로세스 이름 리스트
continue
def get_process_name_list(unique: bool = True, sort: bool = True) -> list:
except (psutil.NoSuchProcess, psutil.AccessDenied):
for proc in psutil.process_iter(['name']):
if proc.info['name']:
if sort:
if unique:
import psutil
names = []
names = list(set(names))
names.append(proc.info['name'])
names.sort()
return names
try:
현재 실행 중인 모든 프로세스의 이름 목록을 반환합니다.
