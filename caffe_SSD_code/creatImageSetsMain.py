# -*- coding:utf-8 -*-
import os
import shutil
import os.path as osp

imageSourcePath = '/home/lq/fire_detection/fire_pic_change'
xmlSourcePath = '/home/lq/fire_detection/fire_xml_change'

objdatapath = '../data'
JPEGImagesPath = osp.join(objdatapath, 'JPEGImages')
ImageSets_Main_Path = osp.join(objdatapath, 'ImageSets/Main')
AnnotationsPath = osp.join(objdatapath, 'Annotations')

def generateDataPath(imgsourcepath, xmlsourcepath):
    for path in [JPEGImagesPath, ImageSets_Main_Path, AnnotationsPath]:
        if not osp.exists(path):
            os.makedirs(path)
    for imgname in os.listdir(imgsourcepath):
        shutil.copy(osp.join(imgsourcepath, imgname), osp.join(JPEGImagesPath, imgname)) 
    for xmlname in os.listdir(xmlsourcepath):
        shutil.copy(osp.join(xmlsourcepath, xmlname), osp.join(AnnotationsPath, xmlname)) 

generateDataPath(imageSourcePath, xmlSourcePath)

trainvalpath = 'trainval.txt'
testpath = 'test.txt'
#打开图片列表清单txt文件
ft = open(osp.join(ImageSets_Main_Path, trainvalpath),"w")
fv = open(osp.join(ImageSets_Main_Path, testpath),"w")
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
