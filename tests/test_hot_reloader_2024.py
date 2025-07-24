# tests/test_ensure_f_list_change_stable.py
import pytest
# from pkg_py.system_object.500_live_logic import ensure_f_list_change_stable
import os

class GetmtimeSeq:
    """
    순서대로 mtime 맵을 반환하도록 os.path.getmtime를 대체.
    maps: [{file1: t1, file2: t2}, {file1: t1', file2: t2'}, …]
    f_list_len: 한 맵당 파일 개수
    """
    def __init__(self, maps, f_list_len):
        self.maps = maps
        self.f_list_len = f_list_len
        self.flat_calls = 0
        self.map_index = 0

    def __call__(self, path):
        # 현재 mtime 반환
        val = self.maps[self.map_index][path]
        self.flat_calls += 1
        # 해당 맵의 호출이 끝나면 다음 맵으로 이동
        if self.flat_calls % self.f_list_len == 0 and self.map_index < len(self.maps) - 1:
            self.map_index += 1
        return val


@pytest.fixture(autouse=True)
def disable_side_effects(monkeypatch):
    monkeypatch.setattr('pkg_py.system_object.500_live_logic.get_pnx_os_style', lambda x: x)
    monkeypatch.setattr('os.path.exists', lambda path: True)
    monkeypatch.setattr('pkg_py.system_object.print_util.pk_print', lambda *args, **kwargs: None)
    monkeypatch.setattr('pkg_py.system_object.500_live_logic.pk_sleep', lambda secs: None)


def test_변경없을_때_True반환():
    f_list = ['file1', 'file2']
    # 두 번 모두 동일한 타임스탬프
    maps = [
        {'file1': 100, 'file2': 200},
        {'file1': 100, 'file2': 200},
    ]
    getmtime = GetmtimeSeq(maps, f_list_len=len(f_list))
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(os.path, 'getmtime', getmtime)

    result = ensure_f_list_change_stable(f_list, limit_seconds=0)
    assert result is True, "mtime이 변하지 않았으므로 안정적이어야 합니다"

    monkeypatch.undo()


def test_변경있을_때_False반환():
    f_list = ['file1', 'file2']
    # 두 번째 맵에서 file1만 변경
    maps = [
        {'file1': 100, 'file2': 200},
        {'file1': 150, 'file2': 200},
    ]
    getmtime = GetmtimeSeq(maps, f_list_len=len(f_list))
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(os.path, 'getmtime', getmtime)

    result = ensure_f_list_change_stable(f_list, limit_seconds=0)
    assert result is False, "mtime이 변경됐으므로 불안정이어야 합니다"

    monkeypatch.undo()

def test_불안정은_false(monkeypatch):
    # f_list, get_pnx_os_style, pk_print, pk_sleep, os.path.exists 등의 픽스처 세팅은 앞과 동일합니다.
    f_list = ['file1', 'file2']
    # 두 번째 체크에서 변경 발생
    maps = [
        {'file1': 100, 'file2': 200},
        {'file1': 150, 'file2': 200},
    ]
    getmtime = GetmtimeSeq(maps, f_list_len=len(f_list))
    monkeypatch.setattr(os.path, 'getmtime', getmtime)

    # limit_seconds=0 으로 즉시 리턴 경로로 진입
    assert not ensure_f_list_change_stable(f_list, limit_seconds=0)
