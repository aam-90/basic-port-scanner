import socket
from config import COMMON_SERVICES


def get_service_name(port):
    return COMMON_SERVICES.get(port, "Unknown")


def scan_port(host, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            return sock.connect_ex((host, port)) == 0

    except socket.gaierror:
        return False

    except socket.timeout:
        return False

    except socket.error:
        return False


def scan_ports(host, start_port, end_port, timeout=1):
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            if scan_port(host, port, timeout):
                service = get_service_name(port)

                print(
                    f"[OPEN] Port {port:<5} "
                    f"Service: {service}"
                )

                open_ports.append({
                    "port": port,
                    "service": service
                })

        except Exception as error:
            print(f"[ERROR] Port {port}: {error}")

    return open_ports