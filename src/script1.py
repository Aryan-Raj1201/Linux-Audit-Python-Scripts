import platform
import getpass
import subprocess
from datetime import datetime

STUDENT_NAME = "Aryan Raj"
SOFTWARE_CHOICE = "Python"

KERNEL = platform.release()
USER_NAME = getpass.getuser()
DATE = datetime.now()

# Uptime (Windows + Linux)
try:
    if platform.system() == "Windows":
        # PowerShell command to get uptime in seconds
        uptime_seconds = subprocess.getoutput(
            'powershell "(get-date) - (gcim Win32_OperatingSystem).LastBootUpTime | select -ExpandProperty TotalSeconds"'
        )

        uptime_seconds = float(uptime_seconds)

        days = int(uptime_seconds // 86400)
        hours = int((uptime_seconds % 86400) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)

        UPTIME = f"up {days} days, {hours} hours, {minutes} minutes"

    else:
        UPTIME = subprocess.getoutput("uptime -p")

except:
    UPTIME = "Could not fetch uptime"

# Distro Info
try:
    if platform.system() == "Linux":
        DISTRO = subprocess.getoutput(
            "cat /etc/os-release | grep PRETTY_NAME | cut -d= -f2"
        ).replace('"', '')
    else:
        DISTRO = platform.platform()

except:
    DISTRO = "Could not fetch distro info"

print(f"Open Source Audit - {STUDENT_NAME}")
print(f"Kernel  : {KERNEL}")
print(f"User    : {USER_NAME}")
print(f"Uptime  : {UPTIME}")
print(f"Distro  : {DISTRO}")
print(f"Date    : {DATE}")
print("License : Linux kernel uses GPL v2")