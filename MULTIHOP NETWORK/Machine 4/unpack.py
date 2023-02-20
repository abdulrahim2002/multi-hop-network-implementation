import pickle
import packetClass
import os

output_file_name = "result.png"

# 'C:/Users/Abdul/Desktop/programs/dataComunicationAndSecurity/practical 2'
parent_dir = os.getcwd()

# open the file in append binary mode
output_file = open(os.path.join(parent_dir, output_file_name), mode='ab')

# function to convert the packets into message
def convertPacketToMessage(packet, string= False):
    if string:
        # decode the payload
        output_file.write(packet.payload.decode('utf-8'))
    else:
        # write the payload to the output file
        output_file.write(packet.payload)
    
    return


def main():

    # to know the number of packets 
    # create a packet object and read the total number of packets
    firstPKT = pickle.load(open(f'{parent_dir}/packets/1.pkt','rb'))
    num_packets = firstPKT.total_num_packets

    for i in range(num_packets):
        # read the packet
        packet = pickle.load(open(f'{parent_dir}/packets/{i+1}.pkt','rb'))
        print(f'packet id: {packet.packet_id} unapacked')
        # append the payload to file
        convertPacketToMessage(packet, string= False)

    # text = output_file.decode('utf-8')
    # print(text)

    # close the output file
    output_file.close()


if __name__ == "__main__":
    main()