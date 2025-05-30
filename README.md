## 📄 PowerShell Version: simple-win-process-report.ps1
### ✅ Overview
This is a simple PowerShell script for Windows that generates a basic report of currently running processes. It captures key details like:
- Process ID (PID)
- Process Name
- CPU Time
- Memory Usage in Megabytes (MB)

The script saves this information to a CSV file named process_report.csv, which can be opened with spreadsheet applications like Microsoft Excel or Google Sheets.

### 📥 How to Download and Run
1. Download the Batch file
- Go to the project repository on GitHub.
- Click on __win-process-report.ps1__.
- Click “📥” icon (Download raw file),
- Save the file to a folder like Downloads or Documents.

2. Run the Batch file on Windows
- Double-click the saved file and choose where to save report file, or:

_Alternatively:_
- Open PowerShell and navigate to the folder where you want to place the report:
```powershell
cd Downloads  # or wherever you want to place the report.
```
- Execute the following command to generate the report:
```powershell
Get-Process | Select-Object Id, ProcessName, CPU,
@{Name="Memory (MB)";Expression={[math]::Round($_.WS / 1MB, 2)}} |
Export-Csv -Path process_report.csv -NoTypeInformation
```
- Allow Script Execution (if prompted)
If you see a security warning about script execution, run:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
This will temporarily allow the script to run without changing global system settings.

3. Output
The script creates a file called process_report.csv in the selected/same folder. You can open it using:
- Microsoft Excel
- Google Sheets
- LibreOffice Calc
- Or any text editor that supports CSV

### ⚖️ Pros and Limitations
✅ Advantages
- No external dependencies: Executes on any Windows system — no need to install Python or third-party tools.
- Quick and easy: Just download and run; ideal for non-technical users or quick checks.
- CSV output: Easily viewable in Excel, Google Sheets, or other spreadsheet tools.

⚠️ Limitations
- Windows-only: Not compatible with macOS or Linux.
- Basic metrics only: Does not include per-user breakdown or real-time CPU %.
- CSV only: No JSON support or advanced data formats.
