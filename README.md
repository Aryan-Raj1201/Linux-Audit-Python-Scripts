# 🐧 Linux Audit & Automation Scripts (Python + Bash)

A mini project containing **Linux auditing and automation scripts** converted from Bash to Python.  
This project demonstrates how common Linux administrative tasks can be automated using **Python scripting**, while still following the logic of real Linux shell scripting.

This is not just random scripts.
It is a practical Linux auditing toolkit built for system inspection and file-based reporting.

---

## 🚨 Why This Project Exists

Linux is widely used in:

- Servers
- Cloud infrastructure
- DevOps environments
- Cybersecurity systems
- Open-source development

A Linux user or administrator must regularly monitor:

- System identity
- Installed packages
- Directory permissions
- Storage usage
- Log files
- User configuration files

Instead of doing this manually every time, this project automates these tasks using scripting.

---

## 🎯 What This Project Does (At a Glance)

✔ Displays system identity information (kernel, user, uptime, distro, date)  
✔ Inspects whether a FOSS package is installed (Python3)  
✔ Audits important Linux directories (permissions, ownership, size)  
✔ Analyzes log files by counting keyword matches  
✔ Generates a personalized open-source manifesto and saves it in a file  
✔ Uses file handling to store outputs permanently  

This is not just scripting.
This is a basic Linux auditing toolkit.

---

## 🏗 System Architecture (High-Level)

User / Terminal Input
|
├── Script 1: System Identity Report
| ├── Kernel Version
| ├── Username
| ├── Uptime
| ├── Distro Details
| └── Date Output
|
├── Script 2: FOSS Package Inspector
| ├── Check package installed or not
| └── Print version + description
|
├── Script 3: Disk and Permission Auditor
| ├── Directory permissions + ownership
| ├── Directory size check
| └── Python executable location check
|
├── Script 4: Log File Analyzer
| ├── Keyword counting
| └── Display last 5 matches
|
└── Script 5: Open Source Manifesto Generator
├── Takes user input
└── Saves manifesto to a text file

---

## 📌 Scripts Included

---

### ✅ Script 1: System Identity Report
Displays system identity details using Linux system commands and Python libraries:

- Kernel version
- Current user
- Uptime
- Linux distribution info
- Current date

---

### ✅ Script 2: FOSS Package Inspector
Checks whether a package (Python3) is installed and displays:

- Installed status
- Version
- Maintainer
- Description

Also prints a short open-source package description.

---

### ✅ Script 3: Disk and Permission Auditor
Audits important Linux directories such as:

- `/etc`
- `/var/log`
- `/home`
- `/usr/bin`
- `/tmp`

For each directory, it reports:

- Permissions
- Owner and group
- Directory size

It also checks the system location of Python executable:

- `/usr/bin/python3`

---

### ✅ Script 4: Log File Analyzer
Reads a log file line by line and:

- Counts keyword occurrences (default: `"error"`)
- Displays the last 5 matching lines

Useful for quick log monitoring and debugging.

---

### ✅ Script 5: Open Source Manifesto Generator
Asks the user 3 questions and generates a personalized manifesto:

- Open-source tool you use
- Meaning of freedom (one word)
- Something you want to build and share freely

It saves the output into a text file:

`manifesto_<username>.txt`

---

## 📥 Inputs Expected

Depending on the script, user may provide:

- Package name (default python3)
- Directory list (pre-defined)
- Log file name + keyword
- Manifesto answers (tool, freedom, build idea)

---

## 📤 Outputs Generated

### 📄 Permanent File Outputs
- `manifesto_<username>.txt`
- `logfile.txt` (if Script 4 auto-generates sample log file)
- Report output printed directly in terminal

---

### 📌 Console Reports
- System identity report
- Directory audit report
- Package inspection details
- Log keyword summary

---

## 🛠️ Technologies Used

- Python 3
- Bash Scripting
- Linux System Commands (`uname`, `uptime`, `dpkg`, `ls`, `du`, `grep`)
- File Handling
- subprocess module
- platform module
- getpass module
- datetime module

---

## 📁 Project Structure

Linux-Audit-Toolkit/
│
├── system_identity.py
├── package_inspector.py
├── directory_auditor.py
├── log_analyzer.py
├── manifesto_generator.py
├── logfile.txt
├── manifesto_<username>.txt
└── README.md

### 🏆 Why This Project Stands Out

Most student Linux projects are:

❌ Basic
❌ Non-practical
❌ Only theory-based

This project is different because it includes:

✅ Real Linux auditing logic
✅ Practical automation scripts
✅ File-based reporting
✅ Strong use of conditions and loops
✅ Cross-platform Python scripting logic

This toolkit demonstrates real scripting skills used in:

Linux Administration
DevOps
Cybersecurity
System Auditing

### 🚀 Future Improvements

Planned upgrades:

Combine all scripts into one unified menu-based Linux toolkit
Export reports into CSV/PDF format
Add memory usage, CPU monitoring, and network monitoring scripts
Add cron job automation for scheduled audits
Add logging system for script outputs

### 📌 Resume Description (Recommended)

Linux Audit & Automation Toolkit (Python + Bash)
Developed a set of Linux auditing scripts to inspect system identity, installed packages, directory permissions, disk usage, and log file keyword analysis. Implemented file handling for persistent reporting and used subprocess-based automation to execute Linux shell commands through Python.

### 👤 Author

Aryan Raj
B.Tech — Artificial Intelligence & Machine Learning
VIT Bhopal University
Python Learner | Linux Scripting Enthusiast

### 🧾 Final Note

This project is not about writing random scripts.
It is about learning how Linux systems work and automating real tasks using:

Shell scripting logic
Python automation
File handling
Practical system auditing

Because automation is what separates a normal user from a real engineer.

