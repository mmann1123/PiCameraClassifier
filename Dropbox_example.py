#https://liudr.wordpress.com/2016/02/20/dropbox-python-api/


import dropbox
import os
os.chdir(r'/home/pi/Documents/PiCameraClassifier/Capture/')

# read in dropbox token from file
token=open("../dropbox_auth.txt").readline().rstrip()


access_token = token
file_from = r'./Date_07_12_2017/Picapture_07.12.2017-15:22:00.jpg'
file_to = '/temp/photo.jpg'
 
def upload_file(file_from, file_to):
    dbx = dropbox.Dropbox(access_token)
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(),file_to)

response = upload_file(file_from,file_to)
print(response)





# Another option


import dropbox, sys, os

# read in dropbox token from file
token=open("../dropbox_auth.txt").readline().rstrip()

try:
  dbx = dropbox.Dropbox(token)
  user = dbx.users_get_current_account()
  print(user)
except:
  print ("Negative, Ghostrider dropbox api token not authenticated")
 
os.chdir(r'/home/pi/Documents/PiCameraClassifier/Capture/')

rootdir = os.getcwd()

print ("Attempting to upload...")
# walk return first the current folder that it walk, then tuples of dirs and files not "subdir, dirs, files"
for dir, dirs, files in os.walk(rootdir):
    for file in files:
        try:
            file_path = os.path.join(dir, file)
            dest_path = os.path.join('/test', file)
            print 'Uploading %s to %s' % (file_path, dest_path)
            with open(file_path) as f:               
                 dbx.files_upload(f.read(),dest_path)
        except Exception as err:
            print("Failed to upload %s\n%s" % (file, err))

print("Finished upload.")