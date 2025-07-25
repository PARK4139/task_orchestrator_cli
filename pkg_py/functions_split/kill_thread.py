
# 스레드 종료
# 종료할 스레드 이름
# 종료할 스레드 찾기
# 현재 exec  중인 모든 스레드 가져오기
break
current_threads = threading.enumerate()
def kill_thread(thread_name):
else:
for thread in current_threads:
if target_thread:
if thread.name == thread_name:
import threading
print(f"{thread_name} 스레드가 종료되었습니다.")
print(f"{thread_name} 스레드를 찾을 수 없습니다.")
target_thread = None
target_thread = thread
target_thread.join()
