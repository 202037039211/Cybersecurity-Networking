from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, gaierror
import time

def scan_ports(target_host, start_port=50, end_port=500):
    start_time = time.time()  # Record the start time of the scan

    try:
        # Resolve the target host's IP address
        target_ip = gethostbyname(target_host)
        print(f"\nStarting scan on host: {target_ip}")

        for port in range(start_port, end_port):
            # Create a socket and attempt to connect to the port
            with socket(AF_INET, SOCK_STREAM) as s:
                s.settimeout(0.5)  # Set a timeout for the connection attempt
                conn = s.connect_ex((target_ip, port))
                
                if conn == 0:  # Connection succeeded
                    print(f"Port {port}: OPEN")
        
        # Print the total time taken for the scan
        print("\nTime taken: {:.2f} seconds".format(time.time() - start_time))

    except gaierror:
        print("Error: Invalid hostname. Please check the target host address.")
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target = input("Enter host for scanning (e.g., google.com or 192.168.1.1): ").strip()
    scan_ports(target)
