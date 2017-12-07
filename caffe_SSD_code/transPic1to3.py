import cv2
import os
def trans1to3(path):
    img = cv2.imread(path, 0)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    cv2.imwrite('./../data/JPEGImages3channel/{0}'.format(path.split('/')[-1]),img)
filepath = './../data/JPEGImages/'
for imgname in os.listdir(filepath):
    imgpath = os.path.join(filepath,imgname)
    trans1to3(imgpath)
