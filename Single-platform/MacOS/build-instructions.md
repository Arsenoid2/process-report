# 🛠️ Build Instructions: macOS Standalone App
As mentioned in [README.md](https://github.com/Arsenoid2/process-report/blob/main/README.md), [Process Reporter v1.0.0_Mac](https://github.com/Arsenoid2/process-report/releases/download/v1.0.0/Process.Reporter.zip) application for MacOS added in GitHub Releases, anyway following you can find the bulding instruction to create a fully standalone macOS `.app` version of the Process Reporting tool using the MacOS built-in __Automator__ app. This method avoids terminal usage and provides a double-clickable interface for non-technical users.

## 🔧 Step-by-Step: Create the App using Automator
1. Open Automator from Spotlight (Cmd + Space, then type "Automator").
2. Select New Document, choose Application as the document type and select Choose.
3. In the left panel, search for Run Shell Script, then drag it into the main workflow area.
4. Set Shell to /bin/bash, and Pass input to as arguments.
5. Open the file mac-process-report.sh from this repository and copy the entire script content.
6. Paste the script into the Run Shell Script action in Automator.
7. Save the app with a name like _Process Report.app_ in your Applications or Desktop folder.

App is ready. Double-click the app to run! It will prompt for export format and destination, and generate the report.

### ⚠️ Security Note: On first run, macOS may block the app. To allow it:
* Go to System Settings → Privacy & Security
* Click "Allow Anyway" under the security prompt for this app

### 📦 Optional: Create a ZIP for Distribution
If you want to share this app:
1. Right-click the .app you created.
2. Choose Compress "Process Report" to create a Process Report.zip.
You can then distribute this ZIP as a self-contained macOS utility.