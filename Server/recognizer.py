import numpy as np
import dlib
from skimage import io
from scipy.spatial import distance

sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()

try:

    img = io.imread('imgs/detect.jpg')
    dets = detector(img, 1)

    for k, d in enumerate(dets):
        shape = sp(img, d)

    face_descriptor1 = facerec.compute_face_descriptor(img, shape)

    img2 = io.imread('imgs/result.jpg')

    dets_webcam = detector(img2, 1)

    for k, d in enumerate(dets_webcam):
        shape = sp(img2, d)
        
    face_descriptor2 = facerec.compute_face_descriptor(img2, shape)

    print(distance.euclidean(face_descriptor1, face_descriptor2))

except:
    pass
