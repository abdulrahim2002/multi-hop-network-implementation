import pickle
import os

# 'C:/Users/Abdul/Desktop/programs/dataComunicationAndSecurity/practical 2'
parent_dir = os.getcwd()

# get the filename ,to know the number of packets 
firstPKT = pickle.load(open(f'{parent_dir}/packets/1.pkt','rb'))
output_file_name = firstPKT['message_name']
num_packets = firstPKT['total_num_packets']

def main():
    
    # open the  output file in append binary mode
    output_file = open(os.path.join(parent_dir, output_file_name), mode='ab')

    for i in range(num_packets):
        # read the packet
        packet = pickle.load(open(f'{parent_dir}/packets/{i+1}.pkt','rb'))
        # append the payload to file
        convertPacketToMessage(output_file ,packet, string= False)

    # close the output file
    output_file.close()
    return output_file_name


# function to convert the packets into message
def convertPacketToMessage(outputFile, packet, string= False):
    if string:
        # decode the payload
        outputFile.write(packet['payload'].decode('utf-8'))
    else:
        # write the payload to the output file
        outputFile.write(packet['payload'])
    
    return


if __name__ == "__main__":
    main()