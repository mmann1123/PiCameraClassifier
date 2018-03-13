import datetime, schedule, time, os, sys, dropbox
from datetime import date, datetime, timedelta
import picamera as pc
from time import sleep
from picamera import PiCamera

# path for folder where image folders should be written to 
os.chdir('/home/pi/Documents/PiCameraClassifier/Capture')

# set up start end dates and frequency of photo shoot
start_datetime = datetime(2018,3,7,1,00)
end_datetime = datetime(2018,3,19,18,30)
delta = timedelta(minutes=2)

# read in dropbox token from file
token=open("../dropbox_auth.txt").readline().rstrip()

# upload backup to dropbox and delete file if sucessfull
try:
  dbx = dropbox.Dropbox(token)
  user = dbx.users_get_current_account()
  print(user)
except:
  print ("Negative, Ghostrider dropbox api token not authenticated")
 

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

# function that takes pictures and stores in time folders
def take_pics(num_of_photos):     
    # take 10 photos 
    i=1
    while i <= 
    :
        time_now = datetime.now().strftime("%d_%m_%Y-%H:%M:%S")
        sleep(1) # Camera warm-up time
        newpath = r'./Date_'+ datetime.now().strftime("%d_%m_%Y")
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        
        print(newpath+'/Picapture_'+str(time_now)+'.jpg')
        camera.capture(newpath+'/Picapture_'+str(time_now)+'.jpg',resize=(442, 250))
        i = int(i) +1 
   
    rootdir = os.getcwd()

    print ("Attempting to upload...")
    # walk return first the current folder that it walk, then tuples of dirs and files not "subdir, dirs, files"
    for dir, dirs, files in os.walk(rootdir):
        for file in files:
            try:
                file_path = os.path.join(dir, file)
                dest_path = os.path.join('/',datetime.now().strftime("%d_%m_%Y"), file)
                print 'Uploading %s to %s' % (file_path, dest_path)
                with open(file_path) as f:               
                     dbx.files_upload(f.read(),dest_path)
                     os.remove(file_path)
            except Exception as err:
                print("Failed to upload %s\n%s" % (file, err))
    print("Finished upload.")



# call the photo job
def job():
    global datelist
    date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    for i in datelist:
        runTime = i[0] + " " + i[1]
        if i and date == str(runTime):   # CHANGE ==
            take_pics(num_of_photos= 2)  # run image capture 2 pictures 


datelist = []
for result in createtimes(start_datetime, end_datetime, delta):
    # limit to day time hours
    if int(result.strftime("%H")) >=7 and int(result.strftime("%H")) <=19:
	print('Staring picture capture at: '+result.strftime("%d.%m.%Y"),result.strftime("%H:%M:%S"))
    	datelist.append((result.strftime("%d.%m.%Y"),result.strftime("%H:%M:%S")))        
 

# run the task 
schedule.every(0.01).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

    
    
    
    



     
