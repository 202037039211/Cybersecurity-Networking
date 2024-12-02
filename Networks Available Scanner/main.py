import subprocess

def scan_wifi_networks():
    try:
        # Execute the command to list available Wi-Fi networks (Windows-specific)
        nw = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
        
        # Decode the output from bytes to a string
        decoded_nw = nw.decode('ascii')
        
        # Print the decoded output
        print(decoded_nw)
    except subprocess.CalledProcessError as e:
        print("Error occurred while scanning networks:", e)
    except FileNotFoundError:
        print("The 'netsh' command is only available on Windows. This code will not work on other operating systems.")
    except Exception as e:
        print("An unexpected error occurred:", e)

# Call the function to scan networks
scan_wifi_networks()
