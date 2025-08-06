# pk_system

## Author
Earth / Korean / Anyang / Jung hoon Park

## Project Overview

**pk_system** is a multi-purpose toolkit for automation, system management, data processing, AI, and multimedia based on Python 3.12+.  
It runs in WSL, Docker, uv, venv environments and supports various file formats, system operations, networking, multimedia, natural language processing, automation, testing, and deployment features.

### AI-Powered Development
This project leverages the latest AI development tools to enhance productivity and code quality:

- **🖥️ [Cursor](https://cursor.sh/)**: Primary IDE with AI-based code completion, refactoring, and intelligent assistance
- **🤖 [ChatGPT](https://chat.openai.com/)**: AI assistant for code generation, debugging, and architectural decisions
- **🧠 AI-Enhanced Workflow**: Iterative development using AI for rapid prototyping, testing, and optimization

The development process combines human expertise with AI capabilities to generate robust and maintainable code while accelerating the development cycle.

---

## 🚀 **Latest Project Status (2025-01-XX)**

### ✅ **Completed Major Projects**

#### **1. MSA Investment Advisory System** (`pkg_finance_invest_assist/`)
- **✅ Complete**: Docker + WSL environment setup, API Gateway, PostgreSQL + Redis integration
- **✅ Complete**: pyproject.toml + uv migration, dependency management modernization
- **🔄 In Progress**: Investment timing recommendation logic implementation
- **❌ Not Implemented**: News crawling, asset price monitoring, Django web interface

#### **2. Core System Tools**
- **✅ Complete**: System automation, process management, multimedia processing
- **✅ Complete**: AI integration (ChatGPT, OCR, speech recognition)
- **✅ Complete**: Network/web tools (Selenium, FastAPI, Cloudflare)

#### **3. Windows System Automation Improvements** (2025-01-XX)
- **✅ Complete**: Windows registry handle error fixes
- **✅ Complete**: Environment variable configuration improvements (`D_BUSINESS_DEMO` included)
- **✅ Complete**: UI/UX improvements (emoji removal, message cleanup)
- **✅ Complete**: UV, FZF installation and PATH configuration automation
- **✅ Complete**: Business Demo directory auto-creation

### 🎯 **Currently Developing Projects**

#### **MSA Investment Advisory System** - Phase 1 in Progress
- **Tech Stack**: FastAPI, Docker, PostgreSQL, Redis, WSL
- **Development Environment**: "Edit on Windows, Run on WSL" approach
- **Dependency Management**: uv + pyproject.toml (replacing requirements.txt)
- **API Status**: 
  - ✅ Gateway: `http://[WSL_IP]:8000/docs` (Swagger UI)
  - 🔄 Recommendation Engine: Investment timing analysis logic implementation
  - ❌ Finance API: External financial API integration needed
  - ❌ News Crawler: News collection and sentiment analysis needed

### 📋 **Next Steps Plan**

#### **Phase 1: Core API Implementation (Priority)**
1. **Investment Timing Recommendation Logic** - Technical indicator-based analysis algorithms
2. **Asset Price Queries** - External financial API integration (Yahoo Finance, Alpha Vantage, etc.)
3. **News Crawling** - News collection using BeautifulSoup/Selenium

#### **Phase 2-4: Advanced Features**
- Machine learning models and prediction algorithms
- Django web interface and user management
- Security system (JWT token-based)
- Monitoring and logging system

---

## Major Folders and File Structure

- **pkg_py/** : Core Python utilities for system/automation/data/AI/multimedia
  - **functions_split/** : Numerous single-purpose scripts for windows/process/network/file/automation/translation/crawling, etc.
  - **system_object/** : Utilities for state management, file/directory/encoding/color/keymap and other system objects
  - **refactor/** : Tools for code automation, refactoring, module/file name changes, meta programming
  - **workspace/** : Workspace management and integrated execution/state control
  - **Independent execution scripts** : Various scripts for process/window/network/multimedia/automation/testing/deployment
- **pkg_finance_invest_assist/** : **🆕 MSA Investment Advisory System** (latest project)
  - **api_gateway/** : FastAPI-based API Gateway
  - **investment_advisor/** : Investment recommendation engine
  - **market_data/** : Financial data API client
  - **news_analyzer/** : News crawling service
  - **shared/** : Common configuration and database modules
  - **deployment/** : Docker Compose and Nginx configuration
- **pkg_windows/** : **🆕 Windows System Automation Tools** (latest addition)
  - **ensure_pk_system_enabled.py** : Automatic UV, FZF, Python virtual environment installation and configuration
  - **Windows Registry Management** : Environment variable setup and PATH configuration
  - **System Automation** : Desktop shortcut creation, AutoRun registration
- **tests/** : pytest-based unit/integration tests
- **docker-compose.yaml, *.Dockerfile** : Docker-based execution/deployment environment
- **pyproject.toml** : Project metadata, dependencies, build/packaging configuration
- **Others** : Various data/media/document package directories (`pkg_cache_private`, `pkg_json`, `pkg_mp3`, etc. — caution when publishing)

---

## Major Features

- **System/OS Management** : Process/window/network/environment management, backup/restore, automation
- **Data Processing** : Support for CSV, JSON, XLSX, images, sound, video, etc.
- **Multimedia** : YouTube downloads, video/audio processing, image conversion, etc.
- **Network/Web** : Integration with Cloudflare, Selenium, Playwright, FastAPI, etc.
- **AI/NLP** : ChatGPT, Konlpy, OCR, speech recognition, etc.
- **Automation/Utilities** : Batch file/directory/name changes, hotkeys, GUI, tmux, venv, Docker, etc.
- **Testing/Deployment** : pytest-based tests, Git/Docker automation, deployment scripts
- **🆕 MSA Architecture** : Microservice-based investment advisory system through Docker orchestration
- **🆕 Windows Automation** : UV, FZF installation, environment variable setup, system configuration automation

---

## Major Modules/Scripts Examples

- **functions_split/**  
  - Window/process control, file/directory management, translation, crawling, automation, screenshots, networking, data conversion, etc.
- **system_object/**  
  - System state management, file/directory/encoding/color/keymap utilities
- **refactor/**  
  - Code automation, function/module splitting, batch name changes, meta programming
- **workspace/**  
  - Workspace integration, execution/state management
- **🆕 pkg_finance_invest_assist/**  
  - MSA Investment Advisory System: API Gateway, recommendation engine, financial data, news crawling
- **🆕 pkg_windows/**  
  - Windows System Automation: UV/FZF installation, environment variable setup, registry management

---

## Installation and Usage

### Quick Start (Windows)
1. **Run Installation Script**:
   ```cmd
   cd pk_system
   ensure_pk_system_enabled.cmd
   ```
   This script performs the following:
   - Install and configure uv package manager
   - Install fzf for fuzzy search
   - Set up Python virtual environment
   - Configure PATH environment variables
   - Create desktop shortcuts
   - Auto-create Business Demo directory

### Manual Installation
1. Prepare Python 3.12+ environment.
2. Use [uv](https://github.com/astral-sh/uv) to install dependencies (recommended):
   ```bash
   # Install uv if not installed
   pip install uv

   # Install all dependencies defined in pyproject.toml
   uv pip install -e .
   ```
   - This project uses uv as package and dependency manager instead of venv/pip.
   - Use uv for installation and execution.
3. (Optional) Docker environment  
   *Docker-based orchestration (docker-compose) is under development and not yet supported.*

### 🆕 **Windows System Automation (Latest Feature)**

#### **Automatic Installation and Setup**
```cmd
# Run system automation on Windows
cd pk_system
python pkg_windows/ensure_pk_system_enabled.py
```

This script automatically performs:
- **UV Package Manager** installation and validation
- **FZF Fuzzy Search Tool** installation and validation
- **Python Virtual Environment** setup and PATH configuration
- **Business Demo Directory** auto-creation
- **Environment Variable Setup** (including `D_BUSINESS_DEMO`)
- **Desktop Shortcut** creation
- **AutoRun Registration** (command prompt auto-execution)

#### **Setup Verification**
```cmd
# Check installed tools
uv --version
fzf --version
python --version

# Check environment variables
echo %PATH%
echo %D_BUSINESS_DEMO%
```

### 🆕 **MSA Investment Advisory System Execution (WSL Environment)**

#### **1. WSL Environment Setup**
```bash
# Move to project directory in WSL
cd /mnt/c/Users/user/Downloads/pk_system/pkg_finance_invest_assist

# Docker permission setup
sudo usermod -aG docker $USER
newgrp docker
```

#### **2. MSA Service Execution**
```bash
# Start all services (PostgreSQL, Redis, Gateway, recommendation engine, etc.)
./scripts/docker_uv_sync.sh

# Or test individual services
./scripts/wsl_quick_test.sh
```

#### **3. API Testing**
```bash
# Check WSL IP
wsl hostname -I

# Access Swagger UI from Windows browser
explorer.exe http://[WSL_IP]:8000/docs
```

---

## Testing

- pytest-based tests are provided in `tests/` folder and scripts like `pk_test_tests.py`
- Example:
  ```bash
  pytest tests/
  ```

### 🆕 **Windows System Automation Testing**
```cmd
# System setup verification
python pkg_windows/ensure_pk_system_enabled.py

# Individual tool testing
uv --version
fzf --version
```

### 🆕 **MSA API Testing**
```bash
# API Gateway status check
curl "http://[WSL_IP]:8000/"

# Investment timing recommendation test (in implementation)
curl "http://[WSL_IP]:8000/api/v1/recommend/invest-timing?asset_name=Samsung"
```

---

## Project Structure and Naming Conventions

### File Naming Rules
- **`pk_` prefix files**: Call-only wrapper functions
  - **In `pkg_py/`**: Major entry point wrappers (e.g., `pk_ensure_chatGPT_responded.py`)
  - **In `functions_split/`**: Internal utility wrappers
  - Example: `pkg_py/pk_ensure_chatGPT_responded.py` → calls `functions_split/ensure_chatGPT_responded()`
- **`ensure_` prefix files**: Actual function implementation
  - **Location**: Must be in `functions_split/` folder
  - Example: `functions_split/ensure_chatGPT_responded.py` → contains `ensure_chatGPT_responded()` function
- **Function naming**: Functions must start with `ensure_` pattern

### Function Naming Patterns
This project actively uses three major function naming patterns for consistency and clarity:

#### **`ensure_` Pattern** - Guaranteed Execution
- **Purpose**: Ensure specific state or condition is achieved
- **Action**: Perform work to guarantee desired results
- **Examples**:
  - `ensure_youtube_cookies_available()` - Ensure YouTube cookies are prepared
  - `ensure_potplayer_started()` - Ensure PotPlayer is running
  - `ensure_printed()` - Ensure output is displayed
  - `ensure_colorama_initialized_once()` - Ensure colorama is initialized

#### **`get_` Pattern** - Data Retrieval
- **Purpose**: Retrieve or calculate data without side effects
- **Action**: Return values without modifying system state
- **Examples**:
  - `get_youtube_video_metadata()` - Retrieve video information
  - `get_image_names_from_tasklist()` - Get process list
  - `get_values_from_historical_file_routine()` - Read history data
  - `get_nx()` - Get next identifier

#### **`set_` Pattern** - State Configuration
- **Purpose**: Configure or modify system state
- **Action**: Change settings or update state
- **Examples**:
  - `set_window_title()` - Change window title
  - `set_environment_variables()` - Environment configuration
  - `set_database_values()` - Update database entries

#### **Pattern Usage Guidelines**
- **`ensure_`**: Use when function should succeed or handle failure gracefully
- **`get_`**: Use for pure data retrieval functions without side effects
- **`set_`**: Use when explicitly modifying system state or configuration
- **Consistency**: Maintain this pattern in all new functions
- **Clarity**: Pattern immediately indicates function purpose and action

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

🆕 pkg_finance_invest_assist/  # MSA Investment Advisory System
├── api_gateway/                # API Gateway (FastAPI)
├── investment_advisor/         # Investment recommendation engine
├── market_data/               # Financial data API
├── news_analyzer/             # News crawling service
├── shared/                    # Common modules
├── deployment/                # Docker configuration
└── scripts/                   # Execution scripts

🆕 pkg_windows/                # Windows System Automation
├── ensure_pk_system_enabled.py # UV/FZF installation and configuration
├── Registry Management Tools
└── System Automation Scripts
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

🆕 # MSA Investment Advisory System example
pkg_finance_invest_assist/
├── api_gateway/main.py               # API Gateway (FastAPI)
├── investment_advisor/main.py         # Investment recommendation service
├── market_data/main.py               # Financial data service
├── news_analyzer/main.py             # News crawling service
└── shared/config.py                  # Common configuration

🆕 # Windows System Automation example
pkg_windows/
├── ensure_pk_system_enabled.py       # UV/FZF installation and configuration
├── Registry Management Functions
└── System Automation Tools
```

## Development/Contribution

### Development Environment
- **IDE**: AI-powered assistance available in [Cursor](https://cursor.sh/)
- **AI Assistant**: [ChatGPT](https://chat.openai.com/) for code generation and debugging
- **Workflow**: AI-enhanced iterative development for rapid prototyping
- **🆕 MSA Development**: "Edit on Windows, Run on WSL" approach
- **🆕 Windows Automation**: UV, FZF installation, environment variable setup

### Development Guidelines
- Refer to scripts in `pkg_py/` for each main feature
- See `pyproject.toml` for dependencies and environment settings
- Use automation/deployment/testing scripts as needed
- Follow the naming conventions above for new functions
- **🆕 MSA Guidelines**: 
  - Develop each microservice independently
  - Communication through API Gateway
  - Manage entire environment with Docker Compose
- **🆕 Windows Automation Guidelines**:
  - Use `with` block for registry operations
  - Broadcast notification after environment variable changes
  - Remove unnecessary emojis from UI messages

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
- **🆕 MSA Best Practices**:
  - Independent testing for each service
  - API documentation (Swagger UI)
  - Docker image optimization
  - Environment-specific configuration separation
- **🆕 Windows Automation Best Practices**:
  - Pay attention to registry handle management
  - Recommend checking in a new terminal after environment variable changes
  - UV installation requires internet connection

---

## License

MIT (provisional, subject to change)

---

## Notes & Warnings

- When publishing, make sure to exclude sensitive data, credentials, session/log/media/document files, and internal/confidential materials using `.gitignore`
- For detailed features/terminology, refer to each script and `pyproject.toml`
- Supports release/tag management and multi-environment execution (Docker, WSL, venv, uv, etc.)
- **🆕 MSA Notes**: 
  - WSL IP address may change on restart
  - Docker containers run only in WSL environment
  - Access from Windows browser using WSL IP required
- **🆕 Windows Automation Notes**:
  - Registry operations may require administrator privileges
  - Recommend checking in a new terminal after environment variable changes
  - UV installation requires internet connection
