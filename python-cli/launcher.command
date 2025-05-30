#!/bin/bash
cd "$(dirname "$0")"
python3 proc_report_prompt.py
read -n 1 -s -r -p "Press any key to close..."