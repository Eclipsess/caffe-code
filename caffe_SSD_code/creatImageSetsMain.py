# -*- coding:utf-8 -*-
import os

JPEGImagesPath = '/home/sy/VOT/caffe/Stamp/data/JPEGImages/'
ImageSets = '/home/sy/VOT/caffe/Stamp/data/ImageSets/Main/'
trainvalpath = 'trainval.txt'
testpath = 'test.txt'
#打开图片列表清单txt文件
ft = open(ImageSets + trainvalpath,"w")
fv = open(ImageSets + testpath,"w")
#遍历所有文件名
val = 0
lenJPEG = len(os.listdir(JPEGImagesPath))
#test set 占百分之10
testnum = 100 / 10
for imagename in os.listdir(JPEGImagesPath):
    val += 1
    if val % testnum == 0:
        fv.write(imagename.split('.')[0] + '\n')
    else:
        ft.write(imagename.split('.')[0] + '\n')
#打印成功信息
print "生成txt文件成功"
#关闭fw
ft.close()
fv.close()
