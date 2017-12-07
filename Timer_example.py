import datetime, schedule, time
from datetime import date, datetime, timedelta
import picamera as pc
import os
from time import sleep
from picamera import PiCamera

os.chdir('/home/pi/Documents/PiCameraClassifier/')

# set up functions
def createtimes(start, end, delta):
    # https://stackoverflow.com/questions/10688006/generate-a-list-of-datetimes-between-an-interval
    curr = start
    while curr < end:
        yield curr
        curr += delta


      
# set camera parameters
camera = PiCamera()  #only do once
print(camera.resolution)
camera.resolution = (1360, 768)

def take_pics(num_of_photos):     
    # take 10 photos 
    i=1
    while i <= num_of_photos:
        time_now = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
        sleep(1) # Camera warm-up time
        newpath = r'./Capture/Date_'+ datetime.now().strftime("%d.%m.%Y")
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        
        print(newpath+'/Picapture_'+str(time_now)+'.jpg')
        camera.capture(newpath+'/Picapture_'+str(time_now)+'.jpg',resize=(442, 250))
        i = int(i) +1 



def job():
    global datelist
    date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    for i in datelist:
        runTime = i[0] + " " + i[1]
        if i and date == str(runTime):   # CHANGE ==
            take_pics(num_of_photos= 10)  # run image capture 10 pictures 




# set up start end dates and frequency of photo shoot
start_datetime = datetime(2017,12,8,6,00)
end_datetime = datetime(2017,12,8,18,30)
delta = timedelta(minutes=10)

datelist = []
for result in createtimes(start_datetime, end_datetime, delta):
    print('Staring picture capture at: '+result.strftime("%d.%m.%Y"),result.strftime("%H:%M:%S"))
    datelist.append((result.strftime("%d.%m.%Y"),result.strftime("%H:%M:%S")))        
 



# run the task 
schedule.every(0.01).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

    
     