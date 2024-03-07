import socket
import time

HOST = "127.0.0.1"
PORT = 63204 # Port to listen on

# open the logging file for appending
loggingFile = open("server.log", "at")

# create a socket object using IPv4 and TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

loggingFile.write("\nCreated socket.\n")

s.bind(('', PORT)) # bind socket
loggingFile.write("Binded socket.\n")

s.listen()
loggingFile.write("Listening on socket.\n")

loggingFile.write("Accepting requests.\n")
(clientConnection, clientAddress) = s.accept() # accept a connection from the client

loggingFile.write(f"Connection established. Client is: {clientAddress[0]}:{clientAddress[1]}.\n\n")

while True:
    data = clientConnection.recv(2048) # receive data from the client

    # close connection if server received a FIN packet
    data = data.decode()
    if not data:
        # if data is empty (FIN packet), stop the connection
        break
    else:
        loggingFile.write(f"Received message: \"{data}\".\n")

loggingFile.write("Received close signal from client.\n\n")

# send FIN to client
time.sleep(5)
clientConnection.shutdown(1)

loggingFile.write("Sent closing signal to client\n")
loggingFile.write("Closed server-side socket.\n")
clientConnection.close()
s.close()