
caffe_root_dir='/home/lq/caffe-ssd'
root_dir='/home/lq/fire_detection'

cd $root_dir

redo=1

data_root_dir="/home/lq/fire_detection"
#save LMDB path : data_root_dir + dataset_name
dataset_name="fire_data"
mapfile="/home/lq/fire_detection/code/labelmap_voc.prototxt"
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
  python $caffe_root_dir/scripts/create_annoset.py --anno-type=$anno_type --label-map-file=$mapfile --min-dim=$min_dim --max-dim=$max_dim --resize-width=$width --resize-height=$height --check-label $extra_cmd $data_root_dir $root_dir/code/$subset.txt $data_root_dir/$dataset_name/$db/$dataset_name"_"$subset"_"$db $root_dir/examples/$dataset_name
done
# two out_dir ?
