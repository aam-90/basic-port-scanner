Basic TCP Port Scanner
Main Idea

This project is a basic TCP port scanner written in Python for learning and authorized testing.

A computer can run many network services at the same time. Each service may listen on a specific port. For example:

Port 22 — SSH
Port 80 — HTTP
Port 443 — HTTPS

The scanner attempts a TCP connection to each port in a selected range. If the connection succeeds, the port is reported as open. If it does not succeed, the port is not reported as open.

This project should only be used on systems and networks you own or have permission to test.

How It Works

The basic flow is:

User Command
     │
     ▼
main.py
     │
     ├── Validate input
     │
     ├── Resolve hostname to IP
     │
     ▼
tcp_scanner.py
     │
     ├── Scan each TCP port
     │
     ├── Check if connection succeeds
     │
     └── Identify known services
     │
     ▼
Results
     │
     ├── Terminal summary
     ├── JSON report
     └── CSV report



main.py → Runs the program and handles user input.

config.py → Stores default settings and service names.

scanner/ → Contains the main scanner modules.

tcp_scanner.py → Scans TCP ports and detects open ports.

reporter.py → Saves scan results as JSON or CSV.

validators.py → Validates port ranges and timeout values.

tests/ → Contains automated tests.

test_scanner.py → Tests scanner functions.

test_reporter.py → Tests report generation.

test_validators.py → Tests validation functions.
