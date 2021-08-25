import cv2     # for capturing videos
import math   # for mathematical operations
import os

"""
Code from: https://www.analyticsvidhya.com/blog/2018/09/deep-learning-video-classification-python/
Author: PULKIT SHARMA

With some adjustments.

Code for reading a video, extracting frames and saving them as images

"""

count = 0
video_dir = "video_dir/" # video path
frame_dir = "frame_dir/" # output path for frames
for root, directories, files in os.walk(video_dir):
    for file in files:
        videoFile = video_dir + file
        print(videoFile)
        cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path

        frameRate = cap.get(cv2.CAP_PROP_FPS) / 100 # returns frame rate divided by hundred

        while cap.isOpened():
            frameId = cap.get(1) #current frame number
            ret, frame = cap.read()
            if (ret != True):
                break
            if (frameId % math.floor(frameRate) == 0):
                filename = frame_dir + "frame%d.jpg" % count;count+=1
                cv2.imwrite(filename, frame)
        cap.release()
print ("Done!")