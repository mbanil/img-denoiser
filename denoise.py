
# import hyperspy.api as hs
# import numpy as np 
# import scipy.special 
# import scipy.signal
# import scipy.interpolate
# import scipy.linalg
# import scipy.fftpack
# import scipy.misc
# from scipy.spatial import distance
# import imageio
# from skimage.feature import match_template
# from skimage import io
# from functools import reduce
# from copy import deepcopy
# import matplotlib.pyplot as plt
# %matplotlib qt

import matplotlib.pyplot as plt
import numpy as np

from src import helperfuncs

folderPath = 'C:/My Documents/TUD-MCL/Semester 4/Thesis/Implementation/Data/Dataset-1/'
imgName = '18_04_27_Thomas_28618_0016.dm3'

radius=23
NumMainclasses=6
MinNumberInClass=4
MaxNumberInClass=100
myrun=0

imgs = helperfuncs.loadData(folderPath=folderPath, fileName=imgName)


# n1_max=1
# n1=0
# n2_max=len(imgs)
# n2=0
# plt.figure(figsize=(20, 20*n2_max/n1_max)) 
# for img in imgs:
#     n2+=1    
#     vstd=np.std(img)
#     vmean=np.mean(img)         
#     ax1=plt.subplot(n2_max,n1_max,n1*n2_max+n2)
#     ax1.imshow(img,cmap='gray',vmin=max(vmean-9*vstd,np.min(img)),vmax=min(vmean+9*vstd,np.max(img)))
#     ax1.axis('off')

# plt.show()

startPosList= [[84-radius,404-radius],[97-radius,404-radius],[88-radius,404-radius]]
templates = helperfuncs.generateTemplates(startPosList=startPosList, imgs=imgs, radius=radius)

templates = helperfuncs.findDissimilarTemplates(templates = templates, imgs = imgs, radius = radius, minTemplateClasses = NumMainclasses)

print(templates[0].shape)

n1_max= 1
n1=0
n2_max=len(templates)
n2=0
plt.figure(figsize=(20, 20*n2_max/n1_max)) 
for template in templates:
    n2+=1
    plt.subplot(n2_max, n1_max, n1*n2_max+n2)
    plt.imshow(template, cmap='gray')
    plt.axis('off')

plt.show()