![CI](https://github.com/Arsenoid2/process-report/actions/workflows/test.yml/badge.svg)


# __Process Reporter__  Tool

_This repository is created as interview task report._

For demonstrating different scenarios and aproaches implemented two variants for generating a detailed process report:
### 🟦 `Single-platform` (requires zero dependencies)
* Windows version
    - Generates CSV report and saves to the asked folder
    - Implemented in `.bat` extension and in ready-to-run state
    - Additionally provided PowerShell command in [README.md]() of the subfolder
    - Has pure vizualization capability and _not lists_ the user of the process.
* MacOS version
    - Generates CSV / JSON report by your choice and stores where you choose
    - Implemented in `.sh` extension and must be premade executable by
    ```bash
    chmod +x /dir/to/process-report/single-platform/MacOS/mac-process-report.sh #replace /dir/to with actual direction
    ```
    - Additionally converted to the ready-to-run application, stored in [Releases](https://github.com/Arsenoid2/process-report/releases/tag/v1.0.0) and can be download by this [link](https://github.com/Arsenoid2/process-report/releases/download/v1.0.0/Process.Reporter.zip)
    - Has better vizualizatoin capability and lists all the neccessary metrics in report file


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