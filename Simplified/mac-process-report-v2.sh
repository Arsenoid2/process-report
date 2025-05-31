#!/bin/bash

# Prompt user to choose export format: CSV or JSON
export_format=$(osascript <<EOT
choose from list {"CSV", "JSON"} with prompt "Choose the export format for the process report:" default items {"CSV"} without multiple selections allowed
EOT
)

# If user cancels the format selection, exit
if [ "$export_format" = "false" ] || [ -z "$export_format" ]; then
  [[ -t 1 ]] && echo "Export cancelled by user." && read -p "Press Enter to close this window."
  exit 0
fi

# Set default file name and format
if [[ "$export_format" == *JSON* ]]; then
  default_name="process_report.json"
  file_ext="json"
else
  default_name="process_report.csv"
  file_ext="csv"
fi

# Ask user where to save the file
file_path=$(osascript <<EOT
set defaultName to "$default_name"
set filePath to POSIX path of (choose file name with prompt "Save Process Report As" default name defaultName)
return filePath
EOT
)

# If user canceled the save dialog, exit
if [ -z "$file_path" ]; then
  [[ -t 1 ]] && echo "Report creation was cancelled." && read -p "Press Enter to close this window."
  exit 0
fi

# Ensure correct file extension
if [[ "$file_path" != *.$file_ext ]]; then
  file_path="$file_path.$file_ext"
fi

# Export process list to file
if [[ "$file_ext" == "csv" ]]; then
  echo "PID,User,ProcessName,CPUTime(s),Memory(MB)" > "$file_path"
  ps -axo pid,user,comm,time,rss | awk 'NR>1 {printf "%s,%s,%s,%s,%.2f\n", $1, $2, $3, $4, $5/1024}' >> "$file_path"
else
  echo "[" > "$file_path"
  ps -axo pid,user,comm,time,rss | awk 'NR>1 {
    printf "  {\x27PID\x27: %s, \x27User\x27: \"%s\", \x27ProcessName\x27: \"%s\", \x27CPUTime\x27: \"%s\", \x27MemoryMB\x27: %.2f},\n", $1, $2, $3, $4, $5/1024
  }' | sed '$ s/},/}/' >> "$file_path"
  echo "]" >> "$file_path"
fi

# Notify user
message="Report saved to: $file_path"

if [[ -t 1 ]]; then
  echo ""
  echo "$message"
  read -p "Press Enter to close this window."
else
  osascript -e "display notification \"${message//\"/\\\"}\" with title \"Process Report Created\""
fi

exit 0