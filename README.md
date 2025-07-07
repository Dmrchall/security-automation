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
