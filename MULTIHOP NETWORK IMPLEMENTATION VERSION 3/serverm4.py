import socket
import subprocess
from time import sleep

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
hostName = socket.gethostname()
host = socket.gethostbyname(hostName)
port = 9999
BUFFERSIZE = 10000

# bind the socket to a public host and a port
serversocket.bind((host, port))

print('\nServer Machine 4\n')

# set the socket to listening mode
serversocket.listen(5)
print(f"[*] Listening as {host}:{port}")

# accept a connection from client
clientsocket, addr = serversocket.accept()
print("Got a connection from %s\n" % str(addr))

# receive data from the client
data = clientsocket.recv(BUFFERSIZE)
num_packets = int(data.decode('utf-8'))
message = f"Total number of packets: {data.decode('utf-8')}"
print("Received: %s\n" % message)

# send a response to the client
message = "ACK0"
clientsocket.send(message.encode('utf-8'))

packets = [] # a list of byte arrays
# recieve the packet
for i in range(num_packets):
    # recieve the packet
    response = clientsocket.recv(BUFFERSIZE)
    if response:
        print(f"Received Packet: {i+1}")
        packets.append(response)
    else:
        print("Packet not received. Closing the connection.")
        clientsocket.close()
    # send the ACK
    clientsocket.send(str(f"ACK{i+1}").encode('utf-8'))
    print(f"Sent ACK: {i+1}\n")
    

for i in range(num_packets):
    # write the packet to a file
    filename = f'packets/{i+1}.pkt'
    with open(filename, 'wb') as f:
        f.write(packets[i])
        f.close()

# close the socket
clientsocket.close()

# fire the forward to unpack script
process = subprocess.Popen(['cmd', '/C', 'unpack.bat'], creationflags= subprocess.CREATE_NEW_CONSOLE)
exit_code = process.wait()

# fire the forward to openimage script
process = subprocess.Popen(['cmd', '/C', 'openimg.bat'], creationflags= subprocess.CREATE_NEW_CONSOLE)
exit_code = process.wait()