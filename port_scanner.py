import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            sock.close()
        except Exception as e:
            print(f"Error on port {port}: {e}")

if __name__ == "__main__":
    host = input("Enter target IP or hostname: ")
    port_range = range(20, 1025)
    scan_ports(host, port_range)
