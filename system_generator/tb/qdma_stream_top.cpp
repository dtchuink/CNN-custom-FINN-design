#include "ap_int.h"
#include <hls_stream.h>
#include "bnn-library.h"
#include "data/config_inj.h"

void qdma_conv_top(hls::stream<qdma_axis<128,0,0,0> > & in, hls::stream<qdma_axis<128,0,0,0> > & out){
#pragma HLS INTERFACE axis port=in
#pragma HLS INTERFACE axis port=out
	stream<ap_uint<128> > stream;
#pragma HLS RESOURCE variable=stream core=FIFO_LUTRAM
#pragma HLS STREAM variable=stream depth=32
#pragma HLS DATAFLOW
	Qdma2Stream_Batch<128, 1000>(in,stream, 1);
	Stream2Qdma_Batch<128, 1000>(stream, out, 1);
}


void qdma_conv(hls::stream<qdma_axis<MEM_DATA_WIDTH,0,0,0> > & in, stream<ap_uint<MEM_DATA_WIDTH> > & internal_stream){
#pragma HLS INTERFACE axis port=in

	Qdma2Stream_Batch<MEM_DATA_WIDTH, 500>(in, internal_stream, 1);
}
