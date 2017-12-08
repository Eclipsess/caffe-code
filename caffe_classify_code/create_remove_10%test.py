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
    Jack Cui
Modify:
    2017-03-29
"""
def createFileList(images_path, test_save_path):

    files_name = os.listdir(images_path)
    
    #遍历所有文件名
    #index = 0
    for filename in files_name:
        current_path = images_path + filename
        current_label = filename
        if not os.path.exists('{0}{1}'.format(test_save_path,filename)):
            os.mkdir('{0}{1}'.format(test_save_path, filename))
        val = 0
        lenimagename = len(os.listdir(current_path))
        number = np.random.randint(0, lenimagename,size = lenimagename/10)
        for imagename in os.listdir(current_path):
            val += 1
            imagepath = current_path + '/' + imagename
            if imagepath != None:
                if val in number:
                    shutil.copy(imagepath,'{0}{1}'.format(test_save_path,filename))
                    os.remove(imagepath)

    print "finished create extra test dataset"
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
    # 10%test picture save path
    test_save_path = '/home/sy/Stamp294/test/'
    #生成txt文件
    createFileList(images_path, test_save_path)
