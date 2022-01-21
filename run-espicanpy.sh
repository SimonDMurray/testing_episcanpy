#!/bin/bash

im=./epi_0.6.sif

singularity exec -B /lustre -B /nfs $im python3 test_epi.py
