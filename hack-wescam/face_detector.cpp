//
//  face_detector.cpp
//  hack-wescam
//
//  Created by Igor Grishchenko on 2018-05-04.
//  Copyright © 2018 Igor Grishchenko. All rights reserved.
//

#include "face_detector.hpp"


FaceDetector::FaceDetector() {
    
    assert(_faceCascade.load(FACE_CASCADE));
}


void FaceDetector::FindFace(Mat frame) {
    
    vector<Rect> faces;
    
    Mat processedFrame;
    
    //: Color 2 Gray
    cvtColor(frame, processedFrame, COLOR_BGR2GRAY);
    
    //: NOTE: Drops performance, but might be needed later
    //equalizeHist(processedFrame, processedFrame);
    
    //: Detects all the faces in the frame
    _faceCascade.detectMultiScale(processedFrame, faces, 1.1, 2, 0 | CASCADE_SCALE_IMAGE, Size(60, 60));
    
    for (size_t iFace = 0; iFace < faces.size(); iFace++) {
        
        rectangle(frame, faces[iFace], Scalar(255,0,0));
    }
}


void FaceDetector::Pipeline() {
    
    VideoCapture capture;
    Mat frame;
    capture.open(0);
    
    if (!capture.isOpened()) {
        
        printf("Error opening video capture\n");
    }
    
    while (capture.read(frame)) {
        
        if(frame.empty()) {
            
            printf("No captured frame -- Break!");
            
            break;
        }
        
        this->FindFace(frame);
        imshow("dis", frame);
        
        if(waitKey(10) == 27) break;
    }
}
