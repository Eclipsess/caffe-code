
cur_dir='/home/sy/VOT/caffe/Stamp/code'
root_dir='/home/sy/VOT/caffe'

cd $root_dir

redo=1

data_root_dir="/home/sy/VOT/caffe/Stamp"
#save LMDB path : data_root_dir + dataset_name
dataset_name="Stampdata"
mapfile="/home/sy/VOT/caffe/Stamp/code/labelmap_voc.prototxt"
anno_type="detection"
db="lmdb"
min_dim=0
max_dim=0
width=0
height=0
True=True

extra_cmd="--encode-type=jpg --encoded"
if [ $redo ]
then
  extra_cmd="$extra_cmd --redo"
fi
for subset in test trainval
do
  python $root_dir/scripts/create_annoset.py --anno-type=$anno_type --label-map-file=$mapfile --min-dim=$min_dim --max-dim=$max_dim --resize-width=$width --resize-height=$height --check-label $extra_cmd $data_root_dir  $root_dir/Stamp/code/$subset.txt $data_root_dir/$dataset_name/$db/$dataset_name"_"$subset"_"$db $root_dir/Stamp/examples/$dataset_name
done
# two out_dir ?

