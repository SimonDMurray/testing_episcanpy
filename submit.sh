#!/bin/bash

set -euo pipefail

MEM=35000
CPU=8
SCRIPT=$1
QUE="long"
WDIR=`pwd`


bsub -G cellgeni -n $CPU -R"span[hosts=1] select[mem>$MEM] rusage[mem=$MEM]" -M $MEM -o $WDIR/%J.bsub.log -e $WDIR/%J.bsub.err -q $QUE $WDIR/$SCRIPT

#bubba -l logs -t $name -n $cpu -q long -m $mem ./run-espicanpy.sh $cpu $name
