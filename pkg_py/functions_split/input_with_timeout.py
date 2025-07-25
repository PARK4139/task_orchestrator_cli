
def pk_input_with_timeout(str_working: str, timeout_secs: int = 9999) -> str | None:
def read_input():
except Empty:
from queue import Queue, Empty
import sys
import threading
input_queue = Queue()
input_queue.put(user_input.strip())
input_thread = threading.Thread(target=read_input, daemon=True)
input_thread.start()
print(str_working, end=" ", flush=True)
return None
return input_queue.get(timeout=timeout_secs)
try:
user_input = sys.stdin.readline()
