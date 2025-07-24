# pk_system

## Project Overview

**pk_system** is a multi-utility toolkit for automation, system management, data processing, AI, and multimedia, built on Python 3.12+.  
It runs in WSL, Docker, uv, and venv environments, supporting a wide range of file formats, system operations, networking, multimedia, natural language processing, automation, testing, and deployment features.

---

## Main Folder & File Structure

- **pkg_py/** : Core Python utilities for system/automation/data/AI/multimedia
  - **functions_split/** : Numerous single-purpose scripts for window/process/network/file/automation/translation/crawling, etc.
  - **system_object/** : Utilities for state management, file/directory/encoding/color/keymap, and other system objects
  - **refactor/** : Tools for code automation, refactoring, module/file renaming, and meta-programming
  - **workspace/** : Workspace management and integrated execution/state control
  - **Standalone scripts** : Various scripts for process/window/network/multimedia/automation/testing/deployment
- **tests/** : pytest-based unit/integration tests
- **docker-compose.yaml, *.Dockerfile** : Docker-based execution/deployment environments
- **pyproject.toml** : Project metadata, dependencies, build/packaging settings
- **Others** : Various data/media/document package directories (`pkg_csv`, `pkg_json`, `pkg_mp3`, etc. — be careful when publishing)

---

## Key Features

- **System/OS Management** : Process/window/network/env management, backup/restore, automation
- **Data Processing** : Supports CSV, JSON, XLSX, image, sound, video, and more
- **Multimedia** : Youtube download, video/audio processing, image conversion, etc.
- **Network/Web** : Integrations with Cloudflare, Selenium, Playwright, FastAPI, and more
- **AI/NLP** : ChatGPT, Konlpy, OCR, speech recognition, etc.
- **Automation/Utilities** : Batch file/dir/rename, hotkeys, GUI, tmux, venv, Docker, etc.
- **Testing/Deployment** : pytest-based tests, Git/Docker automation, deployment scripts

---

## Example Key Modules/Scripts

- **functions_split/**  
  - Window/process control, file/dir management, translation, crawling, automation, screenshot, networking, data transformation, etc.
- **system_object/**  
  - System state management, file/dir/encoding/color/keymap utilities
- **refactor/**  
  - Code automation, function/module splitting, batch renaming, meta-programming
- **workspace/**  
  - Workspace integration, execution/state management

---

## Installation & Usage

1. Prepare Python 3.12+ environment
2. Install dependencies using [uv](https://github.com/astral-sh/uv) (recommended)
   ```bash
   # Install uv if not already installed
   pip install uv

   # Install all dependencies as defined in pyproject.toml
   uv pip install -e .
   ```
   - 이 프로젝트는 전통적인 venv/pip 대신 uv를 사용하여 패키지 및 의존성을 관리합니다.
   - 반드시 uv로 설치 및 실행해 주세요.
3. (Optional) Docker environment  
   *Docker-based orchestration (docker-compose) is under development and not yet supported.*

---

## Testing

- pytest-based tests are provided in the `tests/` folder and scripts like `pk_test_tests.py`
- Example:
  ```bash
  pytest tests/
  ```

---

## Development/Contribution

- Refer to scripts in `pkg_py/` for each main feature
- See `pyproject.toml` for dependencies and environment settings
- Use automation/deployment/testing scripts as needed

---

## License

MIT (provisional, subject to change)

---

## Notes & Warnings

- When publishing, make sure to exclude sensitive data, credentials, session/log/media/document files, and internal/confidential materials using `.gitignore`
- For detailed features/terminology, refer to each script and `pyproject.toml`
- Supports release/tag management and multi-environment execution (Docker, WSL, venv, uv, etc.)
