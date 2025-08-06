from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_project_info_from_pyproject():
    import toml
    from pkg_py.system_object.files import F_PYPROJECT_TOML
    from pathlib import Path

    try:
        pyproject_path = Path(F_PYPROJECT_TOML)

        if not pyproject_path.exists():
            # TODO : 파일이없다고 붉은 글자로 출력
            pass

        # pyproject.toml 읽기
        with open(pyproject_path, "r", encoding="utf-8") as f:
            config = toml.load(f)

        # project 섹션 추출
        if "project" in config:
            project_info = config["project"].copy()
            return project_info
        else:
            return None

    except Exception as e:
        return None
