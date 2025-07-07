#!/usr/bin/env python3

import crypt
import re

with open("shadow.txt", "r") as f:
    hash_entries = [line.strip() for line in f if line.strip()]

with open("common_passwords.txt", "r") as f:
    test_passwords = [line.strip() for line in f if line.strip()]

def is_weak(password):
    return (
        len(password) < 8 or
        not re.search(r"[A-Z]", password) or
        not re.search(r"[a-z]", password) or
        not re.search(r"[0-9]", password) or
        not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    )

found_weak = False

for entry in hash_entries:
    try:
        username, hash_line = entry.split(":", 1)
    except ValueError:
        continue

    for guess in test_passwords:
        if crypt.crypt(guess, hash_line) == hash_line:
            if is_weak(guess):
                print(f"[⚠️] Weak password detected for {username}: {guess}")
                found_weak = True
            break

if not found_weak:
    print("No weak passwords detected.")
