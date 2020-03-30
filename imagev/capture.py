#import numpy as np
import cv2
import os
import os.path
from os import path
import shutil
class Capture(object):
    def __init__(self, camera=None):
        self.camera=camera

    def capture(self):
        frame=cv2.imread(os.getcwd() + "\\images\\salida.jpg")
        b,g,r=cv2.split(frame)
        if self.camera==0:
            self.outputFrame = b
        if self.camera==1:
            self.outputFrame = g
        if self.camera == 2:
            self.outputFrame = r

        print("SENT")
    def generate(self):
        # encode the frame in JPEG format
        (flag, encodedImage) = cv2.imencode(".jpg", self.outputFrame)
        # ensure the frame was successfully encoded

        # yield the output frame in the byte format
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')


