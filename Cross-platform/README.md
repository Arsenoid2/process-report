![CI](https://github.com/Arsenoid2/process-report/actions/workflows/test.yml/badge.svg)

## Multiplatfom solution
This implementation of the tool includes:
* Python based background,
* Can resolve CPU and Memory usage more accurately,
* Provides User information of the process,
* Multiplatform (Win & Mac),
* Easy and user-friendly flow,
* Including automated tests,
* Simple CI pipeline in GitHub Actions,

only mandatory dependancy for this project is __psutil__, that provides accurate CPU and Memory usage and lists the processes for all users on the machine. Also this approach is crossplatform and can be executed on both Windows and MacOS systems.
There is also recommended dependancy __pytest__, that is only used for automated test of the tool.
For installation __psutil__ and __pstest__ on the system must be preinstalled 🐍__python__ environment with it's __pip__ package manager. If you don't have, follow this first:

## Installation of __Python__ and __pip__ 
There are two ways for the installation:
1. Go to https://www.python.org/downloads/, download the appropriate package and install on the system,
2. CLI installation as follows:
### For Windows: from PowerSell or Command Prompt run:
```powershell
winget install Python.Python.3
```
Then restart the PS / CMD and verify installation:
```powershell
python --version
pip --version
```

### For Mac: from Terminal run
```bash
brew install python
```
_If you haven't installed brew yet, then send me your Mac as gift. I can use that better._

Then verify installation:
```bash
python3 --version
pip3 --version
```

## Installation of dependancies
For both Win and Mac run the following from the project folder in PowerShell/CMD/Terminal.
```powershell
pip install psutil
```
As mentioned before, to run automated tests, you’ll need pytest:
```powershell
pip install pytest
```
This is not required for end users — only for contributors or CI pipelines. The tests validate that:
* The process list is correctly generated
* The report file is created and well-formatted