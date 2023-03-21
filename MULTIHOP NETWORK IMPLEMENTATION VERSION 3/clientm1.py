# get the IP address of the server to connect
host = "192.168.56.1"

import socket
import subprocess
import os
import pickle

parent_dir = os.getcwd()

# trigger pack script from pack.bat
process = subprocess.Popen(['cmd', '/C', 'pack.bat'], creationflags= subprocess.CREATE_NEW_CONSOLE)
exit_code = process.wait()

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9999
BUFFERSIZE = 10000
ACK = 30
print('\nClient Machine 1\n')
print(f"[+] Connecting to {host}:{port}")
clientsocket.connect((host, port))
print("[+] Connected.\n")

# find the number of packets
firstPKT = pickle.load(open(f'{parent_dir}\\packets\\1.pkt','rb'))
num_packets = firstPKT['total_num_packets']

# send data to the server
clientsocket.send(str(num_packets).encode('utf-8'))

# receive response from the server
response = clientsocket.recv(BUFFERSIZE)
print("Received: %s\n" % response.decode('utf-8'))

if response.decode('utf-8') == "ACK0":
    pass
else:
    print("ACK0 not received. Closing the connection.")
    clientsocket.close()

packets = [] # a list of byte arrays
# create a packet object and add packet fils to it
for i in range(num_packets):
    filename = f'{parent_dir}/packets/{i+1}.pkt'
    # declare a byte array
    data = bytearray()
    data.extend(open(filename, 'rb').read())
    packets.append(data)

# send the packets
for i in range(num_packets):
    # data = packets[i].read(BUFFERSIZE)
    # send the packet file
    clientsocket.send(packets[i])
    print(f"Sent packet: {i+1}")
    # receive response from the server
    response = clientsocket.recv(ACK)
    if response.decode('utf-8') == f"ACK{1+i}":
        print("Received ACK: %s\n" % response.decode('utf-8'))
    else:
        print("ACK not received. Closing the connection.")
        clientsocket.close()

# close the socket
clientsocket.close()