import os
import cv2
import pickle
import numpy as np
import matplotlib.pyplot as plt
import time

from pprint import pprint
from EyeClassFile import EyeClassDetails, EyeClass

# Defining Variavles
videosFilePath = 'testingvideos'
videosDataFile = open("annotation_training.pkl", "rb")
videosData = pickle.load(videosDataFile, encoding='latin1')

videoCounter = 0  # to keep track of current video for feature extraction

extraversionValue = neuroticismValue = conscientiousnessValue = opennessValue = interviewValue = agreeablenessValue = ''
labelDictionary = {}  # will contain labels from annotation_training file, # key = video name | values video,extraversion, neuroticism, conscientiousness, openness, interview , agreeableness
featuresDictionary = {} #will contain features extracted from the videos
eyeDetailsArray = [] # to store information about all the eyes for a single video

#HaarCascades for face feature detection
face_cascade = cv2.CascadeClassifier('HaarCascadeFiles/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('HaarCascadeFiles/haarcascade_eye.xml')
left_eye_cascade = cv2.CascadeClassifier('HaarCascadeFiles/haarcascade_lefteye_2splits.xml')
right_eye_cascade = cv2.CascadeClassifier('HaarCascadeFiles/haarcascade_righteye_2splits.xml')

# Loading the labels in labelDictionary, the key for each label is the video name
for x in videosData:
    for y in videosData[x]:
        extraversionValue = videosData['extraversion'][y]
        neuroticismValue = videosData['neuroticism'][y]
        conscientiousnessValue = videosData['conscientiousness'][y]
        opennessValue = videosData['openness'][y]
        interviewValue = videosData['interview'][y]
        agreeablenessValue = videosData['agreeableness'][y]
        labelDictionary[y] = [extraversionValue, neuroticismValue, conscientiousnessValue, opennessValue,
                                interviewValue, agreeablenessValue]

toBreakafter20 = 0
for i in range(0, len(labelDictionary) - 1):
    capVideo = cv2.VideoCapture(videosFilePath + '/' + list(labelDictionary.keys())[i]) #Loading the video
    while capVideo.isOpened():
        ret, frame = capVideo.read() # getting frames from the video
        if frame is None:
            break
        else:
            grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(grayFrame, 1.3, 5) # Detecting the face
            for (x, y, w, h) in faces:
                croppedFace = frame[y:y+h,x:x+h]
                croppedFaceGray = grayFrame[y:y+h,x:x+w]
                leftEye = left_eye_cascade.detectMultiScale(croppedFaceGray) # Detecting left eye
                rightEye = right_eye_cascade.detectMultiScale(croppedFaceGray) # Detecting right eye
                leftEyeObject = None
                rightEyeObject = None
                for(ex,ey,ew,eh) in leftEye:
                    cv2.rectangle(croppedFace, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                    leftEyeFrame = croppedFace[ey:ey+eh,ex:ex+ew]
                    leftEyeObject = EyeClassDetails(leftEyeFrame,'left',ex,ey,ex+ew,ey+eh)
                    break
                for (ex, ey, ew, eh) in rightEye:
                    cv2.rectangle(croppedFace, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                    rightEyeFrame = croppedFace[ey:ey + eh, ex:ex + ew]
                    rightEyeObject = EyeClassDetails(rightEyeFrame, 'right', ex, ey, ex + ew, ey + eh)
                    break
                eyeDetailsArray.append(EyeClass(leftEyeObject,rightEyeObject))
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        toBreakafter20+= 1
        if toBreakafter20 is 20:
            break
    if len(eyeDetailsArray) > 0:
        for k in range (0,len(eyeDetailsArray) - 1):
            if eyeDetailsArray[k].getRightEye() is not None:
                print(eyeDetailsArray[k].getRightEye().getEyeFrame())
                time.sleep(1)
    capVideo.release()
cv2.destroyAllWindows()
