//
//  face_detector.hpp
//  hack-wescam
//
//  Created by Igor Grishchenko on 2018-05-04.
//  Copyright © 2018 Igor Grishchenko. All rights reserved.
//

#ifndef face_detector_hpp
#define face_detector_hpp

#include "opencv2/objdetect.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include <stdio.h>
#include <iostream>

#define FACE_CASCADE "/Users/igrishchenko/Desktop/hack-wescam/hack-wescam/haarcascade_frontalface_alt.xml"

using namespace std;
using namespace cv;

class FaceDetector {
    
private:
    
    CascadeClassifier _faceCascade;
    void FindFace(Mat frame);
    
public:
    
    FaceDetector();
    void Pipeline();
};
#endif
