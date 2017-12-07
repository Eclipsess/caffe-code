#!/usr/bin/env sh 

EXAMPLE=/home/suiyang/caffe/keyboarddata/example
DATA=/home/suiyang/caffe/keyboarddata/mean
TOOLS=/home/suiyang/caffe/build/tools

$TOOLS/compute_image_mean $EXAMPLE/keyboard50_train_lmdb \
    $DATA/mean.binaryproto

