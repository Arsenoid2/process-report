# 🌐 Cross-Platform Process Report Tool

![CI](https://github.com/Arsenoid2/process-report/actions/workflows/test.yml/badge.svg)

This folder contains a Python-based CLI utility that generates detailed reports of running processes on both **Windows** and **macOS** systems. It is designed to be portable, accurate, and user-friendly — ideal for both end users and contributors.

---

## 🚀 Features

- ✅ Accurate reporting of:
  - Process ID (PID)
  - Process Name
  - Username
  - CPU usage (%)
  - Memory usage (MB)
- ✅ Supports **CSV** and **JSON** output
- ✅ Cross-platform (Windows & macOS)
- ✅ Minimal dependencies
- ✅ Automated tests included
- ✅ GitHub Actions CI pipeline

---

## 🐍 Requirements (dependencies)

- **Python 3.7+**
- **psutil** (required)
- **pytest** (recommended, for test runs)

---

## 💾 Dependencies Installation

Install `Python` and `psutil` (also `pytest` for automated test):

#### Windows:
```powershell
winget install --id Python.Python.3.13
pip install psutil
pip install pytest # optional
```

#### MacOS:
```bash
brew install python
pip3 install psutil --break-system-packages
pip3 install pytest --break-system-packages # optional
```
* ℹ️ For `brew` installation refer to [Homebrew](https://brew.sh/) website.

---

## 🧪 Running the Tool

For both **macOS** and **Windows**, you can run the tool either via one-click launchers or from the terminal. First download (git clone) the repository to you local machine then:

### 🖱️ Option 1: One-Click Launch

#### macOS
- Make the `launcher.command` executable:
    ```bash
    chmod +x dir/to/process-report/cross-platform/launcher.command # replace dir/to with actual dir
    ```
- Double-click the `launcher.command` file from finder,
- It will prompt you to choose an output format (CSV or JSON) and automatically generate the report in the current folder.

#### Windows
- Double-click the `launcher.bat` file.
- A command window will prompt you to choose the output format and generate the report in the same folder.

> 📌 These launcher files internally call `proc_report.py` with the correct Python environment and user prompts.

---

### 💻 Option 2: Run via Terminal / PowerShell

If you'd like to run it manually with arguments, open a terminal (or PowerShell) in the folder where the files are located and run:

```bash
python proc_report.py -f csv -o my_report.csv
python proc_report.py -f json -o my_report.json
```

If you omit the arguments, the script will enter interactive mode and ask you for output format.

> ✅ Reports include: `pid`, `name`, `user`, `cpu_percent`, `memory_mb`

---

## 🧪 Testing

To run the automated tests (requires `pytest`):

```bash
pytest test_proc_report.py
```

---

## 📂 Included Files

| File                | Purpose                                  |
|---------------------|------------------------------------------|
| `proc_report.py`     | Main CLI tool for collecting process info |
| `launcher.bat`       | Windows launcher for double-click usage  |
| `launcher.command`   | macOS double-click wrapper                |
| `test_proc_report.py`| Automated test suite                     |

---

## 🤖 CI Integration

This tool is continuously tested with [GitHub Actions](https://github.com/Arsenoid2/process-report/actions). The workflow validates:
- Script execution on Windows
- JSON output file creation
- Data structure correctness

---

## 💡 See Also

For simpler, platform-specific scripts, check the [`single-platform`](https://github.com/Arsenoid2/process-report/tree/c71788a9ecc9d8324de19608c725f202820376e9/Single-platform) version that requires no Python or setup.
