![CI](https://github.com/Arsenoid2/process-report/actions/workflows/test.yml/badge.svg)

# 🧾 Process Reporter Tool

_This repository was created as part of a practical interview task._

To demonstrate different levels of usability and portability, the project includes **two versions** of a tool that generates detailed reports of running processes on a machine:

---

## 🟦 `single-platform/` – Zero Dependencies

Platform-specific tools written using native scripting languages. Detailed instructions and alternatives in [`single-platform/README.md`](./single-platform/README.md)

### 🔹 Windows
- `.bat` launcher that calls a PowerShell script to generate a process report in **CSV format**
- No dependencies required — runs on any modern Windows system
- Has limitaion of listing process user in the report

### 🍏 macOS
- `.sh` shell script using native **AppleScript dialogs** to export reports in **CSV or JSON**
- Fully self-contained; no external dependencies
- Also available as a ready-to-use native app in [GitHub Releases](https://github.com/Arsenoid2/process-report/releases/tag/v1.0.0)  
  ⬇️ [Download Process Reporter for macOS](https://github.com/Arsenoid2/process-report/releases/download/v1.0.0/Process.Reporter.zip)

---

## 🐍 `cross-platform/` – Python CLI Version

A flexible CLI tool built with Python that runs on **both Windows and macOS**.

### ✅ Features
- Reports: `pid`, `name`, `user`, `cpu_percent`, `memory_mb`
- Output formats: **CSV** or **JSON**
- Interactive prompts or CLI arguments
- One-click launchers:
  - `launcher.bat` for Windows
  - `launcher.command` for macOS
- Includes:
  - 🔁 CI pipeline via GitHub Actions
  - 🧪 Automated tests using `pytest`

Details in [`cross-platform/README.md`](./cross-platform/README.md)

---

## 📦 Infrastructure as Code

- The `IaC_ansible/` directory contains an [Ansible playbook](./IaC_ansible/playbook.yml) for automated setup and deployment of the Python version.
- Designed for Windows targets using remote PowerShell execution.

---

## 📖 How to Get Started

Choose one of the following:

- **No Python?** Use the scripts in [`single-platform`](./single-platform/) for quick results.
- **Python available?** Try the full-featured version in [`cross-platform`](./cross-platform/).

Each subfolder has its own `README.md` with platform-specific instructions.

Happy reporting and thanks for considering my candidacy! 📊