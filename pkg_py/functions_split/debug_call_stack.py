
def debug_call_stack():
for frame in inspect.stack()[1:5]:
print("[CALL STACK]")
print(f"  - {frame.function} @ {frame.filename}:{frame.lineno}")
