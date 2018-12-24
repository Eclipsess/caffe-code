#!/bin/bash

root_dir=../
sub_dir=ImageSets/Main
#get bash absolute path
bash_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
for dataset in trainval test
do
  dst_file=$bash_dir/$dataset.txt
  if [ -f $dst_file ]
  then
    rm -f $dst_file
  fi
  for name in data
  do

    echo "Create list for $name $dataset..."
    dataset_file=$root_dir/$name/$sub_dir/$dataset.txt

    img_file=$bash_dir/$dataset"_img.txt"
    cp $dataset_file $img_file
    # replace "s / #old ( ^ ) / #new ($name/JPEGImages/) /g "
    # $:end replace .jpg 
    #mac need add ""
    sed -i "s/^/$name\/JPEGImages\//g" $img_file 
#####!    /r ########!!!######
    sed -i "s/$/.jpg/g" $img_file
    label_file=$bash_dir/$dataset"_label.txt"
    cp $dataset_file $label_file
    sed -i "s/^/$name\/Annotations\//g" $label_file
    sed -i "s/$/.xml/g" $label_file

    # connect two files with ' ' 
    paste -d' ' $img_file $label_file >> $dst_file

    rm -f $label_file
    rm -f $img_file
  done
done
