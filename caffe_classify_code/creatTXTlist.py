# -*- coding: UTF-8 -*-
import os
import numpy as np
import shutil
"""
函数说明:生成图片列表清单txt文件

Parameters:
    images_path - 图片存放目录
    txt_save_path - 图片列表清单txt文件的保存目录
Returns:
    无
Author:
    eclipsycn
"""
def createFileList(images_path, txt_save_path, mode):
    #打开图片列表清单txt文件
    ft = open(txt_save_path+'trainList.txt',"w")
    fv = open(txt_save_path+'valList.txt',"w")
    #查看图片目录下的文件,相当于shell指令ls
    files_name = os.listdir(images_path)
    #遍历所有文件名
    #index = 0
    classfile = -1
    for filename in files_name:
        classfile += 1
        current_path = images_path + filename
        if mode == 1:
            current_label = classfile
        if mode == 0:
            current_label = filename
        val = 0
        lenimagename = len(os.listdir(current_path))
        number = np.random.randint(0, lenimagename,size = lenimagename/5)
        for imagename in os.listdir(current_path):
            val += 1
            imagepath = current_path + '/' + imagename
            if imagepath != None:
                if val in number:
                    fv.write(filename+'/'+imagename+ ' '+ str(current_label) + '\n')
                else:
                    ft.write(filename+'/'+imagename+ ' '+ str(current_label) + '\n')
                    
        #index += 1
        #if index == 1000: 
            #break
    #打印成功信息
    print "生成txt文件成功"
    #关闭fw
    ft.close()
    fv.close()


if __name__ == '__main__':
    #caffe_root目录
    caffe_root = '/home/sy/caffe/'
    #my-caffe-project目录
    #my_caffe_project = caffe_root + 'my-caffe-project/'
    #图片存放目录
    images_path = '/home/sy/Stamp294/data/'
    #生成的图片列表清单txt文件的保存目录
    txt_save_path = './'
    #生成txt文件
    #mode = 0 class = filename , mode = 1, class = create(0 ~ len)
    createFileList(images_path, txt_save_path, 1)
