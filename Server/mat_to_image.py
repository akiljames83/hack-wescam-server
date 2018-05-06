from PIL import Image
import numpy as np
import scipy.misc
import cv2
import sys

try:
    
    data_mat = sys.argv[1]
    
    text_data = data_mat.replace('\n', '').split(';')
    
    data = []
    
    for line in text_data:
        
        data.append(list(map(int, line.replace('[', '').replace(']', '').replace(' ', '').split(','))))

    rgba = cv2.cvtColor(np.asarray(data, dtype=np.float32), cv2.COLOR_GRAY2RGB)

    cv2.imwrite('imgs/result.jpg', rgba)
except:
    pass
