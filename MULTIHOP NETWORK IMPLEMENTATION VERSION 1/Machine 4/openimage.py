import pickle
import packetClass
import os
import subprocess

parent_dir = os.getcwd()

# get the filename
firstPKT = pickle.load(open(f'{parent_dir}\\packets\\1.pkt','rb'))
output_file_name = firstPKT.message_name
os.startfile(output_file_name)
