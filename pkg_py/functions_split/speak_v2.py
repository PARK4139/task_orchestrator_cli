
",")]  # from "abc,abc.abc,abc." to ["abc","abc","abc","abc"] # , or . 를 넣으면 나누어 읽도록 업데이트
# while not exit_event.is_set(): # 쓰레드 이벤트 제어
# 비동기 이벤트 루프 exec 할 쓰레드 설정 (simple for void async processing)
# 비동기 이벤트 루프 설정 (simple for void async processing)
PYGLET_PLAYER = None
PYGLET_PLAYER = pyglet.media.Player()
PYGLET_PLAYER.pause()
async def process_thread_speak(str_working):
asyncio.set_event_loop(loop)
def pk_speak_v2(str_working, comma_delay=1.00, thread_join_mode=False):
def process_thread_loop(ment):
def stop_all_sounds():
else:
ensure_do_exception_routine(traceback=traceback, exception=exception)
ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
except Exception as exception:
finally:
for player in playing_sounds:
for str_working in working_list:
from functools import partial
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.is_containing_special_characters_with_thread import is_containing_special_characters_with_thread
from pkg_py.functions_split.remove_special_characters import remove_special_characters
from pkg_py.functions_split.speak import pk_speak
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.etc import PLAYING_SOUNDS
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
func_n = inspect.currentframe().f_code.co_name
if PYGLET_PLAYER is not None:
if PYGLET_PLAYER.playing:
if is_containing_special_characters_with_thread(text=str_working):
if str_working == "":
if thread_join_mode == 1:
import asyncio
import inspect
import pyglet
import threading
import traceback
loop = asyncio.new_event_loop()
loop.run_until_complete(process_thread_speak(ment))
name="thread_for_speak")  # Q: 왜 thread.name 의 case 는 다른거야 ?  wrtn: 네, 스레드의 이름은 일반적으로 대소문자를 구분하지 않습니다.
pass
pk_speak(str_working, after_delay=comma_delay)
player.pause()  # 또는 player.stop()
playing_sounds = PLAYING_SOUNDS
return None
stop_all_sounds()
str_working = remove_special_characters(text=str_working)
str_working = str(str_working)
str_working = str_working.strip()
thread = threading.Thread(target=partial(process_thread_loop, str_working),
thread.join()
thread.start()
try:
while 1:
working_list = [x for x in working_list if x.strip()]  # 리스트 요소 "" remove,  from ["", A] to [A]
working_list = [x.strip() for x in str_working.replace(".", ",").split(
