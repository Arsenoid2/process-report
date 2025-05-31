import sys
import os
import time
import json
import csv
import psutil
import argparse

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
            mem_info = info.get('memory_info')
            mem_usage = mem_info.rss / (1024 * 1024) if mem_info else 0
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
    print("THANKS FOR CONSIDERING MY CANDIDACY")
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

def safe_print_report_path(path):
    msg = f"Report saved to: {os.path.abspath(path)}"
    try:
        print(f"✅ {msg}")
    except UnicodeEncodeError:
        print(msg)

def main():
    parser = argparse.ArgumentParser(description='Generate a process report.')
    parser.add_argument('-f', '--format', choices=['csv', 'json'], help='Output format')
    parser.add_argument('-o', '--output', help='Output file name')
    args = parser.parse_args()

    if args.format and args.output:
        file_format = args.format
        file_name = args.output
    else:
        file_format, file_name = prompt_for_format()

    data = get_processes_info()
    if not data:
        print("⚠️ No process data found or access denied.")
        return

    save_report(data, file_format, file_name)
    safe_print_report_path(file_name)

if __name__ == '__main__':
    main()