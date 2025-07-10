def test_subprocess_module_출력검증():
    from pkg_py.pk_core import cmd_to_os

    # output = cmd_to_os(cmd="echo test", mode='a', mode_with_window=0)

    output = cmd_to_os(cmd="echo test", mode_with_window=0)

    assert any("test" in line.lower() for line in output), "pk_tester: 출력에 'test'가 포함되어야 합니다."

