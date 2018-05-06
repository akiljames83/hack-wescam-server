import numpy as np
import dlib
from skimage import io
from scipy.spatial import distance
from libs import *


try:

    img = io.imread('result.jpg')
    dets = detector(img, 1)

    for k, d in enumerate(dets):
        shape = sp(img, d)

    face_descriptor1 = facerec.compute_face_descriptor(img, shape)

    img2 = io.imread('detect.jpg')

    dets_webcam = detector(img2, 1)
    for k, d in enumerate(dets_webcam):
        shape2 = sp(img2, d)

    face_descriptor2 = facerec.compute_face_descriptor(img2, shape2)

    print(distance.euclidean(face_descriptor1, face_descriptor2))

except:
    pass
