import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#as e server we need to bind the socket to the server port
s.bind((socket.gethostname(), 12345))
#our queue will be 5 PCs
s.listen(5)
clientSocket, address = s.accept()
print(f"Connection from {address} has been established")

stop_word = "quit"
stop_word = stop_word + '\r\n'
f = open("client_text.txt", "w")
full_msg = ''

while True:
    msg = clientSocket.recv(1024)
    print(msg.decode("utf-8"))
    full_msg = msg.decode("utf-8")
    if full_msg == stop_word:
        clientSocket.close()
        f.close()
    f.write(full_msg)
    
