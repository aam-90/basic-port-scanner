import time
from datetime import datetime
VERSION = "1.0.0"
import argparse
import socket
from scanner.validators import (
    validate_ports,
    validate_timeout
)
from config import (
    DEFAULT_TIMEOUT,
    DEFAULT_START_PORT,
    DEFAULT_END_PORT
)

from scanner.tcp_scanner import scan_ports
from scanner.reporter import save_json, save_csv


def main():
    parser = argparse.ArgumentParser(
        description="Basic TCP Port Scanner for authorized testing"
    )

    parser.add_argument(
        "host",
        help="Target hostname or IP address"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}"
    )
    parser.add_argument(
        "--start-port",
        type=int,
        default=DEFAULT_START_PORT,
        help=f"Starting port (default: {DEFAULT_START_PORT})"
    )

    parser.add_argument(
        "--end-port",
        type=int,
        default=DEFAULT_END_PORT,
        help=f"Ending port (default: {DEFAULT_END_PORT})"
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT,
        help=f"Connection timeout in seconds (default: {DEFAULT_TIMEOUT})"
    )

    parser.add_argument(
        "--output",
        help="Save results to a JSON file"
    )
    parser.add_argument(
        "--csv",
        help="Save results to a CSV file"
     )
    args = parser.parse_args()

    try:
        validate_ports(
        args.start_port,
        args.end_port
    )

        validate_timeout(args.timeout)

    except ValueError as error:
        parser.error(str(error))

    try:
        target_ip = socket.gethostbyname(args.host)
    except socket.gaierror:
        print(f"[ERROR] Could not resolve host: {args.host}")
        return

    print("=" * 40)
    print("BASIC NETWORK PORT SCANNER")
    print("=" * 40)

    print(f"Target: {args.host}")
    print(f"Resolved IP: {target_ip}")
    print(f"Port range: {args.start_port}-{args.end_port}")
    print(f"Timeout: {args.timeout} seconds")
    print("-" * 40)
    

    scan_start_time = datetime.now()
    start_time = time.time()
    print(f"Scan started: {scan_start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)

    open_ports = scan_ports(
        target_ip,
        args.start_port,
        args.end_port,
        args.timeout
    )
    end_time = time.time()
    scan_end_time = datetime.now()

    duration = end_time - start_time
    print(f"Scan finished: {scan_end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Scan duration: {duration:.2f} seconds")

    
    if args.output:
        save_json(
            args.output,
            target_ip,
            open_ports
        )
    if args.output:
        save_json(
        args.output,
        target_ip,
        open_ports
        )

    if args.csv:
        save_csv(
        args.csv,
        target_ip,
        open_ports
        )
    print("-" * 40)
    print("SCAN SUMMARY")
    print("-" * 40)

    print(f"Target: {target_ip}")
    print(
        f"Ports scanned: "
        f"{args.end_port - args.start_port + 1}"
    )
    print(f"Open ports found: {len(open_ports)}")

    if open_ports:
        print("\nOpen ports:")

        for item in open_ports:
            print(
                f"  {item['port']:<6} "
                f"{item['service']}"
            )
    else:
        print("\nNo open ports found.")

    print("=" * 40)


if __name__ == "__main__":
    main()