# Hu Invariants SK Version

from skimage.measure import moments_central
from skimage.measure import moments_normalized
from skimage.measure import moments_hu
import numpy as np
import cv2
import sys
from math import copysign,log10

if len(sys.argv) !=2:
   print('usage: {image_file}')
   sys.exit(1)
img = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
mu = moments_central(img)
nu = moments_normalized(mu)
np.set_printoptions(suppress=True,precision=5)
huM = moments_hu(nu)
for i in range(0,7):
   huM[i] = -1* copysign(1.0, huM[i].item()) * log10(abs(huM[i].item()))
print(huM)
