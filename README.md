# CNN-custom-FINN-design
This repository explores the performances of hardware accelerators generated with FINN-HLS framework. It allows to  authomatically  pre-implement different granularities of a model. 

One can generate design of a quantized model per:

  - Layer
  - Block (example residual block of ResNet)
  
  Run for the layer granularity:
    - python vitis_compilation_script.py

