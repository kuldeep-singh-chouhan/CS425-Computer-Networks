from socket import *

# server details
serverName = 'localhost'
serverPort = 281

# server ready to receive
server_socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
server_socket.bind((serverName, serverPort))
server_socket.listen()
print ("The server", serverName,  "is ready to receive at port:",serverPort)

# wait for a client to connect
client_socket, client_address = server_socket.accept()
print('Client {} connected'.format(client_address))

# receive and send messages to/from the client
while True:
    # receive message from the client
    message = client_socket.recv(1024).decode()

    # print the message
    print('Client: {}'.format( message))

    # if the message is 'bye', close the connection    
    if message == 'bye':
        client_socket.close()
        break
    
    # send a response message to the client
    response_message = input('Server: ')
    client_socket.send(response_message.encode())

    # if the message is 'bye', close the connection
    if response_message == 'bye':
        client_socket.close()
        break

# close the server socket
server_socket.close()