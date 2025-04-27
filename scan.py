import socket

def scan_ports(ip, start_port, end_port):
    open_ports = []

    print(f"Scanning {ip} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # Set timeout for faster scanning
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            return
        except socket.error as err:
            print(f"Socket error: {err}")
            return

    if open_ports:
        print(f"\nOpen ports on {ip}: {open_ports}")
    else:
        print("\nNo open ports found.")

def main():
    try:
        ip = input("Enter the IP address to scan: ").strip()

        # Validate IP address
        socket.inet_aton(ip)

        start_port = int(input("Enter the start port: ").strip())
        end_port = int(input("Enter the end port: ").strip())

        # Validate port range
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            print("Invalid port range. Ports must be between 0 and 65535, and start <= end.")
            return

        scan_ports(ip, start_port, end_port)

    except ValueError:
        print("Invalid input. Ports must be integers.")
    except socket.error:
        print("Invalid IP address.")

if __name__ == "__main__":
    main()
