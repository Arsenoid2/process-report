![CI](https://github.com/Arsenoid2/process-report/actions/workflows/test.yml/badge.svg)


# Process-Report CLI Tool

This repository contains two implementations for generating a detailed process report.

## Variants

### 🟦 `powershell-bat/` (Windows only, zero dependencies)
- Generates CSV report using native PowerShell from a `.bat` file.
- This varian NOT requires any prerequisites and in ready-to-run state.
- Has pure vizualization capability and not lists the user of the process.

### 🐍 `python-cli/` (Cross-platform, requires `psutil` and `pytest` (optional))
- CLI tool with CSV/JSON output
- One-click luncher for Win and Mac
- Optional visualizatoin
- Automated tests

Also for this variant created:
- Auto-deployment mechanism using Ansible and all the neccessary configurations and instructions are at \ansible folder.
- CI pipeline in the GitHub Actions

## How to Use

Go into the relevant folder and follow the instructions in its `README.md`.