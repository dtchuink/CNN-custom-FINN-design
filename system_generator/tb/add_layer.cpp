/******************************************************************************
 *  Copyright (c) 2021, Xilinx, Inc.
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions are met:
 *
 *  1.  Redistributions of source code must retain the above copyright notice,
 *     this list of conditions and the following disclaimer.
 *
 *  2.  Redistributions in binary form must reproduce the above copyright
 *      notice, this list of conditions and the following disclaimer in the
 *      documentation and/or other materials provided with the distribution.
 *
 *  3.  Neither the name of the copyright holder nor the names of its
 *      contributors may be used to endorse or promote products derived from
 *      this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 *  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 *  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 *  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
 *  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 *  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 *  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
 *  OR BUSINESS INTERRUPTION). HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 *  WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
 *  OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
 *  ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 ******************************************************************************/
/******************************************************************************
 *
 *  Authors: Timoteo Garcia Bertoa <timoteog@xilinx.com>
 *
 *  \file conv_stmr_top.cpp
 *
 *  HLS Top function with a single convolutional layer for unit testing
 *  including TMR check
 *
 *****************************************************************************/
#include <hls_stream.h>
using namespace hls;
#include "ap_int.h"
#include "bnn-library.h"

#include "data/add_config.h"

void conv_add(stream<ap_uint<NUM_CHANNELS * INPUT_WIDTH> > & in1, stream<ap_uint<NUM_CHANNELS * INPUT_WIDTH> > & in2, stream<ap_uint<NUM_CHANNELS * OUTPUT_WIDTH> > & out, const unsigned int numReps){

	if (SAT == 0)
		AddStreams_Batch<NUM_CHANNELS, ap_uint<INPUT_WIDTH>, ap_uint<INPUT_WIDTH>, ap_ufixed<OUTPUT_WIDTH, OUTPUT_WIDTH, AP_TRN>, NUM_WORDS, OFFSET>(in1, in2, out, numReps);
	else
		AddStreams_Batch<NUM_CHANNELS, ap_uint<INPUT_WIDTH>, ap_uint<INPUT_WIDTH>, ap_ufixed<OUTPUT_WIDTH, OUTPUT_WIDTH, AP_RND, AP_SAT>, NUM_WORDS, OFFSET>(in1, in2, out, numReps);
}
