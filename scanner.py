import socket
import threading
from datetime import datetime

# Configuration
target = "127.0.0.1" # Change this to your local IP or a target you own
print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Scanning started at: {str(datetime.now())}")
print("-" * 50)

def scan_port(port):
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # Timeout after 1 second
        
        # Returns 0 if connection is successful
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        s.close()
    except Exception:
        pass

# Scan common ports (1 to 1024) using threads for speed
for port in range(1, 1025):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
