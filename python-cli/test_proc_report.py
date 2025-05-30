# test_proc_report.py
import os
import json
from proc_report import get_processes_info, save_report

def test_process_list():
    data = get_processes_info()
    assert isinstance(data, list)
    assert len(data) > 0, "Process list is empty"
    assert 'pid' in data[0]
    assert 'cpu_percent' in data[0]

def test_save_json(tmp_path):
    data = get_processes_info()
    output_file = tmp_path / "test_output.json"
    save_report(data, 'json', str(output_file))
    assert output_file.exists(), "Output file was not created"
    with open(output_file) as f:
        content = json.load(f)
    assert isinstance(content, list), "Output is not a JSON array"