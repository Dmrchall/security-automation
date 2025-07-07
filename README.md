#Scripting for Security Automation

This repository contains Python scritpts to automate common cybersecurity tasks.

## Included Scripts
- 'port_scanner.py': Scans open ports using sockets or Nmap.
- 'log_parser.py': Parses system logs to identify suspicious activity.
- 'nmap_automation.py': Automates Nmap scans and generates simple reports.
- 'weak_password_checker.py': Checks for weak user passwords by comparing hashed entries to a wordlist.

## Tools Used
- Python
- Nmap
- Bash
- Splunk

## Author
DeMarco Hall

---
## port_scanner.py

Scans ports on a target host using either the built-in Python socket module or Nmap. It helps quickly identify services that are exposed on a network.

### How It Works

1. Accepts a target IP or hostname
2. Scans a range of ports
3. Optionally uses Nmap for faster/more accurate scanning
4. Outputs results in terminal or to a file

### How To Run
python3 port_scanner.py --target [host IP] --ports 1-1024

## log_parser.py

Parses system logs (e.g., var/log/auth.log) to detect potentially suspicious activity like brute-force login attempts or unauthorized access.

### How It Works

1. Reads a system lof file
2. Searches for suspicious patterns (e.g., failed login, sudo attempts)
3. Summarizes or highlights flagged lines

### How To Run

python3 log_parser.py --log /var/log/auth.log 

## nmap_automation.py

Automates Nmap scans and stores structured output for future analysis. Useful for running scheduled scans or organizing recon results.

### How It Works

1. Runs Nmap with user-specified flags
2. Parses and saves results (e.g., XML or grepable output)
3. Optionally generates basic reports

### How To Run

python3 nmap_automation.py --target [target IP] --scan-type full
## weak_password_checker.py

This script performs a password strength audit by comparing hashed passwords (from a shadow-like file) against a list of common weak passwords.

### Files Used

- `shadow.txt`: Contains `username:hashed_password` pairs
- `common_passwords.txt`: A list of plaintext passwords (wordlist)

### How It Works

1. Reads user hashes from `shadow.txt`
2. Hashes guesses using the same salt as the original
3. Compares each guess to the stored hash
4. Flags any matched password that is considered weak

### Weak Password Criteria

A password is marked weak if it:
- Is fewer than 8 characters
- Lacks uppercase or lowercase letters
- Lacks numbers
- Lacks special characters

### How to Run

```bash
python3 weak_password_checker.py
