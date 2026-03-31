import platform
import subprocess

# Script 2: FOSS Package Inspector
# By: Aryan Raj

PACKAGE = "python3"
system = platform.system()

if system == "Linux":
    # Linux dpkg check
    result = subprocess.run(["dpkg", "-l"], capture_output=True, text=True)

    if PACKAGE in result.stdout:
        print(f"{PACKAGE} is installed.")
        details = subprocess.getoutput(f"dpkg -s {PACKAGE} | grep -E 'Version|Maintainer|Description'")
        print(details)
    else:
        print(f"{PACKAGE} is not installed.")

elif system == "Windows":
    # Windows check python
    try:
        version = subprocess.getoutput("python --version")
        print("python is installed.")
        print("Version:", version)
    except:
        print("python is not installed.")

else:
    print("Unsupported OS")

# Package description
if PACKAGE == "python3":
    print("Python: community-driven language used worldwide")