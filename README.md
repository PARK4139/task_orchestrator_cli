# pk_system

## Author
Korean / Anyang / Jung hoon Park


## Project Overview

**pk_system** is a multi-utility toolkit for automation, system management, data processing, AI, and multimedia, built on Python 3.12+.  
It runs in WSL, Docker, uv, and venv environments, supporting a wide range of file formats, system operations, networking, multimedia, natural language processing, automation, testing, and deployment features.

### AI-Powered Development
This project leverages modern AI development tools to enhance productivity and code quality:

- **🖥️ [Cursor](https://cursor.sh/)**: Primary IDE with AI-powered code completion, refactoring, and intelligent assistance
- **🤖 [ChatGPT](https://chat.openai.com/)**: AI assistant for code generation, debugging, and architectural decisions
- **🧠 AI-Enhanced Workflow**: Iterative development using AI for rapid prototyping, testing, and optimization

The development process combines human expertise with AI capabilities to create robust, maintainable code while accelerating development cycles.

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

### Quick Start (Windows)
1. **Run the installation script**:
   ```cmd
   cd pk_system
   ensure_pk_system_enabled.cmd
   ```
   This script will:
   - Install and configure uv package manager
   - Install fzf for fuzzy finding
   - Set up Python virtual environment
   - Configure PATH environment variables
   - Create desktop shortcuts

### Manual Installation
1. Prepare a Python 3.12+ environment.
2. Install dependencies using [uv](https://github.com/astral-sh/uv) (recommended):
   ```bash
   # Install uv if not already installed
   pip install uv

   # Install all dependencies as defined in pyproject.toml
   uv pip install -e .
   ```
   - This project uses uv as the package and dependency manager instead of traditional venv/pip.
   - Please make sure to use uv for installation and execution.
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

## Project Structure & Naming Conventions

### File Naming Rules
- **`pk_` prefix files**: Call-only wrapper functions
  - **In `pkg_py/`**: Main entry point wrappers (e.g., `pk_ensure_chatGPT_responded.py`)
  - **In `functions_split/`**: Internal utility wrappers
  - Example: `pkg_py/pk_ensure_chatGPT_responded.py` → calls `functions_split/ensure_chatGPT_responded()`
- **`ensure_` prefix files**: Actual function implementations
  - **Location**: Must be in `functions_split/` folder
  - Example: `functions_split/ensure_chatGPT_responded.py` → contains `ensure_chatGPT_responded()` function
- **Function naming**: Functions should start with `ensure_` pattern

### Function Naming Patterns
This project actively uses three main function naming patterns for consistency and clarity:

#### **`ensure_` Pattern** - Guaranteed Execution
- **Purpose**: Ensures a specific state or condition is achieved
- **Behavior**: Performs actions to guarantee the desired outcome
- **Examples**:
  - `ensure_youtube_cookies_available()` - Guarantees YouTube cookies are ready
  - `ensure_potplayer_started()` - Ensures PotPlayer is running
  - `ensure_printed()` - Guarantees output is displayed
  - `ensure_colorama_initialized_once()` - Ensures colorama is initialized

#### **`get_` Pattern** - Data Retrieval
- **Purpose**: Retrieves or calculates data without side effects
- **Behavior**: Returns values without modifying system state
- **Examples**:
  - `get_youtube_video_metadata()` - Retrieves video information
  - `get_image_names_from_tasklist()` - Gets process list
  - `get_values_from_historical_file_routine()` - Reads historical data
  - `get_nx()` - Gets next identifier

#### **`set_` Pattern** - State Configuration
- **Purpose**: Configures or modifies system state
- **Behavior**: Changes settings or updates state
- **Examples**:
  - `set_window_title()` - Changes window title
  - `set_environment_variables()` - Configures environment
  - `set_database_values()` - Updates database entries

#### **Pattern Usage Guidelines**
- **`ensure_`**: Use when the function must succeed or handle failures gracefully
- **`get_`**: Use for pure data retrieval functions with no side effects
- **`set_`**: Use when explicitly modifying system state or configuration
- **Consistency**: Maintain these patterns across all new functions
- **Clarity**: The pattern immediately indicates the function's purpose and behavior

### Directory Structure
```
pkg_py/
├── functions_split/          # Core function implementations
│   ├── ensure_*.py          # Actual function implementations
│   ├── pk_*.py             # Internal utility wrappers
│   └── other_*.py          # Utility functions
├── pk_*.py                 # Main entry point wrappers
├── system_object/           # System state management
├── refactor/               # Code automation tools
└── workspace/              # Workspace management
```

### Installation Entry Point
- **Primary installation**: `ensure_pk_system_enabled.cmd` (Windows)
- **Automated setup**: Installs uv, fzf, Python venv, and configures PATH
- **Desktop shortcuts**: Creates launcher shortcuts for easy access

### File Organization Examples
```
# Main entry point (pkg_py/)
pkg_py/pk_ensure_chatGPT_responded.py
├── pk_ensure_chatGPT_responded()  # Main wrapper function
├── ask_simple_question()          # Convenience functions
└── ask_with_custom_prompt()       # Additional utilities

# Actual implementation (functions_split/)
pkg_py/functions_split/ensure_chatGPT_responded.py
├── ensure_chatGPT_responded()     # Core implementation (ensure_ pattern)
├── get_chat_history()             # Data retrieval (get_ pattern)
└── set_chat_settings()            # Configuration (set_ pattern)

# Pattern examples in functions_split/
pkg_py/functions_split/
├── ensure_youtube_cookies_available.py    # Guaranteed execution
├── get_youtube_video_metadata.py          # Data retrieval
├── set_window_title.py                    # State configuration
├── ensure_potplayer_started.py            # Guaranteed execution
├── get_image_names_from_tasklist.py       # Data retrieval
└── set_environment_variables.py           # State configuration
```

## Development/Contribution

### Development Environment
- **IDE**: [Cursor](https://cursor.sh/) with AI-powered assistance
- **AI Assistant**: [ChatGPT](https://chat.openai.com/) for code generation and debugging
- **Workflow**: AI-enhanced iterative development for rapid prototyping

### Development Guidelines
- Refer to scripts in `pkg_py/` for each main feature
- See `pyproject.toml` for dependencies and environment settings
- Use automation/deployment/testing scripts as needed
- Follow the naming conventions above for new functions

### AI-Enhanced Development Process
1. **🖥️ Cursor IDE**: Use AI-powered code completion and refactoring
2. **🤖 ChatGPT**: Leverage AI for complex logic, debugging, and optimization
3. **🧠 Iterative Development**: Combine human expertise with AI capabilities
4. **📝 Code Review**: AI-assisted code review and improvement suggestions
5. **🚀 Rapid Prototyping**: Use AI to accelerate feature development

### Best Practices
- **Human Oversight**: Always review and validate AI-generated code
- **Testing**: Ensure comprehensive testing of AI-assisted features
- **Documentation**: Maintain clear documentation for AI-enhanced components
- **Version Control**: Use proper Git workflow with AI-assisted commits

---

## License

MIT (provisional, subject to change)

---

## Notes & Warnings

- When publishing, make sure to exclude sensitive data, credentials, session/log/media/document files, and internal/confidential materials using `.gitignore`
- For detailed features/terminology, refer to each script and `pyproject.toml`
- Supports release/tag management and multi-environment execution (Docker, WSL, venv, uv, etc.)
