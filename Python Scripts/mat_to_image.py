from PIL import Image
import numpy as np
import scipy.misc
import cv2

f = open('test_matrix.txt')
text_data = f.read().replace('\n', '').split(';')

data = []

for line in text_data:
    
    data.append(list(map(int, line.replace('[', '').replace(']', '').replace(' ', '').split(','))))

rgba = cv2.cvtColor(np.asarray(data, dtype=np.float32), cv2.COLOR_GRAY2RGB)

cv2.imwrite('color.jpg', rgba)