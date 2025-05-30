import sys
import os
import time
import json
import csv
import psutil

def get_processes_info():
    # Initialize CPU tracking
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    time.sleep(1)

    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info']):
        try:
            info = proc.info
            mem_usage = info['memory_info'].rss / (1024 * 1024)
            processes.append({
                'pid': info['pid'],
                'name': info['name'] or 'N/A',
                'user': info.get('username') or 'N/A',
                'cpu_percent': info['cpu_percent'],
                'memory_mb': round(mem_usage, 2)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, KeyError):
            continue
    return processes

def save_report(data, format, output):
    with open(output, 'w', newline='', encoding='utf-8') as f:
        if format == 'csv':
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        elif format == 'json':
            json.dump(data, f, indent=4)

def prompt_for_format():
    print("THANKS FOR CONSIDERING MY CONDIDACY")
    print("This tool exports system processes information to a file.")
    print("Select output format:")
    print("1. CSV")
    print("2. JSON")
    choice = input("Type 1 or 2, then press Enter: ").strip()

    if choice == '1':
        return 'csv', 'process_report.csv'
    elif choice == '2':
        return 'json', 'process_report.json'
    else:
        print("❌ Invalid input. Please enter 1 or 2.")
        sys.exit(1)

def main():
    file_format, file_name = prompt_for_format()
    data = get_processes_info()

    if not data:
        print("⚠️ No process data found or access denied.")
        return

    save_report(data, file_format, file_name)
    print(f"✅ Report saved to: {os.path.abspath(file_name)}")

if __name__ == '__main__':
    main()
