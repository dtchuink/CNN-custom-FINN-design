import numpy as np
import os
import sys
import random 
import subprocess
import csv

print ('Vitis script Number of arguments:', len(sys.argv), 'arguments.')

# Check if user gave argument
if((len(sys.argv) < 4) or (len(sys.argv) > 4)):    
    print("Vitis_compilation_script Error: Please, provide a valid, single argument, it should be  'top_function', 'file_name' and  'top_function_param'.")
    exit(1) 

project_prefix = sys.argv[1]
Layer_name = sys.argv[2]
ID =sys.argv[3]
file_name = "compile_project_vitis.tcl"

tcl_script = open(file_name, "wt")

tcl_script.write("open_project %s%s \n" % (project_prefix, Layer_name))
tcl_script.write("set_top %s%s \n" % (Layer_name, ID))

tcl_script.write("open_solution sol1 \n")
#tcl_script.write("set_part {xcvu9p-flgb2104-2-i} \n")
#tcl_script.write("create_clock -period 2.5 -name default \n")
tcl_script.write("csynth_design \n")
tcl_script.write("export_design -flow syn -rtl verilog -format syn_dcp")

tcl_script.close()

