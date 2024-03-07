import socket
import time

SERVER_IP = input("Server IP: ")
SERVER_PORT = 63204 # port used by the server

# create a socket object using IPv4 and TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Created socket.")

s.bind(('', SERVER_PORT + 1)) # bind socket
print("Binded socket.\n")

# connect to the server
s.connect((SERVER_IP, SERVER_PORT))
print("Connected to server.")


while True:
    data = input("Data to send to server: ")
    if not data:
        # if data is empty, stop the connection
        # send FIN packet to server
        s.shutdown(1)
        print("Sent closing signal.\n")
        break
    else:
        s.sendall(data.encode())
        print("Sent data to server.")

print("Closed client-side socket.")

# receive close signal (FIN packet) from server
s.recv(2048)
print("Received closing signal from server")

s.close()

