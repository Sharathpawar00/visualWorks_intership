import socket
import sys


def check_port(host, port, timeout=3):
    """Return True when a TCP connection can be opened."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((host, port)) == 0


def read_inputs():
    host = input("Enter host/IP address (default: 127.0.0.1): ").strip()
    if not host:
        host = "127.0.0.1"

    while True:
        port_text = input("Enter port number: ").strip()
        try:
            port = int(port_text)
            if 1 <= port <= 65535:
                return host, port
            print("Port must be between 1 and 65535.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    if len(sys.argv) == 3:
        host = sys.argv[1]
        try:
            port = int(sys.argv[2])
        except ValueError:
            print("Error: port must be a number.")
            return 1

        if not 1 <= port <= 65535:
            print("Error: port must be between 1 and 65535.")
            return 1
    else:
        host, port = read_inputs()

    if check_port(host, port):
        print(f"Port {port} on {host} is open.")
    else:
        print(f"Port {port} on {host} is closed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
