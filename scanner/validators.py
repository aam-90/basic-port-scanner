def validate_ports(start_port, end_port):
    if start_port < 1 or end_port > 65535:
        raise ValueError(
            "Ports must be between 1 and 65535."
        )

    if start_port > end_port:
        raise ValueError(
            "Start port cannot be greater than end port."
        )


def validate_timeout(timeout):
    if timeout <= 0:
        raise ValueError(
            "Timeout must be greater than 0."
        )