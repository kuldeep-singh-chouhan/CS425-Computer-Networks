from socket import *

# server details to be connected to
serverName = 'localhost'
serverPort = 281

# connecting to server
client_socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
client_socket.connect((serverName, serverPort))
print("Connected to", serverName, "at port:", serverPort)

# send and receive messages to/from the server
while True:
    # send a message to the server
    message = input('Client: ')
    client_socket.send(message.encode())

    # if the message is 'bye', close the connection
    if message == 'bye':
        client_socket.close()
        break

    # receive a response message from the server
    response_message = client_socket.recv(1024).decode()

    # print the response message
    print('Server: {}'.format(response_message))

    # if the response message is 'bye', close the connection
    if response_message == 'bye':
        client_socket.close()
        break

# close the client socket
client_socket.close()