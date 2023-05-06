import numpy as np
import pickle
from matplotlib import pyplot as plt
import random


def unpickle(file):    
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

path_pickles = 'ai8x-training/data/CIFAR10/cifar-10-batches-py/'

d = unpickle(path_pickles+'test_batch')

#gs = fig.add_gridspec(4,3, hspace=0, wspace = 1)
#axs = gs.subplots(sharex=True, sharey=True)

#gs = fig.add_gridspec(4, 3, hspace=1, wspace=0)
#axs= gs.subplots(sharex='col', sharey='row')#,hspace=0, wspace=0)

fig, axs = plt.subplots(4, 3)
for i_x in range(4):
    for i_y in range(3):
        k = int(1000*random.random())

        x = d[b'data'][k].astype('float')

        #x = np.clip(x-128, -128, 127)
        x = x/256

        img = np.zeros((32,32,3))
        img0 = np.reshape(x,(3,32,32))

        for i in range(32):
            for j in range(32):
                img[i][j] = img0[0][i][j],img0[1][i][j],img0[2][i][j]
        
        axs[i_x, i_y].imshow(img, interpolation='nearest')
        #np.save(str(i), xf, allow_pickle=False, fix_imports=False)
plt.show()
