import nmap

def scan_ports(target, start_port, end_port):
    scanner = nmap.PortScanner()  # Create an instance of the PortScanner class

    try:
        # Iterate through the specified range of ports
        for port in range(start_port, end_port + 1):
            result = scanner.scan(target, str(port))  # Scan the target for the specified port
            state = result['scan'][target]['tcp'][port]['state']  # Get the port state
            print(f'Port {port}: {state.upper()}')
    
    except KeyError:
        print(f"No data found for target {target}. Is the IP address correct?")
    except nmap.PortScannerError as e:
        print(f"Nmap error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target = input("Enter the target IP address or hostname: ").strip()
    try:
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))

        if start_port > end_port:
            print("Invalid range: start port should be less than or equal to end port.")
        else:
            scan_ports(target, start_port, end_port)
    except ValueError:
        print("Invalid input: Ports must be integers.")
