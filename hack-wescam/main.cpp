//
//  main.cpp
//  hack-wescam
//
//  Created by Igor Grishchenko on 2018-05-04.
//  Copyright © 2018 Igor Grishchenko. All rights reserved.
//

#include "face_detector.hpp"

int main(int argc, const char * argv[]) {

    
    FaceDetector *faceDetector = new FaceDetector();
    faceDetector->Pipeline();
    
    return 0;
}
