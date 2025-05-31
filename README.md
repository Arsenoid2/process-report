![CI](https://github.com/Arsenoid2/process-report/actions/workflows/test.yml/badge.svg)


# __Process Reporter__  Tool

_This repository is created as interview task report._

For better demonstration and capabilities created two implementations for generating a detailed process report.

### 🟦 `single-platform` (requires zero dependencies)
* Windows version
    - Generates CSV report to a folder by your choice
    - Based on native PowerShell execution and NOT requires any prerequisites
    - Implemented in `.bat` format and in ready-to-run state.
    - Has pure vizualization capability and not lists the user of the process.
* MacOS version
    - Generates CSV / JSON and saves to a folder all by your choice
    - Based on native bash execution and NOT requires any prerequisites
    - Created one-click application, stored in [Releases](https://github.com/Arsenoid2/process-report/releases) and can be dowloaded by [Process_Reporter_v1.0.0_Mac.zip](https://github.com/Arsenoid2/process-report/releases/download/v1.0.0/Process.Reporter.zip)
    - Additionally `.sh` command have been stored in the [single-platform](https://github.com/Arsenoid2/process-report/tree/main/Single-platform) folder


### 🐍 `cross-platform` (requires `psutil` and `pytest` (optional))
- Based on Python
- CLI tool with CSV/JSON output
- One-click lunchers for Win and Mac
- Optional visualizatoin
- Automated tests

Also for this variant created:
- Auto-deployment mechanism using Ansible and all the neccessary configurations and instructions are at \ansible folder.
- CI pipeline in the GitHub Actions

## How to Use

Go into the relevant folder and follow the instructions in its `README.md`.