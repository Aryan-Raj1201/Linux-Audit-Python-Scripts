import os
import subprocess

# Script 3: Disk and Permission Auditor
# By: Aryan Raj

STUDENT_NAME = "Aryan Raj"

DIRS = ["C:\\Windows", "C:\\Users", "C:\\Program Files", "C:\\Temp"]

print(f"Directory Audit Report - {STUDENT_NAME}")

for DIR in DIRS:
    if os.path.isdir(DIR):
        size_info = subprocess.getoutput(f'powershell "(Get-ChildItem \'{DIR}\' -Recurse -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum/1GB"')
        print(f"{DIR} => Size (Approx in GB): {size_info}")
    else:
        print(f"{DIR} does not exist on this system")

# Check Python location
python_path = subprocess.getoutput("where python")

if python_path:
    print("\nPython Executable Location Found:")
    print(python_path)
else:
    print("\nPython location not found")