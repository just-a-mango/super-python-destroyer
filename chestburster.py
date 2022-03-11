import time
import sys
import socket
import os
s = socket.socket()
host = "your-host-name"
port = 8080
s.connect((host,port))
print("")
print("Connected to the server.")

command = s.recv(1024)
command = command.decode(encoding='UTF-8')
if command == "shutdown":
    print("")
    print("Shutdown command")
    print("Command received")
    s.send(b'Command received. Shutting down...')
    import os
    os.system("shutdown /s /t 1")
