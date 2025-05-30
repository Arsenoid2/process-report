# ☁️ Infrastructure as Code (IaC) – Ansible Deployment

You can provision a Windows machine with Python and the necessary dependencies using Ansible, which allows automated, repeatable setup without manual installation.

## 🛠️ Prerequisites
* A control machine (Linux/MacOS/WSL) with:
    * Python installed
    * Ansible installed:
    ```bash
    pip install ansible pywinrm
    ```
* A Windows target machine (Laptop, VM, etc.) with:
    * WinRM enabled (see [Microsoft doc](https://learn.microsoft.com/en-us/windows/win32/winrm/installation-and-configuration-for-windows-remote-management))
    * Administrator credentials

## 🧭 Setup Instructions
1. Clone this repository and navigate to the project folder:
```powershell
git clone https://github.com/Arsenoid2/process-report.git
cd process-report
```
2. Open ansible/inventory.ini and replace the example IP address and credentials:
3. Run the Ansible playbook from the project root:
```powershell
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml
```