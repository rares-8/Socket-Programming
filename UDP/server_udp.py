import socket

HOST = "127.0.0.1"
PORT = 63204 # Port to listen on

# open the logging file for appending
loggingFile = open("server.log", "at")

# create a socket object using IPv4 and UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

loggingFile.write("\nCreated socket.\n")

s.bind(('', PORT)) # bind socket
loggingFile.write("Binded socket.\n")

while True:
    data, addr = s.recvfrom(2048) # receive data from the client

    # close connection if client send a newline character
    data = data.decode()
    if not data:
        # if data is empty, stop the connection
        break
    else:
        loggingFile.write(f"Received message from: {addr[0]}:{addr[1]}, data: \"{data}\".\n")

# Wait for a FIN from the client isn't needed in UDP, as it's a connectionless protocol
# So, there's no concept of closing the connection in UDP

loggingFile.write("Closing server-side socket.\n")
s.close()