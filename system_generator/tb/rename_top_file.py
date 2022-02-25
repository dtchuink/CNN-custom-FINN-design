import numpy as np
import os
import sys
import random 
import subprocess
import csv

print ('Rename Top File - Number of arguments:', len(sys.argv), 'arguments.')

# Check if user gave argument
if((len(sys.argv) < 4) or (len(sys.argv) > 4)):    
    print("Rename Top File Error!!!! Please, provide a valid argument.")
    exit(1) 


top_function_start = sys.argv[3]
top_function = sys.argv[1]
file_name = sys.argv[2]

print("top_function_start=", top_function_start)

a_file = open(file_name, "r")  #get list of lines
lines = a_file.readlines()
a_file.close()

#[' kernel_dim ', ' stride ', ' ifm_channels', ' ofm_channels', ' simd', ' pe', ' ifm_dimension', ' ofm_dimension']
new_file = open(file_name, "w+")
#Delete "line2" from new_file
for line in lines:
    if top_function_start in line:
    	print("param found!!!!!")
    	print(line)
    	new_line = line.split("(",1)[1] 
    	print(new_line)
    	new_file.write(top_function_start+" "+top_function+"("+new_line)
    else:	
    	new_file.write(line)

new_file.close()


