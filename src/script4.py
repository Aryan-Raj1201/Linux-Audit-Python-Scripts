import os

# Script 4: Log File Analyzer
# By: Aryan Raj

LOGFILE = "logfile.txt"
KEYWORD = "error"
COUNT = 0
matches = []

# If file does not exist, create it with sample log content
if not os.path.isfile(LOGFILE):
    with open(LOGFILE, "w") as f:
        f.write("INFO: System started successfully\n")
        f.write("WARNING: Low memory detected\n")
        f.write("ERROR: Disk not found\n")
        f.write("INFO: User login success\n")
        f.write("error: Failed login attempt\n")
        f.write("ERROR: Network disconnected\n")
        f.write("INFO: Backup completed\n")
        f.write("error: Unexpected shutdown\n")

    print(f"{LOGFILE} not found, so a sample logfile was created.\n")

# Read file line by line
with open(LOGFILE, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        if KEYWORD.lower() in line.lower():
            COUNT += 1
            matches.append(line.strip())

# Summary output
print(f"Keyword '{KEYWORD}' found {COUNT} times in {LOGFILE}")

# Last matching lines
print("\nLast 5 matching lines:")
for line in matches[-5:]:
    print(line)