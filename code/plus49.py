import os
import shutil

path = '/home/suiyang/caffe/keyboarddata/Right_crop/out/'
filenames = os.listdir(path)
for filename in filenames:
    print filename
    newFilename = str(int(filename) + 49 )
    print newFilename
    shutil.move(os.path.join(path,filename), os.path.join('/home/suiyang/caffe/keyboarddata/Right_crop/w/',newFilename))


