![CI](https://github.com/Arsenoid2/process-report/actions/workflows/test.yml/badge.svg)

# __Process Reporter__ Tool

_This repository was created as an interview task report._

To demonstrate different scenarios and approaches, two variants for generating a detailed process report are implemented:

### 🟦 `single-platform` (zero dependencies)
* **Windows version**
    - Generates a CSV report and saves it to the specified folder
    - Implemented as a `.bat` script, ready to run
    - Additional PowerShell command provided in the subfolder's `README.md`
    - Provides basic visualization, but does _not_ list the user of each process
* **MacOS version**
    - Generates CSV or JSON report (user's choice) and saves it to the chosen location
    - Implemented as a `.sh` script; make it executable with:
    ```bash
    chmod +x /path/to/process-report/single-platform/MacOS/mac-process-report.sh
    ```
    - Also available as a ready-to-run application in [Releases](https://github.com/Arsenoid2/process-report/releases/tag/v1.0.0) ([download link](https://github.com/Arsenoid2/process-report/releases/download/v1.0.0/Process.Reporter.zip))
    - Provides enhanced visualization and lists all necessary metrics in the report

### 🐍 `cross-platform` (requires `psutil`, `pytest` optional)
- Python-based CLI tool with CSV/JSON output
- One-click launchers for Windows and Mac
- Optional visualization
- Automated tests

Additional features:
- Auto-deployment mechanism using Ansible (see the `ansible` folder for configurations and instructions)
- CI pipeline via GitHub Actions

## How to Use

Navigate to the relevant folder and follow the instructions in its `README.md`.