import re
from collections import Counter

FAILED_LOGIN_THRESHOLD = 3


def extract_failed_logins(log_file):
"""Extract IP addresses from failed login attempts."""
failed_ips = []

try:
with open(log_file, "r", encoding="utf-8") as file:
for line in file:
if "failed" in line.lower():
ip_addresses = re.findall(
r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
line
)

failed_ips.extend(ip_addresses)

except FileNotFoundError:
print("\n[ERROR] Log file not found.")
return None

except PermissionError:
print("\n[ERROR] Permission denied.")
return None

return failed_ips


def analyze_logs(log_file):
"""Analyze failed login attempts and identify suspicious IPs."""

failed_ips = extract_failed_logins(log_file)

if failed_ips is None:
return

if not failed_ips:
print("\n[OK] No failed login attempts detected.")
return

attempts = Counter(failed_ips)

print("\n=== Failed Login Summary ===")

for ip, count in attempts.items():
print(f"{ip}: {count} failed attempt(s)")

print("\n=== Suspicious IP Addresses ===")

suspicious_found = False

for ip, count in attempts.items():
if count >= FAILED_LOGIN_THRESHOLD:
suspicious_found = True
print(
f"[WARNING] {ip} generated "
f"{count} failed login attempts."
)

if not suspicious_found:
print("[OK] No suspicious IP addresses detected.")


def main():
print("=== Security Log Analyzer ===")

log_file = input("Enter the path of the log file: ").strip()

analyze_logs(log_file)


if __name__ == "__main__":
main()
