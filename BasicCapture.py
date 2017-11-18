import picamera as pc
import os
from time import sleep
from picamera import PiCamera

#http://picamera.readthedocs.io/en/release-1.13/install.html

camera = PiCamera()
print(camera.resolution)
camera.resolution = (1360, 768)
#camera.start_preview()
#camera.stop_preview()

# Camera warm-up time
for i in range(0,5):
    sleep(1)
    camera.capture('./Capture/capture'+str(i)+'.jpg',resize=(442, 250))
