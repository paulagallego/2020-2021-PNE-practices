import socket
import termcolor
import server_utils
list_sequences = ["ACGTAAAAGTTTAAGCGCCAAT", "AGTCCCCCCAAAATTTTGGGGGAATAT", "AGAGAGAGGATTATTATATACTCTTC", "GGGGGGGGGGGTTTTTTTTTAAAAAACCCC", "AAAAAATTTTTCGAAAAAAA"]

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8081
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()
count = +1

print("The server is configured!")
client_address_list = []
count_connections = 0

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:

        (cs, client_ip_port) = ls.accept() #count connections always after accept
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION " + str(count_connections) + ".Client IP, PORT: " + str(client_ip_port))


    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()
    msg_raw = cs.recv(2048)
    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()

    formatted_message = server_utils.format_command(msg)
    formatted_message = formatted_message.split(" ")

    # -- Execute this part if there are no errors
    # -- Read the message from the client
    # -- The received message is in raw bytes

    if len(formatted_message) == 1:
        command = formatted_message[0]
    else:
        command =formatted_message[0]
        argument = formatted_message[1]


    #if formatted_message == 'PING':
        #server_utils.ping()
    if command == "PING":
        server_utils.ping(cs)
    # -- Send a response message to the client
    #try is used to avoid the server to stop when something not transformable into an integer is introduced
        #response = "OK!"
    # -- The message has to be encoded into bytes
        #cs.send(str(response).encode()) # the int is back to a str and encoded into bytes by .encode and sent back to client
    elif command == "GET":
        server_utils.get(cs, list_sequences, argument)
    elif command == "INFO":
        server_utils.info(cs, argument)

    elif command == "COMP":
        server_utils.comp(cs, argument)

    elif command == "REV":
        server_utils.rev(cs, argument)

    elif command == "GENE":
        server_utils.gene(cs, argument)

    else:
        response = "Not available command"
        termcolor.cprint(response, "red")
        cs.send(str(response).encode())

    # -- Close the data socket
    cs.close()
