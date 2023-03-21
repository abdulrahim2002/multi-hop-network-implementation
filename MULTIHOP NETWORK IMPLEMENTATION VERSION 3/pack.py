import socket
import math
import pickle
import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

# get the path of the file from file selection box
root = tk.Tk()
root.withdraw()

desktop = os.path.join(str(Path.home()) , 'Desktop')

# Set the initial directory for the file dialog box i.e. the desktop
file_path = filedialog.askopenfilename(initialdir=desktop, title="Select file to send")

# 'C:/Users/Abdul/Desktop/programs/dataComunicationAndSecurity/practical 2'
parent_dir = os.getcwd()

# returns host name of current machine
host_name = socket.gethostname()    

# returns ip address of current machine
host_ip = socket.gethostbyname(host_name)   

# input destination ip address
destination_ip = input("Enter the destination IP address(eg 127.0.0.1): ")

# payload contains actual data of the packet
payload_size = int(input("Enter Payload size of Packet(How many bytes/characters of information a packet will carry): "))

# input message from file
message = open(file_path, 'rb').read()

# (What kind of name will be given to message using which it will be delivered at
# the recipient side).
message_name = os.path.basename(file_path)

# (Presently use null certificate)
security_certificate = None

# function to convert the message into packets
def convertMessageToPacket(message):
    # calculate the number of packets
    # math.ceil() returns the smallest integer greater than or equal to x
    num_packets = math.ceil(len(message) / payload_size)

    # number of characters already read
    num_chars_read = 0
    
    # divide the message into packets
    for i in range(num_packets):

        # if last packet
        if i == num_packets - 1 and len(message) % payload_size != 0:
            # read characters from message
            curr_payload = message[num_chars_read:num_chars_read+payload_size]
            num_chars_read += len(curr_payload)
        else:
            # calculate the payload size of the current packet
            curr_payload = message[num_chars_read:num_chars_read+payload_size]
            num_chars_read += len(curr_payload)

        # create the current packet object
        # creaet data dictionary to store the data
        data = dict()
        data['client_id'] = host_name
        data['client_ip_address'] = host_ip
        data['destination_ip_address'] = destination_ip
        data['payload'] = curr_payload
        data['total_num_packets'] = num_packets
        data['current_packet_id'] = i+1
        data['message_name'] = message_name
        data['security_certificate'] = security_certificate
        
        # curr_packet = packetClass.Packet(
        #     client_id=host_name,
        #     client_ip_address=host_ip,
        #     destination_ip_address=destination_ip,
        #     payload=curr_payload,
        #     total_num_packets=num_packets,
        #     current_packet_id=i+1,
        #     message_name=message_name,
        #     security_certificate=security_certificate
        # )

        print(f"Packet id:{i+1} created")
        
        # dump the packet object into a file
        filename = f'{parent_dir}/packets/{i+1}.pkt'
        outfile = open(filename,'wb')
        pickle.dump(data, outfile)
    
    return

def main():
    convertMessageToPacket(message)

if __name__ == "__main__":
    main()