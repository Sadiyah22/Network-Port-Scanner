Network Port Scanner (TCP Connect)
Overview
This tool is a multi-threaded network utility designed to discover active services on a target host. By scanning for open TCP ports, it helps identify potential entry points, a critical step in Vulnerability Assessment.

How it Works: The TCP Handshake
This scanner performs a "TCP Connect Scan." It attempts to complete the Three-Way Handshake with the target:

SYN: The scanner sends a synchronize packet.

SYN-ACK: If the port is open, the server responds.

ACK: The scanner completes the connection (proving the port is open) and then gracefully closes it.

Technical Features
Multi-threading: Implements the threading library to scan 1024 ports in seconds rather than minutes.

Error Handling: Uses socket.connect_ex to handle connection timeouts without crashing the program.

Learning Outcomes
Developed as part of my preparation for a September 2027 intake in Cybersecurity, this project provided hands-on experience with the OSI Model (Layer 4) and the practical security risks of leaving unnecessary services exposed to the internet.
