# my_auto_utility

Custom Python and C++ utility toolkit for automating repetitive internal workflows.  
This project includes tools for file processing, automation scripts, and in-house deployment integration.

---

## Project Overview

`my_auto_utility` is a personal and internal-use utility suite built to automate routine tasks across engineering and operations. It includes Python scripts for workflow automation and optional C++ modules tested via CMake.

---

## Environment Setup

This project uses [`uv`](https://github.com/astral-sh/uv) for managing Python dependencies and environment.

### Python Setup

```bash
# Install uv (one-time)
curl -Ls https://astral.sh/uv/install.sh | sh

# Set up environment and install dependencies
uv venv
uv pip install -r pyproject.toml
