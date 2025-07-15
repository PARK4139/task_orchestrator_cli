# Project Description

`auto_utility` is a collaborative, modular Python-based automation toolkit designed to streamline development, testing, deployment, and system operations. This repository is structured to support **teamwork**, scalability, and consistent workflows across Windows, WSL, and Linux environments.

---

## 🤝 Purpose of This Repository

This project is built for **collaborative development**. Team members can:

- Reuse and extend modular scripts for automation
- Share consistent development environments using `uv`
- Maintain system setup and testing routines in one place
- Contribute via version-controlled Python, Bash, AHK, and batch scripts

It serves as a **shared toolbox** for rapid development, system configuration, testing, and deployment.

---

## 🛠️ Environment Setup

We use [`uv`](https://github.com/astral-sh/uv) to manage the virtual environment and dependencies.

### Quick Start

```bash
# Install uv (one-time)
curl -Ls https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv venv
uv pip install -r pyproject.toml
