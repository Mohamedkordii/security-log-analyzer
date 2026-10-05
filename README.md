# Security Log Analyzer

A Python-based cybersecurity tool that analyzes authentication logs to detect repeated failed login attempts and identify potentially suspicious IP addresses.

## Features

- Analyzes authentication log files
- Detects failed login attempts
- Extracts IP addresses from log entries
- Counts failed attempts from each IP address
- Identifies suspicious IP addresses based on a defined threshold
- Helps demonstrate basic security monitoring and log analysis concepts

## How It Works

The program reads a log file and searches for failed login attempts. It extracts the associated IP addresses and counts how many failed attempts were made from each address.

If an IP address exceeds the defined threshold, it is flagged as potentially suspicious.

## Project Files

- `log_analyzer.py` — Main Python script used to analyze the logs
- `sample.log` — Sample authentication log used for testing
- `README.md` — Project documentation

## Requirements

- Python 3
- No external libraries required

## How to Run

Clone the repository or download the project files.

Run the analyzer using:

```bash
python3 log_analyzer.py
```

The script will analyze the sample log and display IP addresses associated with repeated failed login attempts.

## Example Use Case

This project demonstrates how basic log analysis can help identify repeated authentication failures that may indicate suspicious activity or attempted unauthorized access.

## Security & Ethical Use

This project is intended for educational and defensive cybersecurity purposes only. Use it only with systems, files, and data that you own or are authorized to analyze.

## Skills Demonstrated

- Python
- Cybersecurity fundamentals
- Log analysis
- Regular expressions
- IP address extraction
- Security monitoring
- Basic threat detection

## Author
Mohamed Kordi
Cybersecurity Engineering Student
