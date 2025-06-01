# 🖥️ Single-Platform Process Report Tool

This folder contains standalone utilities tailored for specific platforms — **Windows** and **macOS** — to generate a process report without needing Python or any external dependencies. These are ideal for non-technical users or one-off use cases.

---

## 📄 Windows: `win-process-report.bat` (Double-click to run) / `win-process-report.ps1` (Execute in PowerShell/Command Prompt)

This tool provides a simple way to generate a report of currently running processes on Windows. It captures:

- Process ID (PID)
- Process Name
- CPU Time
- Memory Usage (in Megabytes)

The output is saved as a **CSV file**, viewable in Excel, Google Sheets, LibreOffice Calc, etc.

### 📥 How to Use

1. **Download** [`win-process-report.bat`](https://github.com/Arsenoid2/process-report/blob/e17a9c796b48fa9711a7f70aca37c4b675a6dfde/Single-platform/Windows/win-process-report.bat) from the repository.
2. **Double-click** it to run.
3. Choose where to save the report (you’ll be prompted).
4. Open the generated `process_report.csv` file using your preferred spreadsheet app.

> 💡 The `.bat` file internally calls PowerShell to execute the actual data collection (`win-process-report.ps1`).

### 🔧 Manual Alternative via PowerShell

If you prefer not to use the `.bat` file, then copy-paste the content of [`win-process-report.ps1`](https://github.com/Arsenoid2/process-report/blob/main/Single-platform/Windows/win-process-report.ps1) to PowerShell and run it.
If script execution is blocked, run this before execution of the script:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### ⚖️ Pros and Limitations

**✅ Advantages**
- No installation required — works out of the box on any modern Windows system.
- Simple CSV output for easy inspection.
- Ideal for quick checks or end-user environments.

**⚠️ Limitations**
- Windows-only.
- Does not include per-user attribution.
- CSV only — no JSON support.

---

## 🍎 macOS: `mac-process-report.sh`

This is an AppleScript-enhanced shell script designed for macOS. It uses native dialogs to prompt users for:
- Export format: **CSV** or **JSON**
- Output file location

It collects the following data:
- PID
- User
- Process Name
- CPU Time
- Memory Usage in MB

### 📥 How to Use

1. Download [`mac-process-report.sh`](https://github.com/Arsenoid2/process-report/blob/e17a9c796b48fa9711a7f70aca37c4b675a6dfde/Single-platform/MacOS/mac-process-report.sh).
2. Make it executable:
```bash
chmod +x ./mac-process-report.sh
```
3. Run the script by double-clicking it or from Terminal:
```bash
bash mac-process-report.sh
```
4. Choose format and destination via graphical dialogs.
5. Open the generated report file using:
   - Excel or Google Sheets (CSV)
   - Any JSON viewer or text editor (JSON)

### 💡 Tip: Create a macOS App

As mentioned in [README.md](https://github.com/Arsenoid2/process-report/blob/main/README.md), a user-friendly [Process Reporter v1.0.0_Mac](https://github.com/Arsenoid2/process-report/releases/download/v1.0.0/Process.Reporter.zip) MacOS app added in GitHub Releases and can be downloaded and run. If you prefer to build the app yourself, see [Build Instructions](./MacOS/build-instruction.md). You can create a native `.app` file using Automator that runs this script with double-click.

### ⚖️ Pros and Limitations

**✅ Advantages**
- No dependencies — uses macOS native tools.
- User-friendly UI dialogs.
- JSON or CSV support.

**⚠️ Limitations**
- macOS-only.

---

For advanced, cross-platform support, refer to the [`cross-platform`](./cross-platform/) version of this tool powered by Python.
