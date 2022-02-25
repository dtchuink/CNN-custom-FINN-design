import numpy as np
import os
import sys
import random 
import subprocess
import csv

print ('Number of arguments:', len(sys.argv), 'arguments.')

# Check if user gave argument
if((len(sys.argv) < 10) or (len(sys.argv) > 10)):    
    print("Error: Please, provide a valid, single argument, it should be either 'inj', 'no_inj' or 'tmrcheck'.")
    exit(1) 

kernel_dim_val = "kernel_dim = "
stride_val = "stride = "
ifm_channels_val = "ifm_channels = "
ofm_channels_val = "ofm_channels = "
simd_val = "simd = "
pe_val = "pe = "
ifm_dimension_val = "ifm_dimension = "
ofm_dimension_val = "ofm_dimension = "
precision_val = "input_precision = "

kernel_dim = sys.argv[1]
stride = sys.argv[2]
ifm_channels = sys.argv[3]
ofm_channels = sys.argv[4]
simd = sys.argv[5]
pe = sys.argv[6]
ifm_dimension = sys.argv[7]
ofm_dimension = sys.argv[8]
precision = sys.argv[9]


a_file = open("sample.py", "r")  #get list of lines
lines = a_file.readlines()
a_file.close()

#[' kernel_dim ', ' stride ', ' ifm_channels', ' ofm_channels', ' simd', ' pe', ' ifm_dimension', ' ofm_dimension']
new_file = open("gen_weights_param.py", "w+")
#Delete "line2" from new_file
for line in lines:
    if kernel_dim_val in line:
    	print("param found!!!!!")
    	print(line)
    	new_file.write(kernel_dim_val+kernel_dim+"\n")
    elif stride_val in line:
    	print(line)
    	new_file.write(stride_val+stride+"\n")
    elif ifm_channels_val in line:
    	print(line)
    	new_file.write(ifm_channels_val+ifm_channels+"\n")
    elif ofm_channels_val in line:
    	print(line)
    	new_file.write(ofm_channels_val+ofm_channels+"\n")
    elif simd_val in line:
    	print(line)
    	new_file.write(simd_val+simd+"\n")
    elif pe_val in line:
    	print(line)
    	new_file.write(pe_val+pe+"\n")
    elif ifm_dimension_val in line:
    	print(line)
    	new_file.write(ifm_dimension_val+ifm_dimension+"\n")
    elif ofm_dimension_val in line:
    	print(line)
    	new_file.write(ofm_dimension_val+ofm_dimension+"\n")
    elif precision_val in line:
    	print(line)
    	new_file.write(precision_val+precision+"\n")
    else:	
    	new_file.write(line)

new_file.close()


