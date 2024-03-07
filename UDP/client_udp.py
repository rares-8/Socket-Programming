import socket

SERVER_IP = input("Server IP: ")
SERVER_PORT = 63204 # port used by the server

# create a socket object using IPv4 and UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Created socket.")

s.bind(('', SERVER_PORT + 1)) # bind socket
print("Binded socket.\n")

while True:
    data = input("Data to send to server: ")
    # send data to the server
    s.sendto(data.encode(), (SERVER_IP, SERVER_PORT))
    if not data:
        # if data is empty, stop the connection
        print("Sent closing signal.\n")
        break
    else:
        print("Sent data to server.")

# Close socket. There's no need to send a FIN packet in UDP, because it's a connectionless protocol.
print("Closed client-side socket.")

# Receive close signal from server isn't needed in UDP, because it's a connectionless protocol
# So, there's no concept of closing the connection in UDP

s.close()