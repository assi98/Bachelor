import os
"""
Project: https://github.com/theAIGuysCode/YoloGenerateTrainingFile/blob/master/generate_train.py
Author: TheAIGuysCode

Script for generating the train.txt and valid.txt used in Darknet. 
Add the script to the Darknet root folder, and run it from root after adding the training images to the darknet/data/obj folder and the validation images to the darknet/data/valid folder
"""

image_files = []
os.chdir(os.path.join("data", "obj"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("data/obj/" + filename)
os.chdir("..")
with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")

validation_files = []
os.chdir(os.path.join("data", "valid"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        validation_files.append("data/valid/" + filename)
os.chdir("..")
with open("valid.txt", "w") as outfile:
    for image in validation_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")