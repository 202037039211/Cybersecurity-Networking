# Reverse Shell Implementation

This project demonstrates a basic reverse shell setup, where a client connects to a server to execute remote commands.

## Components:
- **Client Script:** Connects to the server and executes received commands.
- **Server Script:** Listens for incoming connections and sends commands.

## Prerequisites:
- Python 3.x

## Setup:
1. **Server:**
   - Run the server script on the machine that will control the client.
```bash
python server.py
```

2. **Client:**
   - Run the client script on the remote machine.
```bash
python client.py
```
   - Replace <server_IP_address> with your server's IP address.
