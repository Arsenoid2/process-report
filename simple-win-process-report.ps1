Get-Process | Select-Object Id, ProcessName, CPU,
@{Name="Memory (MB)";Expression={[math]::Round($_.WS / 1MB, 2)}} |
Export-Csv -Path process_report.csv -NoTypeInformation