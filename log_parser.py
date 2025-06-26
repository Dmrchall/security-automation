#!/usr/bin/env python3

import re
from datetime import datetime

LOG_FILE = "/var/log/auth.log"

def parse_auth_log(log_path):
    suspicious_events = []

    with open(log_path, "r") as f:
        for line in f:
            if "Failed password" in line or "authentication failure" in line:
                # Example line:
                # Jun 25 10:32:00 ubuntu sshd[12345]: Failed password for invalid user admin from 192.168.0.5 port 44222 ssh2
                suspicious_events.append(line.strip())

    return suspicious_events

def save_report(events):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"suspicious_logins_{timestamp}.txt", "w") as f:
        for event in events:
            f.write(event + "\n")
    print(f"[+] Report saved to suspicious_logins_{timestamp}.txt")

if __name__ == "__main__":
    print(f"[+] Parsing log file: {LOG_FILE}")
    events = parse_auth_log(LOG_FILE)
    print(f"[+] Found {len(events)} suspicious entries")

    for event in events:
        print(event)

    if events:
        save_report(events)

