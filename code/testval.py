import sys
import os
import time
caffe_root = '/Users/eclipsycn/Documents/caffe/' 
sys.path.append(caffe_root + 'python')
import caffe
import cv2
import numpy as np

caffemodel = '/Users/eclipsycn/Documents/Stamp_Proj/Stamp294_Resnet50/snapshot/resnet__iter_20000.caffemodel'
deploy = '/Users/eclipsycn/Documents/Stamp_Proj/Stamp294_Resnet50/prototxt/ResNet_50_deploy.prototxt'
testfile = '/Users/eclipsycn/Documents/Stamp_Proj/Stamp294_Resnet50/test/'
mean_file = '/Users/eclipsycn/Documents/Stamp_Proj/Stamp294_Resnet50/mean/mean104_113_127.npy'
caffe.set_mode_cpu()
net = caffe.Net(deploy, caffemodel, caffe.TEST)

def getCategory(imagepath):
	img = caffe.io.load_image(imagepath)
	transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
        transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))
	transformer.set_transpose('data', (2,0,1))
	transformer.set_raw_scale('data',255)
	transformer.set_channel_swap('data', (2,1,0))

	net.blobs['data'].data[...] = transformer.preprocess('data', img)

	#	start = time.time()
	out = net.forward()
	#out = net.predict([img])
	#predicts = out.argmax()
	#print predicts
	#	end = time.time()

	#category = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
	category = net.blobs['prob'].data[0].argmax()
	#print category
	return category
def testValList():
    start = time.time()
    total = 0
    accuracycount = 0 
    labdic = {}
    labels = np.loadtxt('/Users/eclipsycn/Documents/Stamp_Proj/Stamp294_Resnet50/code/valList.txt', str, delimiter = '\t')
    for label in labels:
	    if labdic.has_key(label.split(' ')[1]):
		    continue
	    else:
		    labdic[label.split(' ')[1]] = label.split(' ')[0]
    for valpath in labels:
	    imagepath = testfile + valpath.split(' ')[0]
	    total += 1
	    #print total
	    predict = getCategory(imagepath)
	    if valpath.split(' ')[0].split('/')[0] == labdic[str(predict)].split('/')[0]:
		    accuracycount += 1
	    else:
		    print 'true class:',valpath.split(' ')[0]
		    print 'predict class:',labdic[str(predict)]
            print float(accuracycount)/total
    print total,time.time()-start
#testValList()
def testTestSet(testfile):
    start = time.time()
    total = 0
    accuracycount = 0 
    labdic = {}
    labels = np.loadtxt('/Users/eclipsycn/Documents/Stamp_Proj/Stamp294_Resnet50/code/valList.txt', str, delimiter = '\t')
    for label in labels:
	    if labdic.has_key(label.split(' ')[1]):
		    continue
	    else:
		    labdic[label.split(' ')[1]] = label.split(' ')[0]
    for valpath in os.listdir(testfile):
        imgfilepath = testfile + valpath + '/'
        for imgname in os.listdir(imgfilepath):
            imagepath = imgfilepath + imgname
            total += 1
	        #print total
            predict = getCategory(imagepath)
            if valpath == labdic[str(predict)].split('/')[0]:
                accuracycount += 1
            else:
                print 'true class:',valpath+'/'+imgname
                print 'predict class:',labdic[str(predict)].split('/')[0]
            print float(accuracycount)/total
    print total,time.time()-start
testTestSet(testfile)
#net = caffe.Classifier(deploy, caffemodel, channel_swap= (2,1,0),raw_scale = 255)
#for num in range(1,42):
#    if len(str(num)) == 1:
#		num = '0' + str(num)
#    else:
#        num = str(num)
#    print num
	#img = caffe.io.load_image('/home/sy/Stamp/sku/YP10000{0}/YP10000{1}.jpg'.format(num,num))

#labels = np.loadtxt('/home/sy/Stamp/valList.txt', str, delimiter = '\t')
    #print 'YP10000{0}:'.format(num)
#for label in labels:
#    if label[7:9] == '40':
#		print label.split(' ')[1]
#		break
#for i in np.arange(category.size):
#	print category[i]
#    print '\n'
