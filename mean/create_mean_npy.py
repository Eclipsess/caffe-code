import numpy as np

MEAN_NPY = 'mean.npy'

mean = np.ones([3,224, 224], dtype=np.float)
mean[0,:,:] = 104
mean[1,:,:] = 117
mean[2,:,:] = 123

np.save(MEAN_NPY, mean)


#mean_npy = np.load(MEAN_NPY_PATH)
#mean = mean_npy.mean(1).mean(1)
