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
i=1
count = 1
while i== 1:
    sleep(1)
    count = "%09d" % count
    print('./Capture/capture'+str(count)+'.jpg')
    camera.capture('./Capture/Monday9am/capture'+str(count)+'.jpg',resize=(442, 250))
    count = int(count) +1 