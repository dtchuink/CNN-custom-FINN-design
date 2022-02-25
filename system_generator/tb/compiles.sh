#!/bin/sh
##############################################################################
#
# Main file to compile and generate DCP of CNN layers as defined in "configuration.txt"
#
# @Danielle Tchuinkou
#
##############################################################################

# 1. Edit gen_params_stmr.py
# 2. Compile gen_params_stmr.py


project_prefix="hls-syn-"
project_suffix="_top.cpp"
top_function_start="void "

#Prepare the different projects for synthesis
vitis_hls test_conv3.tcl
vitis_hls test_pool.tcl
vitis_hls test_add.tcl

#Read the configuration file
exec < configuration.txt || exit 1
read header # read (and ignore) the first line
while IFS="," read -r Layer_name ID kernel_dim  stride  ifm_channels ofm_channels simd pe ifm_dimension ofm_dimension precision reps
do
 
  if [ $Layer_name = "conv" ];
  then 
  	  echo $Layer_name
	  cd data
	  pwd
	  python3 update_config.py $kernel_dim  $stride  $ifm_channels $ofm_channels $simd $pe $ifm_dimension $ofm_dimension $precision
	  python3 gen_weights_param.py
	  cd ..
	  
	  
   elif [ $Layer_name = "pool" ];
   then
	echo $Layer_name
   	cd data
	#pwd
	python3 update_pool_config.py $kernel_dim  $stride  $ifm_channels $ifm_dimension $ofm_dimension $precision $reps $pe
	cd ..

   fi
   
   #top_function, file_name top_function_start
   python3 rename_top_file.py $Layer_name$ID $Layer_name$project_suffix $top_function_start
   #3. compile vitis project
   python3 vitis_compilation_script.py $project_prefix $Layer_name $ID
   vitis_hls compile_project_vitis.tcl
   #copy finaldcp
   cp $project_prefix$Layer_name/sol1/impl/verilog/project.runs/synth_1/$Layer_name$ID".dcp" /home/administrator/project/ResnetBlock/layerResults/
   cp $project_prefix$Layer_name/sol1/impl/report/verilog/$Layer_name$ID"_export.rpt" /home/administrator/project/ResnetBlock/layerResults/
   cp $project_prefix$Layer_name/sol1/syn/report/$Layer_name$ID"_csynth.rpt" /home/administrator/project/ResnetBlock/layerResults/
done 

#cd data
#python3 gen_weigths.py
#cd ..

#3. compile vitis project
#open_project hls-syn-conv
#csynth_design
#export_design -flow syn -rtl verilog -format syn_dcp 


#conv11 activation width 6, higher bit with exceed bus width of 4096
